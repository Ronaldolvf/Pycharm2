
from validate_docbr import CPF, CNPJ     # Esta importando a bliblioteca cpf e cnpj.

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)        # Buscando a classe DocCpf
        elif len(documento) == 14:
            return DocCnpj(documento)       # Buscando a classe DocCnpj
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):              # É usada parta retorna o cpf como string.
        return self.format()

    def valida(self, documento):    # Está confirmando se o cpf é válido de acordo com a blibioteca.
        validador = CPF()
        return validador.validate(documento)

    def format(self):               # É usado para inserir as características no cpf.
      mascara = CPF()
      return mascara.mask(self.cpf)



class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")

    def __str__(self):                # É usada parta retorna o cnpj como string.
        return self.format()

    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)

    def format(self):                 # É usado para inserir as características no cnpj.
        mascara = CNPJ()
        return mascara.mask(self.cnpj)





# class CpfCnpj:
#
#     def __init__(self, documento, tipo_documento):
#         self.tipo_documento = tipo_documento
#         documento = str(documento)
#         if self.tipo_documento == "cpf":
#             if self.cpf_eh_Valido(documento):
#                 self.cpf = documento
#             else:
#                 raise ValueError("CPF inválido!")
#         elif self.tipo_documento == "cnpj":
#             if self.cnpj_eh_Valido(documento):
#                 self.cnpj = documento
#             else:
#                 raise ValueError("CNPJ inválido!")
#         else:
#             raise ValueError("Documento inválido!")
#
#
#     def cpf_eh_Valido(self, cpf):
#         if len(cpf) == 11:
#             validador = CPF()
#             return validador.validate(cpf)
#         else:
#             raise ValueError("Quantidade de dígitos inválida!")
#
#     def format_cpf(self):
#         mascara = CPF()
#         return mascara.mask (self.cpf)
#
#     def format_cnpj(self):
#         mascara = CNPJ()
#         return mascara.mask (self.cnpj)
#
#     def __str__(self):
#         if self.tipo_documento == "cpf":
#             return self.format_cpf()
#         elif self.tipo_documento == "cnpj":
#             return self.format_cnpj()
#
#
#
#     def cnpj_eh_Valido(self, cnpj):
#         if len(cnpj) == 14:
#             validate_cnpj = CNPJ()
#             return validate_cnpj.validate(cnpj)
#         else:
#             raise ValueError("Quantidade de dígitos inválida!")



