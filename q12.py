# Crie um programa que traduza qualquer texto em qualquer idioma para o português.

# biblioteca
from deep_translator import GoogleTranslator

# gerar tradução
tradutor = GoogleTranslator(source='auto', target='pt')

while True:
    try:
        texto = input('Texto a ser traduzido: ')
        texto_traduzido = tradutor.translate(texto)
        
        print(f'\nTradução: "{texto_traduzido}".')
        
        repetir = input('Deseja traduzir outro texto?(s/n)').lower()
        
        if repetir == 's':
            continue
        else:
            break
    except:
        print('Não foi possível traduzir.')