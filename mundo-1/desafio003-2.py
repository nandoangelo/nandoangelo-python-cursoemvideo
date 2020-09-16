# DESAFIO 003 - 2
# Crie um script Python que leia dois números e TENTE mostrar
# a soma entre eles. CORRIGIDO!
#
# -------------------------------------- Mundo I / Aula 06 ----

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

print('O resultado da soma dos números', num1, 'e', num2,
      'é:\033[36m', num1 + num2)
print('ACERTÔ MISERÁVI!')

'''
 Reparou a solução para o problema? Antes a entrada era
 reconhecida apenas como String. Com a definição do tipo
 primitivo int, tudo foi resolvido.

'''