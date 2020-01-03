import re
import string

class RequirementDeductions:
    def __init__(self, passwd):
        self.__passwd = passwd

    def letters_only(self):
        letter_only = 0
        for i in range(len(self.__passwd)):
            if self.__passwd[i].isalpha():
                letter_only += 1
        if letter_only == len(self.__passwd):
            return letter_only
        else:
            return 0

    def numbers_only(self):
        number_only = 0
        for i in range(len(self.__passwd)):
            if self.__passwd[i].isnumeric():
                number_only += 1
        if number_only == len(self.__passwd):
            return number_only
        else:
            return 0

    def consecutive_uppercase_letters(self):
        consecutive_upper = 0
        for i in range(len(self.__passwd) - 1):
            if self.__passwd[i].isupper() and self.__passwd[i+1].isupper():
                consecutive_upper += 1
        return consecutive_upper

    def consecutive_lower_letters(self):
        consecutive_lower_letter = 0
        for i in range(len(self.__passwd) - 1):
            if self.__passwd[i].islower() and self.__passwd[i+1].islower():
                consecutive_lower_letter += 1
        return consecutive_lower_letter

    def consecutive_numbers(self):
        consecutive_number = 0
        for i in range(len(self.__passwd) - 1):
            if self.__passwd[i].isnumeric() and self.__passwd[i+1].isnumeric():
                consecutive_number += 1
        return consecutive_number

    def sequential_letters(self):
        sequential_letter = 0
        for i in range(len(self.__passwd)-2):
            if (self.__passwd[i] + self.__passwd[i+1] + self.__passwd[i+2]) in string.ascii_letters:
                sequential_letter += 1
        return sequential_letter

    def sequential_numbers(self):
        sequential_number = 0
        list_numbers = [num for num in range(10)]
        for i in range(1, len(self.__passwd)-1):
            for num in list_numbers:
                try:
                    if num == int(self.__passwd[i]):
                        if num-1 == int(self.__passwd[i-1]) and num+1 == int(self.__passwd[i+1]):
                            sequential_number += 1
                except:
                    pass
        return sequential_number

    def sequential_symbols(self):
        sequential_symbol = 0
        list_symbols = [')', '!', '@', '#', '$', '%', '&', '*', '(']
        for i in range(1, len(self.__passwd) - 1):
            for symb in range(1, len(list_symbols) - 1):
                if list_symbols[symb] == self.__passwd[i]:
                    if list_symbols[symb-1] == self.__passwd[i-1] and list_symbols[symb+1] == self.__passwd[i+1]:
                        sequential_symbol += 1
        return sequential_symbol
