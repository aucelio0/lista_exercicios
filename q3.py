# Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.

# usuário insere o número
numero = int(input('Informe um número inteiro: '))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")