import emoji
# Tentando importar e usar emojis
print(emoji.emojize("Olá mundo :thumbs_up:", language='en'))
print(emoji.emojize("Python é :snake: e :fire:", language='en'))




# somando numeros e que nao saiam como texxto
n1 = int( input('digite um número')) #convert tudo em inteiro
n2 = int( input('digite outro número')) #convert tudo em inteiro
s = n1 + n2
print('A soma vale {}'.format(s))
print(f'A soma entre {n1} e {n2} vale: {s}') #concatenando

n = input('digite algo: ')
print(n.isupper())  #vai retornar se esta tudo minusculo. existem varios testes de variaveis

#operadores aritméticos
# + adição ; - subtração ; * mumltiplicação; / Divisão; ** Potencia; // Divisão inteira; % Resto da divisão
# == Usado para Resultado (igual à)
#:Ordem de precedencia:
# 1º ( ) 2º ** 3º * / // % 4º + -
3*5+4**2
3*(5+4)**2
#pode usar funcoes para o print EX:
print('oi'*5), print('='*20+ 'olá')
nome = input('digite seu nome')
print('Prazer em te conhecer {:11}!!'.format(nome)) #aqui vai escrever o nome dentro de ate 11 caracteres
#pode-se usar dentro do {:^11} (centraliza o nome)/ {:>11} (direita o nome) ou {:=^11} (insere o = no nome)
n1 = int (input('digite um valor: '))
n2 = int (input('digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {},\n o produto é {},\n e a divisão é: {:.3f}'.format(s, m, d), end=' x ')
print('Divisão inteira: {} e potência {}'.format(di, e))
# # \n insere uma quebra de linha (enter)
# digitar no final end=' ' faz com que o final do print nao quebre linha e continue na mesma.
#
# CTRL + / eu consigo comentar tudo selecionado de uma vez
# usar \ ou [] ou ( ) pode quebrar linhas e eu continuar o codigo
#

#---- aula de condicional----
tempo = int(input('quantos anos tem seu carro?'))
if tempo <= 3:  # esse aqui é o bloco se for True
    print('carro novo')
else:                  # # esse aqui é o bloco se for False
    print('carro velhuxo')
print(('--FIM--'))

import time #para aparecer um temporizador legal
time.sleep(2)
print('--FIM--')
time.sleep(2)

#---------- mundo 2----------------
# estrutura de repetição FOR:
# pode criar laços infinitos com contadores pré-definidos;
# for variavel in range(1,10): #10 sequencias de passos e pulos até pegar a maçã
#     passo
#     pula
# passo
# pega
# for c in range(1,6):
#     print('hui')
# print("FIM")
# for c in range(1,9,3): #pula de tres em tres comecando no 1 ate 9
#     print(c)
#-------------------- #usanddo for para somar valores digitados
# s = 0
# for c in range(0,4):
#     n = int(input('digite um numero: '))
#     s = s + n
# print('a soma vale {}'.format(s))
#---------------------- Aula de WHILE
# while not apple:
#     print('--caminhando--')
# pegar maçã