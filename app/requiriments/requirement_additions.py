class RequirementsAdditions:
    def __init__(self, passwd):
        self.__passwd = passwd

    def characteres_passwd(self):
        charactere = len(self.__passwd)
        return charactere

    def uppercases(self):
        upper = 0
        for i in range(len(self.__passwd)):
            if self.__passwd[i].isupper():
                upper += 1
        return upper

    def lowercases(self):
        lower = 0
        for i in self.__passwd:
            if i.islower():
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
        for i in range(len(self.__passwd)):
            if not self.__passwd[i].isalnum():
                symbol += 1
        return symbol

    def middle_numbers_or_symbols(self):
        middle_num_or_symb = 0
        for i in range(len(self.__passwd) - 2):
            if self.__passwd[i+1].isnumeric() or not self.__passwd[i+1].isalnum():
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
