from validate_docbr import CPF

class Cpf:

    def __init__(self, documento):
        self.documento = str(documento)
        if self.cpf_eh_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def __str__(self):
        return self.format_cpf()


    def format_cpf(self):

        mascara = CPF()     # Devido a bliblioteca importada, não é preciso escrever todo o codigo abaixo.
        return mascara.mask(self.cpf)

        # fatia_um = self.cpf[:3]
        # fatia_dois = self.cpf[3:6]
        # fatia_tres = self.cpf[6:9]
        # fatia_quatro = self.cpf[9:]
        # return(
        #     "{}.{}.{}-{}".format(
        #         fatia_um,
        #         fatia_dois,
        #         fatia_tres,
        #         fatia_quatro
        #     )
        # )


from cpf import CPF