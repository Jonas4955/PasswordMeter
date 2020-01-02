from app.requiriments.requirement_additions import Requirements

class Addition(Requirements):
    def __init__(self, passwd):
        self.__passwd = passwd
        super().__init__(self.__passwd)

    def add_bonus_number_of_caracteres(self):
        bonus = (self.characters_passwd() * 4)
        return bonus

    def add_bonus_uppercases_letters(self):
        bonus = (self.characters_passwd() - self.uppercases()) * 2
        return bonus

    def add_bonus_lowercases_letters(self):
        bonus = (self.characters_passwd() - self.lowercases()) * 2

    def add_bonus_numbers(self):
        bonus = (self.numbers() * 4)
        return bonus

    def add_bonus_symbols(self):
        bonus = (self.symbols() * 6)
        return bonus

    def add_bonus_middle_numbers_or_symbols(self):
        bonus = (self.middle_numbers_or_symbols() * 2)
        return bonus

    def add_bonus_requirements(self):
        bonus = (self.requirements() * 2)
        return bonus


senha = 'Jonas13/'

add = Addition(senha)
print(add.add_bonus_number_of_caracteres())
