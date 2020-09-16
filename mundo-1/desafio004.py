# DESAFIO 004
# Faça um programa que receba o que foi digitado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele
# 
# -------------------------------------- Mundo I / Aula 06 ----

algo = input('Digite alguma coisa: ')

print('O tipo é:\033[33m', type(algo), '\033[m')
print('É numérico?\033[33m', algo.isnumeric(), '\033[m')
print('É decimal?\033[33m', algo.isdecimal(), '\033[m')
print('É alfanumérico?\033[33m', algo.isalnum(), '\033[m')
print('É apenas texto?\033[33m', algo.isalpha(), '\033[m')
print('É apenas espaço?\033[33m', algo.isspace(), '\033[m')
print('Está em maiúsculo?\033[33m', algo.isupper(), '\033[m')
print('Está em minúsculas?\033[33m', algo.islower(), '\033[m')
print('Está capitalizado?\033[33m', algo.istitle(), end=' \033[31m... Fim!\n')

'''
 Nosso analisador de Strings não ficou mais bonito 
 com cores?
'''