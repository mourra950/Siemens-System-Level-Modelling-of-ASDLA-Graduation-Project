import json

from utils.Singleton import Singleton

class StaticAnalysis(metaclass=Singleton):
    def __init__(self, rules_path, debug) -> None:
        self.debug = debug
        with open(rules_path, 'r') as f:
            self.rules = f.read().split('\n')
        self.rule_map = {
            # Layer1 -> Layer2
            '->': self.after_comes_directly,
            # Layer1 ->x Layer2
            '->x': self.after_comes_not_directly,
            # Layer1 --> Layer2
            '-->': self.after_comes,
            # Layer1 -->x Layer2
            '-->x': self.after_comes_not,

            # Layer1 <- Layer2
            '<-': self.before_comes_directly,
            # Layer1 <-x Layer2
            '<-x': self.before_comes_not_directly,
            # Layer1 <-- Layer2
            '<--': self.before_comes,
            # Layer1 <--x Layer2
            '<--x': self.before_comes_not,

            # (Layer1,Layer2) <--> Layer3
            '<-->': self.between_comes
        }


    def test_rule(self, rule_func, layer_idx, rule_tokens, violations_list):
        return_val = rule_func(layer_idx, rule_tokens)
        if return_val == False:
            violations_list.append(
                f'Violation of Rule ({" ".join(rule_tokens)}) at Layer "{self.layers[layer_idx]["name"]}"'
            )
        return return_val


    # Layer1 -> Layer2
    def after_comes_directly(self, layer_idx, rule_tokens) -> bool:
        if self.layers[layer_idx]['type'] != rule_tokens[0]:
            return True
        if layer_idx >= len(self.layers)-1:
            return True    
        if self.layers[layer_idx+1]['type'] == rule_tokens[2]:
            return True
        return False
    
    # Layer1 ->x Layer2
    def after_comes_not_directly(self, layer_idx, rule_tokens) -> bool:
        if self.layers[layer_idx]['type'] != rule_tokens[0]:
            return True
        if layer_idx >= len(self.layers)-1:
            return True
        if self.layers[layer_idx+1]['type'] != rule_tokens[2]:
            return True
        return False
    
    # Layer1 --> Layer2
    def after_comes(self, layer_idx, rule_tokens) -> bool:
        if self.layers[layer_idx]['type'] != rule_tokens[0]:
            return True
        if layer_idx >= len(self.layers)-1:
            return True
        for i in range(layer_idx+1, len(self.layers)):
            if self.layers[i]['type'] == rule_tokens[2]:
                return True
        return False
    
    # Layer1 -->x Layer2
    def after_comes_not(self, layer_idx, rule_tokens) -> bool:
        if self.layers[layer_idx]['type'] != rule_tokens[0]:
            return True
        if layer_idx >= len(self.layers)-1:
            return True
        for i in range(layer_idx+1, len(self.layers)):
            if self.layers[i]['type'] == rule_tokens[2]:
                return False
        return True
        
    # Layer1 <- Layer2
    def before_comes_directly(self, layer_idx, rule_tokens) -> bool:
        if self.layers[layer_idx]['type'] != rule_tokens[0]:
            return True
        if layer_idx <= 0:
            return True 
        if self.layers[layer_idx-1]['type'] == rule_tokens[2]:
            return True
        return False
    
    # Layer1 <-x Layer2
    def before_comes_not_directly(self, layer_idx, rule_tokens) -> bool:
        if self.layers[layer_idx]['type'] != rule_tokens[0]:
            return True
        if layer_idx <= 0:
            return True
        if self.layers[layer_idx-1]['type'] != rule_tokens[2]:
            return True
        return False
       
    # Layer1 <-- Layer2
    def before_comes(self, layer_idx, rule_tokens) -> bool:
        if self.layers[layer_idx]['type'] != rule_tokens[0]:
            return True
        if layer_idx <= 0:
            return True
        for i in range(0, layer_idx):
            if self.layers[i]['type'] == rule_tokens[2]:
                return True
        return False
    
    # Layer1 <--x Layer2
    def before_comes_not(self, layer_idx, rule_tokens) -> bool:
        if self.layers[layer_idx]['type'] != rule_tokens[0]:
            return True
        if layer_idx <= 0:
            return True
        for i in range(0, layer_idx):
            if self.layers[i]['type'] == rule_tokens[2]:
                return False
        return True
    

    # (Layer1,Layer2) <--> Layer3
    def between_comes(self, layer_idx, rule_tokens):
        layer_1, layer_2 = rule_tokens[0][1:-1].split(',')
        if self.layers[layer_idx]['type'] != layer_1:
            return True
        if layer_idx >= len(self.layers):
            return True
        for i in range(layer_idx+1, len(self.layers)):
            if self.layers[i]['type'] == layer_2:
                return False
            if self.layers[i]['type'] == rule_tokens[2]:
                return True
        return True
        

    def analyze(self, arch_json_path):
        with open(arch_json_path, 'r') as f:
            self.layers = json.loads(f.read())['layers']['list']
        violations_list = []
        for layer_idx in range(len(self.layers)):
            for rule in self.rules:
                if rule.startswith('//') or rule.strip() == '':
                    continue
                rule_tokens = rule.split()

                self.test_rule(
                    self.rule_map[rule_tokens[1]],
                    layer_idx,
                    rule_tokens,
                    violations_list
                )

        if self.debug:
            for violation in violations_list:
                print(violation)
        return violations_list


if __name__ == "__main__":
    analyzer = StaticAnalysis(
        'public/Rules/warning_rules.txt',
    )   
    analyzer.analyze('TESTS/Banna.json')