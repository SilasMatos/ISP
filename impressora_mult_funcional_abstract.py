from abc import abstractmethod
from impressora_basica import ImpressoraBasica
from impressora_digital import ImpressoraDigital


class ImpressoraMultiFuncional(ImpressoraBasica, ImpressoraDigital):
    @abstractmethod
    def enviarEmail(self, documento, destinatario):
        pass

    @abstractmethod
    def copiar(self, documento):
        pass

    @abstractmethod
    def fax(self, documento, destinatario):
        pass