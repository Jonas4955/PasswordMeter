import re
from app.requiriments.requirement_additions import Requirements


class Regras(Requirements):
    def __init__(self, senha):
        self.__pass = senha
        super().__init__(self.__pass)

    def senha(self):
        return self.__pass

    def test_password(self):
        minimal_number = 1
        minimal_upper_char = 2
        minimal_lower_char = 2
        minimal_special_char = 1
        minimal_len_char = 8
        password = self.__pass
        if len(password or ()) < minimal_len_char:
            raise Exception('Senha tem que ter no mínimo '+str(minimal_len_char)+' caracteres')
        if len(re.findall(r"[A-Z]", password)) < minimal_upper_char:
            raise Exception('Senha tem que ter no mínimo '+str(minimal_upper_char)+' letras maiusculas')
        if len(re.findall(r"[a-z]", password)) < minimal_lower_char:
            raise Exception('Senha tem que ter no mínimo '+str(minimal_lower_char)+' letras minusculas')
        if len(re.findall(r"[0-9]", password)) < minimal_number:
            raise Exception('Senha tem que ter no mínimo '+str(minimal_number)+' numeros')
        if len(re.findall(r"[~`!@#$%^&*()_+=-{};:'><]", password)) < minimal_special_char:
            raise Exception('Senha tem que ter no mínimo '+str(minimal_special_char)+' caracteres especiais')


regra = Regras('XxtochaxX123')
print(regra.senha())
print(regra.test_password())
