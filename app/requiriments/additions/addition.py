class Additions:
    def __init__(self, passwd):
        self.__passwd = passwd

    def number_of_charactere_passwd(self):
        number_of_charactere = len(self.__passwd)
        return number_of_charactere

    def uppercases(self):
        upper = 0
        exceptions = [' ', '_']
        for i in range(len(self.__passwd)):
            if self.__passwd[i].isupper() and self.__passwd[i] not in exceptions:
                upper += 1
        return upper

    def lowercases(self):
        lower = 0
        exceptions = [' ', '_']
        for i in self.__passwd:
            if i.islower() and i not in exceptions:
                lower += 1
        return lower

    def numbers(self):
        number = 0
        for i in range(len(self.__passwd)):
            if self.__passwd[i].isnumeric():
                number += 1
        return number
    
    def symbols(self):
        symbol = 0
        exceptions = [' ', '_']
        for i in range(len(self.__passwd)):
            if not self.__passwd[i].isalnum() and self.__passwd[i] not in exceptions:
                symbol += 1
        return symbol

    def middle_numbers_or_symbols(self):
        middle_num_or_symb = 0
        exceptions = [' ', '_']
        for i in range(len(self.__passwd) - 2):
            if self.__passwd[i+1].isnumeric() or not self.__passwd[i+1].isalnum() and self.__passwd[i+1] not in exceptions:
                if self.__passwd[i+2]:
                    middle_num_or_symb += 1
        return middle_num_or_symb

    def requirements(self):
        require = 0
        lista = [len(self.__passwd), self.uppercases(), self.lowercases(), self.numbers(), self.symbols()]
        for i in lista:
            if i > 0:
                require += 1
        return require
