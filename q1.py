# Crie um programa que peça para que o usuário digite um número, em seguida o converta para float, exibindo em tela tanto o número em si quanto seu tipo de dado.

numero = float(input('Informe um número: ').replace(',', '.'))
print(f'Seu número é : {numero}')
print(type(numero))