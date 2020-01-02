from app.requiriments.requirement_deductions import RequirementDeductions
from app.requiriments.requirement_additions import RequirementsAdditions

class Score:
    def __init__(self, passwd):
        self.__passwd = passwd
        self.__deduction = RequirementDeductions(passwd)
        self.__addition = RequirementsAdditions(passwd)
        self.__score = 0

    def get_score(self):
        add = self.score_add_characteres_passwd() + self.score_add_lowercases() + self.score_add_uppercases() + self.score_add_numbers() + self.score_add_symbols() + self.score_add_middle_numbers_or_symbols() + self.score_add_requeriments()
        deduct = self.score_deduct_consecutive_numbers() + self.score_deduct_consecutives_lowercases() + self.score_deduct_consecutives_uppercases() + self.score_deduct_letters_only() + self.score_deduct_numbers_only() + self.score_deduct_sequential_letters() + self.score_deduct_sequential_numbers() + self.score_deduct_sequential_symbols()
        score = add - deduct
        if score > 100:
            score = 100
        return score

    def score_add_characteres_passwd(self):
        score = self.__addition.characteres_passwd() * 4
        return score

    def score_add_uppercases(self):
        score = (len(self.__passwd) - self.__addition.uppercases()) * 2
        return score

    def score_add_lowercases(self):
        score = (len(self.__passwd) - self.__addition.lowercases()) * 2
        return score

    def score_add_numbers(self):
        score = self.__addition.numbers() * 4
        return score

    def score_add_symbols(self):
        score = self.__addition.symbols() * 6
        return score

    def score_add_middle_numbers_or_symbols(self):
        score = self.__addition.middle_numbers_or_symbols() * 2
        return score

    def score_add_requeriments(self):
        score = 0
        if self.__addition.characteres_passwd() >= 8:
            if self.__addition.requirements() >= 4:
                score = self.__addition.requirements() * 2
        return score

    def score_deduct_letters_only(self):
        score = self.__deduction.letters_only()
        return score

    def score_deduct_numbers_only(self):
        score = self.__deduction.numbers_only()
        return score

    def score_deduct_consecutives_uppercases(self):
        score = self.__deduction.consecutive_uppercase_letters() * 2
        return score

    def score_deduct_consecutives_lowercases(self):
        score = self.__deduction.consecutive_lower_letters() * 2
        return score

    def score_deduct_consecutive_numbers(self):
        score = self.__deduction.consecutive_numbers() * 2
        return score

    def score_deduct_sequential_letters(self):
        score = self.__deduction.sequential_letters() * 3
        return score

    def score_deduct_sequential_numbers(self):
        score = self.__deduction.sequential_numbers() * 3
        return score

    def score_deduct_sequential_symbols(self):
        score = self.__deduction.sequential_symbols() * 3
        return score
