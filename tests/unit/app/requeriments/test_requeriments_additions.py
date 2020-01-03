import unittest
from app.requiriments.requirement_additions import RequirementsAdditions

class TestRequirementsAdditions(unittest.TestCase):
    def test_characters_passwd_deve_retornar_numero_de_letras(self):
        passwd = '123jonas'

        additions = RequirementsAdditions(passwd)

        self.assertEqual(additions.characteres_passwd(), 8)

    def test_uppercases_deve_retornar_numero_de_letras_maiusculas(self):
        passwd = '123JoNaS'

        additions = RequirementsAdditions(passwd)

        self.assertEqual(additions.uppercases(), 3)

    def test_lowercase_deve_retornar_numero_de_letras_minusculas(self):
        passwd = '123JoNas'

        additions = RequirementsAdditions(passwd)

        self.assertEqual(additions.lowercases(), 3)

    def test_numbers_deve_retornar_quantidade_de_numeros(self):
        passwd = '123Jonas34'

        additions = RequirementsAdditions(passwd)

        assert additions.numbers() == 5

    def test_symbols_deve_retornar_numero_de_symbolos(self):
        passwd = '123-Jo#nas/'

        additions = RequirementsAdditions(passwd)

        assert additions.symbols() == 3

    def test_middle_numbers_or_symbols_deve_retornar_quantidade_de_numbers_or_symbols_estao_entre_characters(self):
        passwd = '1faev/fdw3a'

        additions = RequirementsAdditions(passwd)

        assert additions.middle_numbers_or_symbols() == 2

    def test_requirements_return_numeros_de_requerimentos_atingidos(self):
        passwd = '/jonas1Antunes'

        additions = RequirementsAdditions(passwd)

        assert additions.requirements() == 5
