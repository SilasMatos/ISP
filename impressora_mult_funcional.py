from impressora_mult_funcional_abstract import ImpressoraMultiFuncional


class ImpressoraMultifuncional(ImpressoraMultiFuncional):
    def imprimir(self, documento):
        print(f"Imprimindo o documento {documento}")

    def digitalizar(self, documento):
        print(f"Digitalizando o documento {documento}")

    def enviarEmail(self, documento, destinatario):
        print(f"Enviando o documento {documento} por e-mail para {destinatario}")

    def copiar(self, documento):
        print(f"Copiando o documento {documento}")

    def fax(self, documento, destinatario):
        print(f"Enviando o documento {documento} por fax para {destinatario}")