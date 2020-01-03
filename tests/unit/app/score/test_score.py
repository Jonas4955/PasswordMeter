import unittest
from unittest.mock import Mock, MagicMock
from app.score.score import Score
from app.requiriments.requirement_deductions import RequirementDeductions
from app.requiriments.requirement_additions import RequirementsAdditions


class TestScore(unittest.TestCase):
    # Complexity of password conform score
    def test_complexity_of_password_too_short(self):
        passwd = ''

        RequirementDeductions(passwd)
        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;31mToo Short\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_very_weak(self):
        passwd = 'Jo'

        RequirementDeductions(passwd)
        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;31mVery Weak\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_weak(self):
        passwd = 'Jo4'

        RequirementDeductions(passwd)
        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;33mWeak\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_good(self):
        passwd = 'Jo4/'

        RequirementDeductions(passwd)
        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;34mGood\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_strong(self):
        passwd = 'Jo4/An9'

        RequirementDeductions(passwd)
        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;32mStrong\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_very_strong(self):
        passwd = 'Jo4/An9T-u'

        RequirementDeductions(passwd)
        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;32mVery Strong\033[m'

    # Soma total de scores
    def test_soma_total_de_scores_positivos_e_negativos(self):
        passwd = 'Jo4/A9nT-u'

        score = Score(passwd)

        assert score.get_score() == 100

    # Quantidade de letras multiplicado por 4
    def test_score_add_characters_passwd(self):
        passwd = 'jonasantunes'

        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.score_add_characteres_passwd() == 48

    # Quantidade de letras uppercase multiplicado por 2
    def test_score_add_uppercases(self):
        passwd = 'JonasAntunes'

        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.score_add_uppercases() == 20

    def test_score_add_lowercases(self):
        passwd = 'jonasANTUNES'

        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.score_add_lowercases() == 14

    def test_score_add_numbers(self):
        passwd = 'Jonas4956'

        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.score_add_numbers() == 16

    def test_score_add_symbols(self):
        passwd = 'Jonas/antunes@'

        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.score_add_symbols() == 12

    def test_score_add_middle_numbers_or_symbols(self):
        passwd = 'Jonas1Antu/nes'

        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.score_add_middle_numbers_or_symbols() == 4

    def test_score_add_requeriments(self):
        passwd = 'Jonas1Antunes/s'

        RequirementsAdditions(passwd)
        score = Score(passwd)

        assert score.score_add_requeriments() == 10

    def test_score_deduct_letters_only(self):
        passwd = 'jonasantunes'

        RequirementDeductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_letters_only() == 12

    def test_score_deduct_numbers_only(self):
        passwd = '143475'

        RequirementDeductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_numbers_only() == 6

    def test_score_deduct_consecutives_uppercases(self):
        passwd = 'JonasANtunes'

        RequirementDeductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_consecutives_uppercases() == 2

    def test_score_deduction_consecutives_lowercases(self):
        passwd = 'jonasANT234'

        RequirementDeductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_consecutives_lowercases() == 8

    def test_score_deduction_consecutive_numbers(self):
        passwd = 'Jonas1Antunes45'

        RequirementDeductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_consecutive_numbers() == 2

    def test_score_deduction_sequential_letters(self):
        passwd = 'JonabcAntuneshij'

        RequirementDeductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_sequential_letters() == 6

    def test_score_deduction_sequential_numbers(self):
        passwd = 'Jonas123Antunes23678'

        RequirementDeductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_sequential_numbers() == 6

    def test_score_deduction_sequential_symbols(self):
        passwd = 'Jonas)!@Antunes$('

        RequirementDeductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_sequential_symbols() == 3
