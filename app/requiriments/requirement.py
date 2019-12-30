import sys
sys.path.append('C:/Users/jonas.antunes/Desktop/python/')

class Requirements:
    def __init__(self, passwd):
        self.__passwd = passwd

    def separar_lista(self):
        lista_pass = list(self.__passwd)
        return lista_pass

    def characters_passwd(self):
        character = len(self.__passwd)
        return character
        
    def uppercases(self, lista, characters):
        upper = 0
        for i in range(characters):
            if lista[i].isupper():
                upper += 1
        return upper

    def lowercases(self, lista, characters):
        lower = 0
        for i in range(characters):
            if lista[i].islower():
                lower += 1
        return lower

    def numbers(self, lista, characters):
        number = 0
        for i in range(characters):
            if lista[i].isnumeric():
                number += 1
        return number
    
    def symbols(self, lista, characters):
        symbol = 0
        for i in range(characters):
            if lista[i].isalnum() != True:
                symbol += 1
        return symbol
