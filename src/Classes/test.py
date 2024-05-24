class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Python3
class MyClass(metaclass=Singleton):
    def __init__(self, value):
        self.value = value
        self.list = []

    def add_value(self, value):
        self.list.append(value)


t = MyClass(2)
print(t.value)
t1 = MyClass(3)
print(t1.value)
t.add_value(4)
t.add_value(5)
t1.add_value(6)
t.__dict__['list']=5
print(t.__dict__['list'])
