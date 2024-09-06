# Crie um programa que receba o peso (em gramas) de um bebê recém-nascido, e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.

# usuário informa nome e peso do bebê
nome = input('Informe seu nome: ').capitalize()
peso = float(input('Informe o peso do bebê em g: '))

# verificação do peso
if peso >= 2.500:
    print(f'{nome} seu bebê está bem!!')
else:
    print(f'{nome} seu bebê precisará ficar internado.')

