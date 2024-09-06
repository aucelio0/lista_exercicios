#  Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser) e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.

# lista de nomes
nomes = []

# usuário insere nomes na lista
print("Digite os nomes um por um. Quando terminar, digite 'fim'.")

while True:
    nome = input("Digite um nome: ").capitalize()
    if nome.lower() == 'fim':
        break
    nomes.append(nome)
    
# Ordena a lista de nomes em ordem alfabética
nomes.sort()

# Exibe a lista de nomes em ordem alfabética e o número total de nomes
print("\nLista de nomes em ordem alfabética:")
for nome in nomes:
    print(nome)
    
print(f"\nNúmero total de nomes digitados: {len(nomes)}")