import re

class RequirementDeductions:
    def __init__(self, passwd):
        self.__passwd = passwd

    def separar_lista(self):
        lista_pass = list(self.__passwd)
        return lista_pass

    def characters_passwd(self):
        character = len(self.__passwd)
        return character

    def letters_only(self):
        letter_only = 0
        lista = self.separar_lista()
        characteres = self.characters_passwd()
        for i in lista:
            if lista[i] in len(re.findall(r"[A-Z]", self.__passwd)) or lista[i] in len(re.findall(r"[a-z]", self.__passwd)):
                letter_only += 1
        if letter_only == characteres:
            return letter_only
        else:
            return 0

    def numbers_only(self):
        number_only = 0
        lista = self.separar_lista()
        characteres = self.characters_passwd()
        for i in lista:
            if lista[i].isnumeric():
                number_only += 1
        if number_only == characteres:
            return number_only
        else:
            return 0

    def repeat_characteres(self):
        pass

    def consecutive_uppercase_letters(self):
        pass
