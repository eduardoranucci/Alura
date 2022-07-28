from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def make_document(document):
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError('Incorrect number of digits.')


class DocCpf:

    def __init__(self, document):
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError("Invalid Cpf.")

    def __str__(self):
        return self.format_cpf()

    def cpf_is_valid(self, document):
        if len(document) == 11:
            validator = CPF()
            return validator.validate(document)
        else:
            raise ValueError('A Cpf must have 11 digits.')
    
    def format_cpf(self):
        masker = CPF()
        return masker.mask(self.cpf)


class DocCnpj():

    def __init__(self, document):
        document = str(document)
        if self.cnpj_is_valid(document):
            self.cnpj = document
        else:
            raise ValueError('Invalid Cnpj.')

    def __str__(self):
        return self.format_cnpj()

    def cnpj_is_valid(self, document):
        if len(document) == 14:
            validator = CNPJ()
            return validator.validate(document)
        else:
            raise ValueError('A Cnpj must have 14 digits.')

    def format_cnpj(self):
        masker = CNPJ()
        return masker.mask(self.cnpj)
