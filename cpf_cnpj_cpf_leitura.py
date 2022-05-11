from validate_docbr import CNPJ

from cpf_cnpj import Documento   # O cpf_cnpj do meio se refere ao nome do arquivo que está a classe.

from cpf import Cpf             # O cpf do meio se refere ao nome do arquivo que está a classe.

# cpf_um = Cpf ("17819510714")


# objeto_cpf = Cpf(cpf)
# print(objeto_cpf)
#
# cpf = CPF()
#
# print (cpf.validate("17819510714"))
#


exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

documento = Documento.cria_documento(exemplo_cpf)
print(documento)
