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
print(f'add: {score.score_add_characteres_passwd()}')
print(f'add: {score.score_add_uppercases()}')
print(f'add: {score.score_add_lowercases()}')
print(f'add: {score.score_add_numbers()}')
print(f'add: {score.score_add_symbols()}')
print(f'add: {score.score_add_middle_numbers_or_symbols()}')
print(f'add: {score.score_add_requeriments()}')
print(f'deduct: {score.score_deduct_letters_only()}')
print(f'deduct: {score.score_deduct_numbers_only()}')
print(f'deduct: {score.score_deduct_consecutives_uppercases()}')
print(f'deduct: {score.score_deduct_consecutives_lowercases()}')
print(f'deduct: {score.score_deduct_consecutive_numbers()}')
print(f'deduct: {score.score_deduct_sequential_letters()}')
print(f'deduct: {score.score_deduct_sequential_numbers()}')
print(f'deduct: {score.score_deduct_sequential_symbols()}')
print(f'Score \033[1;32m{score.get_score():.0f}%\033[m')
