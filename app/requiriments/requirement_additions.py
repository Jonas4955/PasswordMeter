class RequirementsAdditions:
    def __init__(self, passwd):
        self.__passwd = passwd

    def separar_lista(self):
        lista_pass = list(self.__passwd)
        return lista_pass

    def characters_passwd(self):
        character = len(self.__passwd)
        return character

    def uppercases(self):
        lista = self.separar_lista()
        characteres = self.characters_passwd()
        upper = 0
        for i in range(characteres):
            if lista[i].isupper():
                upper += 1
        return upper

    def lowercases(self):
        lista = self.separar_lista()
        characteres = self.characters_passwd()
        lower = 0
        for i in range(characteres):
            if lista[i].islower():
                lower += 1
        return lower

    def numbers(self):
        lista = self.separar_lista()
        characteres = self.characters_passwd()
        number = 0
        for i in range(characteres):
            if lista[i].isnumeric():
                number += 1
        return number
    
    def symbols(self):
        lista = self.separar_lista()
        characteres = self.characters_passwd()
        symbol = 0
        for i in range(characteres):
            if lista[i].isalnum() != True:
                symbol += 1
        return symbol

    def middle_numbers_or_symbols(self):
        lista = self.separar_lista()
        characteres = self.characters_passwd()
        middle_num_or_symb = 0
        for i in range(characteres):
            if lista[i].isnumeric() or not lista[i].isalnum():
                pass
        return middle_num_or_symb

    def requirements(self):
        require = 0
        lista = [self.characters_passwd(), self.uppercases(), self.lowercases(), self.numbers(), self.symbols(), self.middle_numbers_or_symbols()]
        for i in lista:
            if i > 0:
                require += 1
        return require

senha = 'Jonas13/'
require = Requirements(senha)
# lista = require.separar_lista()
# characteres = require.characters_passwd()
# uppercase = require.uppercases(lista, characteres)
# lowercase = require.lowercases(lista, characteres)
# numbers = require.numbers(lista, characteres)
# symbols = require.symbols(lista, characteres)
# middle = require.middle_numbers_or_symbols(lista, characteres)
print(require.requirements())
# print(characteres)
