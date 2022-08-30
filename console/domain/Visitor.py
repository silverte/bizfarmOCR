from abc import ABC, abstractmethod


class Visitable(ABC):
    @abstractmethod
    def rule_check(self):
        pass


class Visitor(ABC):
    @abstractmethod
    def check(self, visitable):
        pass
