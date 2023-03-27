from abc import ABC, abstractmethod


class ImpressoraDigital(ABC):
    @abstractmethod
    def digitalizar(self, documento):
        pass