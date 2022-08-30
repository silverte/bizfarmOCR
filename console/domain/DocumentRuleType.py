from abc import ABC, abstractmethod
from console.domain.CodeFactory import CodeFactory


class RuleType(ABC):
    @abstractmethod
    def get_values(self):
        pass


class CodeType(RuleType):
    def __init__(self, code_domain):
        self.code_domain = code_domain

    def get_values(self):
        code = CodeFactory.get_instance()
        return code.get(self.code_domain)
