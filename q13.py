# Crie um programa que automatize uma busca na Internet por videoaulas sobre Python no Youtube.

# bibliotecas
import pyautogui as auto
import time

# atrasar os comandos
auto.PAUSE = 0.5

auto.press('win') # abre o menu iniciar
auto.write('chrome') # digita palavra
auto.press('enter') # aperta "enter

auto.write('youtube.com') 
auto.press('enter')

# ir até barra de busca
for i in range(4):
   auto.press('tab')

# buscar aulas de python
auto.write('aulas de python')
auto.press('enter')
   