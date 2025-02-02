# Crie um programa com funções para calcular a área de 4 figuras geométricas (quadrado, círculo, triângulo e trapézio).

# biblioteca
import os

quadrado    = lambda l: l**2
circulo     = lambda r: 3.14*r**2
triangulo   = lambda b,h: (b*h)/2
trapezio    = lambda b_menor,b_maior,h: ((b_maior+b_menor)*h)/2

if __name__ == "__main__":
    while True:
        print('1 - Quadrado')
        print('2 - Circulo')
        print('3 - Triângulo')
        print('4 - Trapézio')
        print('5 - Sair')

        opcao = input('Opção desejada: ')

        os.system('cls')

        match opcao:
            case '1':
                try:
                    lado = float(input('Informe o lado do quadrado: ').replace(',', '.'))
                    print(f'Área do quadrado: {quadrado(lado)}.')
                except Exception as e:
                    print('Não foi possível calcular área.')
                finally:
                    continue
            case '2':
                try:
                    raio = float(input('Informe o raio do circulo: ').replace(',', '.'))
                    print(f'Área do circulo: {circulo(raio)}.')
                except Exception as e:
                    print('Não foi possível calcular área.')
                finally:
                    continue
            case '3':
                try:
                    base = float(input('Informe a base do triângulo: ').replace(',', '.'))
                    altura = float(input('Informe a altura do triângulo: ').replace(',', '.'))
                    print(f'Área do trÂngulo: {triangulo(base,altura)}.')
                except Exception as e:
                    print('Não foi possível calcular área.')
                finally:
                    continue
            case '4':
                    try:
                        b_menor = float(input('Informe a base menor do trapézio: ').replace(',', '.'))
                        b_maior = float(input('Informe a base maior do trapézio: ').replace(',', '.'))
                        altura = float(input('Informe a altura do trapézio: ').replace(',', '.'))
                        print(f'Área do trapézio: {trapezio(b_menor,b_maior,altura)}.')
                    except Exception as e:
                        print('Não foi possível calcular área.')
                    finally:
                        continue
            case '5':
                break
            case _:
                print('Opção indisponível.')
                continue