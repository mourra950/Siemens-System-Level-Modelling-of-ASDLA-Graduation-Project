from secondfile import pathss
from superClass import SUUper

class third(SUUper,pathss):
    def __init__(self) -> None:
        # super().__init__()
        SUUper.__init__(self)
        pathss.__init__(self)
        print(self.a)
        
        print(self.b)
        
        
def main():
    test=third()

main()