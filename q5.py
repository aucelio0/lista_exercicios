#  Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.

# lista
nomes = ['Mateus', 'Asaph', 'Felipe', 'Wesley', 'Gustavo', 'Luis', 'Caio', 'Rafael']

# usuario informa o indice
indice = int(input('Digite um número inteiro para obter um nome: '))

# le a lista e seleciona o índice
if 0 <= len(nomes):
    print(f'O nome selecionado é: {nomes[indice]}')
else:
    print('Não possue na lista.')