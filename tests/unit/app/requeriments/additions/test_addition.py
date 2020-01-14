import unittest
from unittest.mock import Mock, MagicMock, patch
from app.requiriments.additions.addition import Additions

class TestAdditions(unittest.TestCase):
    def test_characters_passwd_deve_retornar_numero_de_letras(self):
        passwd = '123jonas'

        additions = Additions(passwd)

        self.assertEqual(additions.number_of_charactere_passwd(), 8)

    def test_uppercases_deve_retornar_numero_de_letras_maiusculas(self):
        passwd = '123JoNaS'

        additions = Additions(passwd)

        self.assertEqual(additions.uppercases(), 3)

    def test_lowercase_deve_retornar_numero_de_letras_minusculas(self):
        passwd = '123JoNas'

        additions = Additions(passwd)

        self.assertEqual(additions.lowercases(), 3)

    def test_numbers_deve_retornar_quantidade_de_numeros(self):
        passwd = '123Jonas34'

        additions = Additions(passwd)

        assert additions.numbers() == 5

    def test_symbols_deve_retornar_numero_de_symbolos(self):
        passwd = '123-Jo#nas/'

        additions = Additions(passwd)

        assert additions.symbols() == 3

    def test_middle_numbers_or_symbols_deve_retornar_quantidade_de_numbers_or_symbols_estao_entre_characters(self):
        passwd = '1faev/fdw3a'

        additions = Additions(passwd)

        assert additions.middle_numbers_or_symbols() == 2

    @patch('app.requiriments.additions.addition.Additions.symbols')
    @patch('app.requiriments.additions.addition.Additions.numbers')
    @patch('app.requiriments.additions.addition.Additions.lowercases')
    @patch('app.requiriments.additions.addition.Additions.uppercases')
    def test_requirements_return_numeros_de_requerimentos_atingidos(self, mock_uppercases, mock_lowercases, mock_numbers, mock_symbols):
        mock_passwd = Mock()

        additions = Additions(mock_passwd)
        mock_uppercases.return_value = 1
        mock_lowercases.return_value = 7
        mock_numbers.return_value = 2
        mock_symbols.return_value = 1

        result = additions.requirements()

        self.assertEqual(result, additions.requirements())
        self.assertTrue(mock_uppercases.assert_called_once)
        self.assertTrue(mock_lowercases.assert_called_once)
        self.assertTrue(mock_numbers.assert_called_once)
        self.assertTrue(mock_symbols.assert_called_once)
