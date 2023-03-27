from abc import ABC, abstractmethod

class ImpressoraBasica(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass