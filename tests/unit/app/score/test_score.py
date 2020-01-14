import unittest
from app.score.score import Score
from app.requiriments.deductions.deduction import Deductions
from app.requiriments.additions.addition import Additions


class TestScore(unittest.TestCase):
    # Complexity of password conform score
    def test_complexity_of_password_too_short(self):
        passwd = ''

        Deductions(passwd)
        Additions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;31mToo Short\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_very_weak(self):
        passwd = 'Jo'

        Deductions(passwd)
        Additions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;31mVery Weak\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_weak(self):
        passwd = 'Jo4'

        Deductions(passwd)
        Additions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;33mWeak\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_good(self):
        passwd = 'Jo4/'

        Deductions(passwd)
        Additions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;34mGood\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_strong(self):
        passwd = 'Jo4/An9'

        Deductions(passwd)
        Additions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;32mStrong\033[m'

    # Complexity of password conform score
    def test_complexity_of_password_very_strong(self):
        passwd = 'Jo4/An9T-u'

        Deductions(passwd)
        Additions(passwd)
        score = Score(passwd)

        assert score.complexity() == '\033[1;32mVery Strong\033[m'

    # Soma total de scores
    def test_soma_total_de_scores_positivos_e_negativos(self):
        passwd = 'Jo4/A9nT-u'

        score = Score(passwd)

        assert score.get_score() == 100

    # Quantidade de letras multiplicado por 4
    def test_score_add_numbers_of_characters_passwd(self):
        passwd = 'jonasantunes'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_number_of_characteres_passwd() == 48

    # Quantidade de letras uppercase multiplicado por 2
    def test_score_add_uppercases(self):
        passwd = 'JonasAntunes'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_uppercases() == 20

    def test_score_add_uppercases_return_zero(self):
        passwd = '_______'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_uppercases() == 0

    def test_score_add_lowercases(self):
        passwd = 'jonasANTUNES'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_lowercases() == 14

    def test_score_add_lowercases_return_zero(self):
        passwd = '______'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_lowercases() == 0

    def test_score_add_numbers(self):
        passwd = 'Jonas4956'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_numbers() == 16

    def test_score_add_symbols(self):
        passwd = 'Jonas/antunes@'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_symbols() == 12

    def test_score_add_middle_numbers_or_symbols(self):
        passwd = 'Jonas1Antu/nes'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_middle_numbers_or_symbols() == 4

    def test_score_add_requeriments(self):
        passwd = 'Jonas1Antunes/s'

        Additions(passwd)
        score = Score(passwd)

        assert score.score_add_requeriments() == 10

    def test_score_deduct_letters_only(self):
        passwd = 'jonasantunes'

        Deductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_letters_only() == 12

    def test_score_deduct_numbers_only(self):
        passwd = '143475'

        Deductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_numbers_only() == 6

    def test_score_deduct_consecutives_uppercases(self):
        passwd = 'JonasANtunes'

        Deductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_consecutives_uppercases() == 2

    def test_score_deduction_consecutives_lowercases(self):
        passwd = 'jonasANT234'

        Deductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_consecutives_lowercases() == 8

    def test_score_deduction_consecutive_numbers(self):
        passwd = 'Jonas1Antunes45'

        Deductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_consecutive_numbers() == 2

    def test_score_deduction_sequential_letters(self):
        passwd = 'JonabcAntuneshij'

        Deductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_sequential_letters() == 6

    def test_score_deduction_sequential_numbers(self):
        passwd = 'Jonas123Antunes23678'

        Deductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_sequential_numbers() == 6

    def test_score_deduction_sequential_symbols(self):
        passwd = 'Jonas)!@Antunes$('

        Deductions(passwd)
        score = Score(passwd)

        assert score.score_deduct_sequential_symbols() == 3
