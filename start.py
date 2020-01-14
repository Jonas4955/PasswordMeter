import sys
from app.requiriments.additions.addition import Additions
from app.requiriments.deductions.deduction import Deductions
from app.score.score import Score

sys.path.append('C:/Users/jonas.antunes/Desktop/python/')

print('-'*30, f'\033[1;31mVerificação de senha\033[m', '-'*30)
senha = input('\033[1;33mDigite sua senha: \033[m')

add = Additions(senha)
deduct = Deductions(senha)
score = Score(senha)
print(f'Number of Characters:               \033[1;32m+{score.score_add_number_of_characteres_passwd()}\033[m')
print(f'Uppercase Letters:                  \033[1;32m+{score.score_add_uppercases()}\033[m')
print(f'Lowercase Letter:                   \033[1;32m+{score.score_add_lowercases()}\033[m')
print(f'Numbers:                            \033[1;32m+{score.score_add_numbers()}\033[m')
print(f'Symbols:                            \033[1;32m+{score.score_add_symbols()}\033[m')
print(f'Middle Numbers or Symbols:          \033[1;32m+{score.score_add_middle_numbers_or_symbols()}\033[m')
print(f'Requirements:                       \033[1;32m+{score.score_add_requeriments()}\033[m')
print(f'Letter Only:                        \033[1;31m-{score.score_deduct_letters_only()}\033[m')
print(f'Numbers Only:                       \033[1;31m-{score.score_deduct_numbers_only()}\033[m')
print(f'Consecutive Uppercase Letters:      \033[1;31m-{score.score_deduct_consecutives_uppercases()}\033[m')
print(f'Consecutive Lowercase Letters:      \033[1;31m-{score.score_deduct_consecutives_lowercases()}\033[m')
print(f'Consecutive Numbers:                \033[1;31m-{score.score_deduct_consecutive_numbers()}\033[m')
print(f'Sequential Letters (+3):            \033[1;31m-{score.score_deduct_sequential_letters()}\033[m')
print(f'Sequential Numbers (+3):            \033[1;31m-{score.score_deduct_sequential_numbers()}\033[m')
print(f'Sequential Symbols (+3):            \033[1;31m-{score.score_deduct_sequential_symbols()}\033[m')
print(f'Score:                     \033[1;32m{score.get_score():.0f}%\033[m')
print(f'Complexity:                {score.complexity()}')
