import json
import os
import importlib
from utils.Singleton import Singleton


class StaticAnalysis(metaclass=Singleton):
    def __init__(self, rules_path, debug) -> None:
        self.debug = debug
        with open(rules_path, 'r') as f:
            self.rules = f.read().split('\n')
        self.rule_map = dict()
        self.load()

    def load(self):
        rule_dir = os.path.join(os.path.dirname(__file__), 'Rules')
        module_files = [f for f in os.listdir(
            rule_dir) if f.endswith('.py') and f != '__init__.py']
        for module_file in module_files:
            module_name = f"Tests.Rules.{module_file[:-3]}"
            module = importlib.import_module(module_name)
            class_name = module_file[:-3]
            cls = getattr(module, class_name, None)
            t = cls()
            t, v = t.definition()

            self.rule_map[t] = v

    def test_rule(self, rule_func, layer_idx, rule_tokens, violations_list):
        return_val = rule_func(self.layers, layer_idx, rule_tokens)
        if return_val == False:
            violations_list.append(
                f'Violation of Rule ({" ".join(rule_tokens)}) at Layer "{self.layers[layer_idx]["name"]}"'
            )
        return return_val

    def analyze(self, layers):
        self.layers = layers

        violations_list = []
        for layer_idx in range(len(self.layers)):
            for rule in self.rules:
                if rule.startswith('//') or rule.strip() == '':
                    continue
                rule_tokens = rule.split()
                print(rule)
                self.test_rule(
                    self.rule_map[rule_tokens[1]],
                    layer_idx,
                    rule_tokens,
                    violations_list
                )

        if self.debug:
            for violation in violations_list:
                print(violation)
                print("analyze")

        return violations_list


if __name__ == "__main__":
    analyzer = StaticAnalysis(
        'public/Rules/warning_rules.txt',
    )
    analyzer.analyze('TESTS/Banna.json')
