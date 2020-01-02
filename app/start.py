import sys
from app.requiriments.requirement_additions import Requirements
from app.score.score import Score

sys.path.append('C:/Users/jonas.antunes/Desktop/python/')

print('-'*30, f'Verificação de senha', '-'*30)
senha = input('Digite sua senha: ')


passwd = Requirements(senha)
lista = passwd.separar_lista()
print(f'Separa string em lista: {passwd.separar_lista()}')
passw = passwd.characters_passwd()
print(f'Quantidade de Caracteres: {passw}')
print(f'Upercase: {passwd.uppercases(lista, passw)}')
print(f'Lowercase: {passwd.lowercases(lista, passw)}')
print(f'Numbers: {passwd.numbers(lista, passw)}')
print(f'Symbols: {passwd.symbols(lista, passw)}')
score = Score(senha)
print(f'Score por letra {score.score_por_letras():.2f}')
