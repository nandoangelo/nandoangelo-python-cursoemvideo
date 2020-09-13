# DESAFIO 001 
# Crie um script Python que leia o nome de uma pessoa e mostre 
# uma mensagem de boas vindas de acordo com o valor digitado.
#
# -------------------------------------- Mundo I / Aula 04 ----

nome = input('Qual o seu nome? ')
print('Olá,\033[34m', nome, '\033[m!\nSeja bem-vindo ao mundo do Python.')

'''
 Repare que estamos usando virgulas para unir a saida e
 os códigos de cores aprendidos na Aula 11. 
 No caso, o nome da pessoa será exibido em azul.
 
'''