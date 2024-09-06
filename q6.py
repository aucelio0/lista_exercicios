#  Crie um programa que possua uma lista com números de 1 a 20, e informe quais deles são primos.

# função para saber se o número é primo
def numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Lista com números de 1 a 20
numeros = list(range(1, 21))

# Lista para armazenar números primos
primos = []

# Verifica quais números na lista são primos
for numero in numeros:
    if numero_primo(numero):
        primos.append(numero)
        
# Exibe os números primos
print("Números primos de 1 a 20:")
print(primos)