from abc import ABC, abstractmethod
from console.domain.Algorithm import Algorithm


class Builder(ABC):
    def __init__(self):
        self.algorithm = None

    def set_algorithm(self, algorithm: Algorithm):
        self.algorithm = algorithm
        return self

    def get_instance(self):
        return self.algorithm.get_instance()

    @abstractmethod
    def build(self):
        pass
