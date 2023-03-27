from impressora_basica import ImpressoraBasica


class ImpressoraSimples(ImpressoraBasica):
    def imprimir(self, documento):
        print(f"Imprimindo o documento {documento}")
