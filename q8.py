# Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números

import os

notas = []

while True:
    opcao = input('1 para inserir a nota ou 2 para calcular média: ')
    os.system('cls')
    match opcao:
        case '1':
            try:
                nota_nova = float(input('Informe um valor de 0 a 10: ').replace(',', '.'))
                if nota_nova >= 0 and nota_nova <= 10:
                    notas.append(nota_nova)
                    print('Nota inserida com sucesso.')
                else:
                    print('Nota inválida.')
            except Exception as e:
                print(f'Não foi possível inserir nota. {e}')
            finally:
                continue
        case '2':
            break
        case _:
            print('Opção inválida.')

print(f'Média: {(sum(notas)/len(notas)):,.2f}')