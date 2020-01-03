import unittest
from app.requiriments.requirement_deductions import RequirementDeductions

class TestRequerimentsDeductions(unittest.TestCase):
    def test_letters_only_deve_retornar_numero_de_letras_se_todas_forem_letras(self):
        passwd = 'jonasantunes'

        deductions = RequirementDeductions(passwd)

        assert deductions.letters_only() == 12

    def test_letters_only_retorna_zero_se_string_nao_for_toda_em_letras(self):
        passwd = 'jonas1antunes'

        deductions = RequirementDeductions(passwd)

        assert deductions.letters_only() == 0

    def test_numbers_only_retorna_numero_de_caracteres_se_todos_forem_numeros(self):
        passwd = '13343545'

        deductions = RequirementDeductions(passwd)

        assert deductions.numbers_only() == 8

    def test_numbers_only_retorna_zero_se_string_nao_for_toda_em_numbers(self):
        passwd = '12323af'

        deductions = RequirementDeductions(passwd)

        assert deductions.numbers_only() == 0

    def test_consecutive_uppercase_deve_retornar_numero_de_letras_maiusculas_consecutivas(self):
        passwd = 'JonasANt32'

        deductions = RequirementDeductions(passwd)

        assert deductions.consecutive_uppercase_letters() == 1

    def test_consecutive_lowercase_retorna_numero_de_letras_minusculas_consecuticvas(self):
        passwd = 'jonasAnt24'

        deductions = RequirementDeductions(passwd)

        assert deductions.consecutive_lower_letters() == 5

    def test_consecutive_numbers_retorna_vezes_de_numeros_digitados_consecutivamente(self):
        passwd = 'Jonas1a79'

        deductions = RequirementDeductions(passwd)

        assert deductions.consecutive_numbers() == 1

    def test_sequential_letters_retorna_numero_de_sequencias_alfabeticas_agrupadas_por_tres_caracteres(self):
        passwd = 'Jonasabcjgfjkl'

        deductions = RequirementDeductions(passwd)

        assert deductions.sequential_letters() == 2

    def test_sequential_numbers_retorna_numero_de_sequencias_numericas_ate_dez_agrupadas_por_tres(self):
        passwd = 'Jonas123ad12/456'

        deductions = RequirementDeductions(passwd)

        assert deductions.sequential_numbers() == 2

    def test_sequential_symbols_retorna_numero_de_sequencias_de_symbolos_agrupados_por_tres(self):
        passwd = 'Jonas)!@ad$&'

        deductions = RequirementDeductions(passwd)

        assert deductions.sequential_symbols() == 1
