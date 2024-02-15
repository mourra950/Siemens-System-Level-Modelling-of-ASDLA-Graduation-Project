import abc


class DNN(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse_json(self):
        pass
