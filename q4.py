# Crie um programa que o usuário informa um número inteiro positivo, e o programa exibe na tela uma contagem regressiva.

# importação de biblioteca
import time
import os

# usuário informa o numero
numero = int(input('Informe um número inteiro: '))

os.system('cls')

print('Contagem regressiva')

for i in range(numero, -1, -1):
    print(f'{i}...')
    time.sleep(1)
    os.system('cls')

print('BOOOM!')