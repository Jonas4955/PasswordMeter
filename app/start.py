import sys
from app.requiriments.requirement_additions import RequirementsAdditions
from app.requiriments.requirement_deductions import RequirementDeductions
from app.score.score import Score

sys.path.append('C:/Users/jonas.antunes/Desktop/python/')

print('-'*30, f'Verificação de senha', '-'*30)
senha = input('Digite sua senha: ')


add = RequirementsAdditions(senha)
deduct = RequirementDeductions(senha)
score = Score(senha)
print(f'Number of Characters:          +{score.score_add_characteres_passwd()}')
print(f'Uppercase Letters:             +{score.score_add_uppercases()}')
print(f'Lowercase Letter:              +{score.score_add_lowercases()}')
print(f'Numbers:                       +{score.score_add_numbers()}')
print(f'Symbols:                       +{score.score_add_symbols()}')
print(f'Middle Numbers or Symbols:     +{score.score_add_middle_numbers_or_symbols()}')
print(f'Requirements:                  +{score.score_add_requeriments()}')
print(f'Letter Only:                   +{score.score_deduct_letters_only()}')
print(f'Numbers Only:                  +{score.score_deduct_numbers_only()}')
print(f'Consecutive Uppercase Letters: +{score.score_deduct_consecutives_uppercases()}')
print(f'Consecutive Lowercase Letters: +{score.score_deduct_consecutives_lowercases()}')
print(f'Consecutive Numbers:           +{score.score_deduct_consecutive_numbers()}')
print(f'Sequential Letters (+3):       +{score.score_deduct_sequential_letters()}')
print(f'Sequential Numbers (+3):       +{score.score_deduct_sequential_numbers()}')
print(f'Sequential Symbols (+3):       +{score.score_deduct_sequential_symbols()}')
print(f'Score \033[1;32m                {score.get_score():.0f}%\033[m')
