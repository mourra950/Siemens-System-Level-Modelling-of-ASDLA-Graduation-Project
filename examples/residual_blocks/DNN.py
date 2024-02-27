import abc


class DNN(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse_json(self):
        pass

    @classmethod
    @abc.abstractmethod
    def create_layers(cls):
        pass
