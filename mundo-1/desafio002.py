# DESAFIO 002
# Crie um script Python que leia o dia, o mês e o ano de
# nascimento de uma pessoa e mostre uma mensagem com a data
# formatada.
#
# -------------------------------------- Mundo I / Aula 04 ----
print('Informe a sua data de nascimento:')

dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')

# ESQUEMA DE CORES
cor = {'limpa': '\033[m',
       'amarelo': '\033[33m'}

print('Esta é a sua data de nascimento:\n'
      '{}{}{} de {}{}{} de {}{}{}. Parabéns!!!'
      .format(cor['amarelo'], dia, cor['limpa'],
              cor['amarelo'], mes, cor['limpa'],
              cor['amarelo'], ano, cor['limpa']))
'''
 Agora inserimos, além das variáveis, montamos nosso próprio 
 esquema de cores para colorir as mensagens exibidas no terminal.
 funcionou.
'''