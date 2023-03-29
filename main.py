from impressora_mult_funcional import ImpressoraMultifuncional
from impressora_simples import ImpressoraSimples


        impressora_simples = ImpressoraSimples()
        impressora_simples.imprimir("documento")

        
        impressora_multifuncional = ImpressoraMultifuncional()
        impressora_multifuncional.imprimir("documento")
        impressora_multifuncional.digitalizar("documento")
        impressora_multifuncional.enviarEmail("documento", "destinatario@example.com")
        impressora_multifuncional.copiar("documento")
        impressora_multifuncional.fax("documento", "fax@example.com")
