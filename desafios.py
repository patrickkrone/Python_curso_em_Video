# import math
#
# import pydub
#
# nome = input('qual seu nome?')
# print('olá!', nome, 'prazer em conhecer!')
#
# dia = input('dia = ')
# mes = input('Mês = ')
# ano = input('Ano = ')
# print('Você nasceu no dia ', dia, ' de ', mes, ' de ', ano, 'correto?!')
#
# prim = input('1º nº = ')
# seg = input('2º nº = ')
# numbers = [prim, seg]
# print('a soma é!', prim + seg)
#
# #desafio 03
# #crie programa que leia dois numeros e mostre a soma entre eles
# n1 = float (input('digite um número real: '))
# n2 = float (input('digite outro número real: '))
# soma = n1 + n2
# print(f'Então a soma de {n1} + {n2}, é igual= {soma}')
#
# #desafio 04
# #crie programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# #informações possiveis sobre ele
# dado = input('Digite algum dado para ser analisado')
# print('o tipo primitivo é: ', type(dado))
# print('este dado é numérico? ', dado.isnumeric())
# print('este dado é maiúsculo? ', dado.isupper())
# print('este dado é minusculo? ', dado.islower())
# print('este dado é somente espaços? ', dado.isspace())
# print('este dado é alfabético? ', dado.isalpha())
# print('este dado é alfanumerico? ', dado.isalnum())
# print('este dado esta capitalizada? ', dado.istitle())
#
# #desafio 05
# #crie programa que leia um numero inteiro e mostra na tela o seu sucessor e o seu antecessor
# n1 = int (input("Digite um numero inteiro: "))
# print('Você digitou o n°: {:_^10}'.format(n1),'\nSeu antecessor é o nº: {}'.format(n1-1), '\nSeu sucessor é o n°: {}'.format(n1+1))
#
# #desafio 06
# #crie programa que leia um numero com seu dobro, triplo e raiz quadrada
# n1 = int (input('Digite um número'))
# print('Você digitou o nº: {}'.format(n1),'\n O dobro: {}'.format(n1*2),'\n O triplo: {}'.format(n1*3),'\n A raiz quadrada: {}'.format(n1**(1/2)))
#
# #desafio 07
# # Ler duas notas de um aluno e calcular a sua média
# n1 = float (input("nota 1: "))
# n2 = float (input("nota 2: "))
# soma = n1 + n2
# print('Média do aluno é: {}'.format((n1+n2)/2))
#
# #desafio 08
# # Leia um valor em metros e o exiba convertido em centimetros e milimetros
# n = float (input('digite um valor em metros: '))
# print('Convertido em cm: {}'.format(n*100),'\n Convertido em mm: {}'.format(n*1000))
#
# #desafio 09
# # Leia um valor inteiro e mostre sua tabuada
# n = int (input('Descubra a tabuada do nº: '))
# print('{} x {:2} = {}'.format(n,1,n*1))
# print('{} x {:2} = {}'.format(n,2,n*2))
# print('{} x {:2} = {}'.format(n,3,n*3))
# print('{} x {:2} = {}'.format(n,4,n*4))
# print('{} x {} = {}'.format(n,5,n*5))
# print('{} x {} = {}'.format(n,6,n*6))
# print('{} x {} = {}'.format(n,7,n*7))
# print('{} x {} = {}'.format(n,8,n*8))
# print('{} x {} = {}'.format(n,9,n*9))
# print('{} x {} = {}'.format(n,10,n*10))
#
# #desafio 10
# # converta quantos dólares a pessoa pode comprar
# r = float (input('Quantos R$: '))
# print('Você pode comprar até U${:.2f}'.format(r/3.27))
#
# #desafio 11
# # faça programa que leia largura e altura de uma parede em METROS, calcule a sua área e a quantidade de tinta necessária para pintá-la
# #sabendo que cada litro de tinta pinta área de 2m²
# l = float(input('Digite a largura em metros: '))
# a = float(input('Digite a altura em metros: '))
# area = l * a
# tinta = area / 2
# print('Área total sendo {:.2f} m²'.format(area),'\nNecessário {} Litros de tinta'.format(tinta))
#
# #desafio 12
# # faça programa que leia o preço de um produto e aplique 5% de desconto
# p = float (input('Digite o preço do produto (R$): '))
# print('Valor promocional com 5% de desconto: R$ {} !'.format(p-(p*0.05)))
#
# #Desafio 13
# #faça um programa que leia o salário e aplique 15% de aumento
# sal = float (input('Digite seu salário atual.'))
# sal= sal+(sal*0.15)
# print('Seu salário com 15% de aumento será: R${:.2f}!!!!'.format(sal))
#
# #Desafio 14
# #faça um programa que converta a temperatura digita em ºC e para Fº
# t = float (input('Digite a temperatura em ºC: '))
# f= (t * 9/5) + 32
# print(f'Então [{t}ºC] equivale à [{f}ºF]')
#
# #Desafio 15
# #Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
# #quais ele foi alugado; Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado
# km = float (input('Quantos KM você rodou? '))
# dias = int (input('Por quantos dias você alugou?'))
# preço = km * 0.15 + dias * 60
# print(f'Valores: \nR$ 0,15 x {km} = {km*0.15:.2f}\nR$ 60 x {dias} = {dias*60:.2f}')
# print(f'Total a pagar: R$ {preço}')
#
# ##Desafio 16
# # Crie um programa que leia um numero REAL qualquer pelo teclado e mostre na tela a sua porção INTEIRA
# # ex: numero: 6.148 o numero tem a parte inteira 6.
# import math
# real = float    (input('digite um número REAL: '))
# real = math.trunc(real)
# print(f'A parte inteira do seu numero é {real:.^5}')
#
# # Desafio 17
# # Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# # um triangulo retangulo, CALCULE e mostre o comprimento da hipotenusa
# catetoop = float (input('digite o cateto oposto: '))
# catetoad = float (input('digite o cateto adjacente: '))
# hipotenusa = math.hypot(catetoop, catetoad)
# print('-'*10,f'\nA hipotenusa dos catetos {catetoad} e {catetoop} é {hipotenusa:.2f}')
#
# # Desafio 18
# # Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# angulo = int (input('Qual ângulo em º: '))
# radiano = math.radians(angulo)
# seno = math.sin(radiano)
# cosseno = math.cos(radiano)
# tangente = math.tan(radiano)
# print('-'*10,f'\nMEDIDAS DE ÂNGULO {angulo}º    '
#              f' \nSENO {seno:>20.2f}'
#              f'\nCOSSENO {cosseno:>20.2f}  '
#              f' \nTANGENTE {tangente:>20.2f}\n','-'*10 )
# # Desafio 19
# # Fazer com que digite nome de 4 alunos e o sistema aleatoriamente escolha um para limpar o quadro
# import random
# import emoji
# a1 = input('Digite o nome do primeiro aluno: ')
# a2 = input('Digite o nome do segundo aluno: ')
# a3 = input('Digite o nome do terceiro aluno: ')
# a4 = input('Digite o nome do quarto aluno: ')
# resultado = random.choices([a1,a2,a3,a4])
# print(emoji.emojize('Quem deverá apagar o quadro será!!!!!! \n'),emoji.emojize(":fire:"*10 , language='en'))
# print(f'{resultado}')
#
# # Desafio 20
# # Um professor quer sortear a ordem de apresentação dos alunos
# # Leia 4 nomes e mostre a ordem sorteada
# import  random
# a1 = input('Digite o nome do primeiro aluno: ')
# a2 = input('Digite o nome do segundo aluno: ')
# a3 = input('Digite o nome do terceiro aluno: ')
# a4 = input('Digite o nome do quarto aluno: ')
# num = [a1,a2,a3,a4]
# random.shuffle(num)
# print('=LISTA DE APRESENTAÇÕES=')
# print(f' {num}')
#
#
# #Desafio 21
# # Faça um programa em Python que abra e reproduza o audio de um arquivo mp3
# import os
# os.startfile("Taylor Swift - The Great War.mp3")
#
# #Desafio 22
# # Crie um programa que leia o nome completo de uma pessoa e mostre:
# # - O nome com todas as letras maiúsculas.
# # - O nome com todas as letras minúsculas.
# # - Quantas letras ao to do (sem considerar espaços).
# # - Quantas letras tem o primeiro nome.
# nome = input('Digite o nome completo')
# print(nome.upper())
# print(nome.lower())
# print(len(nome.replace(' ','')))
# print(len(nome.split()[0]))
#
# # 💡 DESAFIO 023
# # Faça um programa que leia um número de 0 a 9999
# # e mostre na tela cada um dos dígitos separados.
# # Exemplo: # Digite um número: 1834 # unidade: 4 # dezena: 3# centena: 8# milhar: 1
# n =(input('Digite nº de 0 a 9999'))
# print(f'unidade:{n[3]}\ndezena:{n[2]}\ncentena:{n[1]}\nmilhar:{n[0]}')
#
# # 💡 DESAFIO 024
# # Crie um programa que leia o nome de uma cidade
# # e diga se ela começa ou não com o nome "SANTO".
# cid = input('digite nome da cidade')
# cid = cid.split()[0] ##pega a primeira palavra do nome
# print('Começa com a palavra SANTO essa cidade?: ','SANTO' in cid.upper())
#
# # 💡 DESAFIO 025
# # Crie um programa que leia o nome de uma pessoa
# # e diga se ela tem "SILVA" no nome.
# pessoa = input('digite nome da pessoa')
# print('Existe a palavra SILVA nesse nome?: ','SILVA' in cid.upper())
#
# # 💡 DESAFIO 026
# # Faça um programa que leia uma frase pelo teclado e mostre:
# # ▶ Quantas vezes aparece a letra "A".
# # ▶ Em que posição ela aparece a primeira vez.
# # ▶ Em que posição ela aparece a última vez.
# frase = input('digite uma frase')
# frase = frase.lower() #'''transforma tudo em minusculo para ser certeiro na contagem'''
# vezes = ( frase.count('a'))
# pos1 = frase.find('a')
# ultimo = frase.rfind('a')
# print('A quantidade de A"s: ', vezes )
# print('Primeira aparição: ', pos1)
# print('Última aparição: ', ultimo)
#
# # 💡 DESAFIO 027
# # Faça um programa que leia o nome completo de uma pessoa,
# # mostrando em seguida o primeiro e o último nome separadamente.
# # Exemplo:# Digite um nome: Ana Maria de Souza# primeiro = Ana # último = Souza
# nome = input('digite seu nome completo por favor:')
# primeiro = nome.split()[0]
# ultimo = nome.split()[-1]
# print(nome.split())
# print('1ª: ',primeiro )
# print(f'último:  {ultimo}' )
#
# 💡 DESAFIO 028
# Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# import random
# pensei = random.randrange(0, 5)
# digitei = int(input('Digite um numero de 0 à 5: '))
# if digitei == pensei:
#     print('PARABÉNS AKINATOR!')
# else:
#     print(f'Errou, era o nº: {pensei}!')
import random
import time
from datetime import date

# 💡 DESAFIO 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite
# velocidade = int(input('Qual a velocidade do carro?(km)'))
# if velocidade > 80:
#     multa = (velocidade -80) * 7
#     print(f'Terá que pagar uma multa a cada km acima do limite. \n(R$ 7,00/km) x {velocidade-80}'
#           f'\n-----TOTAL:  R$ {multa}')
# else:
#     print('PARABÉNS, DENTRO DA LEI!')

# 💡 DESAFIO 030
# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.
# num = int(input('digite um numero: '))
# if num % 2 == 0:
#     print('número par')
# else:
#     print('numero ímpar')

# DESAFIO 031
# 💡 Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
# distancia = float(input('Qual é a distância da sua viagem em Km? '))
# # Verifica o valor por km de acordo com a distância
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
# # Mostra o valor da passagem formatado com duas casas decimais
# print(f'O preço da sua passagem será de R${preco:.2f}')

# DESAFIO 032
# 💡 Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# Programa para verificar se um ano é bissexto
# ano = int(input('Digite um ano: '))
# # Regra para ano bissexto:
# # 1. Deve ser divisível por 4
# # 2. Não pode ser divisível por 100, a menos que também seja divisível por 400
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print(f'O ano {ano} é BISSEXTO!')
# else:
#     print(f'O ano {ano} NÃO é bissexto.')

# DESAFIO 033
# 💡 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# n1 = int(input('digite 1ª numero: '))
# n2 = int(input('digite 2ª numero: '))
# n3 = int(input('digite 3ª numero: '))
# if n1 > n2 and n1 > n3:
#     maior = n1
# if n1 < n2 and n1 < n3:
#     menor = n1
# if n2 > n3 and n2 > n1:
#     maior = n2
# if n2 < n3 and n2 < n1:
#     menor = n2
# if n3 > n1 and n3 > n2:
#     maior = n3
# if n3 < n1 and n3 < n2:
#     menor = n3
# print('O menor é: {:>10}'.format(menor))
# print('O maior é: {:>10}'.format(maior))

# DESAFIO 034
# 💡 Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# sal = float(input('Qual o seu salário?'))
# if sal <= 1250:
#     promo = sal +(sal * 0.15)
#     print('AUMENTO DE 15%')
# else:
#     promo= sal+ (sal * 0.10)
#     print('AUMENTO DE 10%')
# print("="*10,f'\nPARABÉNS PELA PROMOÇÃO!!!\nSeu novo salário será: \nDe: R${sal:>10}\nPara: R${promo:>10.2f}!!!')
# print("="*10)

# DESAFIO 035
# 💡 Escreva um programa que leia o comprimento de tres retas e diga se elas podem ou não formar um triangulo
# print('====Descobrindo se os valores formam triângulo====')
# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# c = int(input('Digite o terceiro valor: '))
# if a + b > c and b + c > a and a + c > b:
#       print("É POSSÍVEL CRIAR O TRIÂNGULO!!!")
# else:
#     print('NÃO SERÁ POSSÍVEL. \nA SOMA DE DOIS LADOS NÃO É SUFICIENTE')

#---------- mundo 2----------------
# DESAFIO 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.
# import time
# print("| - |"*5,'BANCO EMPRÉSTIMO',"| - |"*5)
# valor = float(input('Qual valor da casa R$: '))
# salario = float(input("Qual seu salário atual R$: "))
# anos = int(input("Quantos anos de financiamento: "))
# print('\033[30;4;41m --CONSULTANDO...--\033[0;1;m')
# time.sleep(2)
# if (valor/ (anos * 12)) < salario * 0.30:
#     print(f'Notícia boa!! \nEmpréstimo aprovado com parcelas de: R${valor/(anos * 12):.2f}')
# else:
#     print("ops!! empréstimo não disponível. \nParcela maior que 30% do seu salário.\n"
#           f"R$:{valor/ (anos * 12):.2f} \nR$:{salario*0.30:.2f}")
# print("| - |"*5,'BANCO EMPRÉSTIMO',"| - |"*5)

# DESAFIO 037
# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
# num =  int(input('Digite um numero inteiro:  '))
# escolha = int(input("Qual a base de conversão:\n1 - Para BINÁRIO;\n2 - Para OCTAL;\n3 - Para HEXADECIMAL \nOPÇÃO: "))
# if escolha == 1:
#     print(f'Em BINÁRIO SERIA: {bin(num)[2:]}') # O [2:] remove o prefixo (0b, 0o, 0x)
# elif escolha == 2:
#     print(f'Em OCTAL SERIA: {oct(num)[2:]}') # O [2:] remove o prefixo (0b, 0o, 0x)
# elif escolha == 3:
#     print(f'Em HEXADECIMAL SERIA: {hex(num)[2:]}')
# else:
#     print("Opção inválida")

# DESAFIO 038
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
#- Não existe valor maior, os dois são iguais
# n1 = int(input("Digite um número inteiro: "))
# n2 = int(input("Digite outro número inteiro: "))
# if n1 > n2:
#     print(f"O primeiro valor é o maior")
# elif n1 < n2:
#     print(f"O segundo valor é o maior")
# else:
#     print("não existe valor maior, ambos são iguais")

# DESAFIO 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
import datetime
# print("ALISTAMENTO MILITAR - ELEGIBILIDADE")
# ano = int(input("Ano de nascimento do jovem:"))
# idade = date.today().year - ano
# if 18 > idade :
#     print("Poderá ainda se alistar futuramente.")
#     print(f"Faltam {18-idade} anos.")
# elif idade == 18:
#     print("Deve se alistar imediatamente!")
# elif idade > 18:
#     print("Passou do tempo de alistamento.")
#     print(f'Passaram {idade-18} anos depois do prazo.')

# DESAFIO 040
# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# media = (nota1+nota2)/2
# print('sua média final foi de: {}'.format(media))
#
# if media >= 7:
#     print("Aprovado")
# elif 5 <= media < 7:
#     print("Em recuperação")
# elif media < 5:
#     print("Reprovado")

# DESAFIO 041
# A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER
# print("-|"*10)
# print("Confederação Nacional de Natação")
# print("-|"*10)
# nasc = int(input("Digite o ano de nascimento: "))
# idade = date.today().year - nasc
# print(f"O tipo de competidor com idade de {idade} será: ")
# if idade <= 9:
#     print("MIRIM")
# elif idade <= 14:
#     print("INFANTIL")
# elif idade <= 19:
#     print("JUNIOR")
# elif idade <= 20:
#     print("SENIOR")
# else:
#     print("MASTER")
# print("-|"*10)

# DESAFIO 042
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
# print('====Descobrindo se os valores formam triângulo====')
# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# c = int(input('Digite o terceiro valor: '))
# if a + b > c and b + c > a and a + c > b:
#     print("É POSSÍVEL CRIAR O TRIÂNGULO!!!")
#     print('seu tipo é.......')
#     time.sleep(1),print(','*20)
#     if a==b and b==c:
#         print('é um Equilátero!')
#     elif a==b or a==c or b==c:
#         print('é um Isósceles')
#     elif a!=b!=c:
#         print('é um Escaleno')
# else:
#     print('NÃO SERÁ POSSÍVEL. \nA SOMA DE DOIS LADOS NÃO É SUFICIENTE')

# DESAFIO 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# # - Acima de 40: Obesidade mórbida
# peso = float(input("Digite o peso: "))
# altura = float(input("Digite a altura: "))
# imc = peso / (altura ** 2)
# print('STATUS CORPORAL')
# print(f'IMC: {imc:.2f}')
# if imc < 18.5:
#     print('Você está abaixo do peso')
# elif 18.5 <= imc <= 25:
#     print('Você está num peso ideal')
# elif imc >= 25 and imc <= 30:
#     print('Você está sobrepeso')
# elif 40>= imc >= 30:
#     print('Você está OBESO')
# elif imc >40:
#     print('Você vai morrer de obesidade mórbida!')

# DESAFIO 044
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto    - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal        - 3x ou mais no cartão: 20% de juros
# produto = float(input("Digite o valor do produto: R$ "))
# print("""1 - À vista dinheiro/cheque: 10% de desconto    \n2 - À vista no cartão: 5% de desconto
# 3 - Em até 2x no cartão: preço normal        \n4 - 3x ou mais no cartão: 20% de juros""")
# forma = int(input("Digite a forma de pagamento: "))
# print('=|'*20)
# if forma == 1:
#     print(f"Pagamento em dinheiro/cheque - TOTAL: R${produto*0.90:.2f}")
# elif forma == 2:
#     print(f" À vista no cartão - TOTAL: R${produto*0.95:.2f}")
# elif forma == 3:
#     print(f"Em até 2x no cartão - TOTAL: R${produto:.2f} \n[2 Parcelas de: {produto/2:.2f}]")
# elif forma == 4:
#     print(f"3x ou mais no cartão - TOTAL: R${produto*1.20:.2f} \n[3 Parcelas de: {produto*1.20/3:.2f}]")

# DESAFIO 045
#Criei um jogo de JOKENPÔ contra o CPU
# import emoji
# import random
# print("=="*10)
# print(" "*1,"{JOGO DO JOKENPÔ}")
# print("=="*10)
# print(emoji.emojize("|| pedra :moai: || papel :page_facing_up: || tesoura :scissors:", language='en'))
#
# jogador = input("Digite a opção (pedra, papel ou tesoura): ").strip().lower()
#
# pedra = emoji.emojize(":moai:",language='en')
# tesoura = emoji.emojize(":scissors:",language='en')
# papel = emoji.emojize(":page_facing_up:",language='en')
# cpu = random.choice([pedra,tesoura,papel])
# if jogador == 'pedra':
#     jogador = pedra
# elif jogador == 'papel':
#     jogador = papel
# elif jogador == 'tesoura':
#     jogador = tesoura
# print("=="*10)
# time.sleep(1),print(f'Você jogou: {jogador}')
# time.sleep(1),print(f'CPU jogou: {cpu}')
# time.sleep(2),print("~"*10)
# if jogador == cpu:
#     print(f"CPU:{cpu} x {jogador} = EMPATE!")
# elif jogador == pedra and cpu == tesoura or jogador == tesoura and cpu == papel or jogador == papel and cpu == pedra:
#     print(f"VOCÊ GANHOU! 🎉")
# else:
#     print(f" VOCÊ PERDEU 😭!")

# DESAFIO 046
# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
# for c in range(10,0,-1):
#     time.sleep(1)
#     print(c)
# print("FELIZ ANO NOVO!!!!!!!!!")

# DESAFIO 047
# Crie um programa que mostre na tela todos os números pares
# # que estão no intervalo entre 1 e 50.
# for x in range(0,52,2):
#     print(x,end="-")

# DESAFIO 048
# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
import math
from xml.dom.minidom import ProcessingInstruction

from django.template.defaultfilters import upper

# soma = 0
# impar = 9 % 2
# for x in range(1,500):
#     if x % 2 == 1 and x % 3 == 0:
#         soma = soma + x
#         print(x,' - ', soma, )
#     # print(x ,end='  ')
# print("total:", soma)

# DESAFIO 049
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.
# n = int (input('Descubra a tabuada do nº: '))
# for c in range(1,11):
#     print('{} x {:2} = {}'.format(n,c,n*c))


# DESAFIO 050
# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
# soma = 0
# print("Digite 6 Números inteiros")
# print("-"*4)
# for c in range(1,7):
#     num = int(input(f"{c}º número: "))
#     if num % 2 == 0:
#         soma = soma+num
# print(f"A soma dos números pares é: {soma}")

# DESAFIO 051
# Desenvolva um programa que leia:
# 1. O primeiro termo de uma Progressão Aritmética (PA).
# 2. A razão dessa PA.
# No final, o programa deve mostrar:
# * Os 10 primeiros termos dessa progressão.
# print("="*40)
# print(" "*5,"10 TERMOS DE UMA PROGRESSÃO ARITMETICA"," "*5)
# print("="*40)
# termo = int(input("Primeiro termo: "))
# razao = int(input("Razão: "))
# pa = termo + razao * (10 -1)
# for c in range(termo,pa+razao,razao):
#     #c+=c
#     print(c," -->",end="")
# print("\nACABOUUUUUUUUUUU")

# DESAFIO 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# num = int(input("Digite um numero inteiro: "))
# vezes = 0
# for c in range(1,num+1):
#     print(c,end=" ")
#     if num % c == 0:
#         vezes = vezes + 1
# if vezes <=2 and num >=1:
#     print(f"\nO numero {num} foi divisível {vezes} vezes e por isso é primo!")
# else:
#     print(f"\nO numero {num} foi divisível {vezes} vezes e por isso não é primo!")

# DESAFIO 053
# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de Palíndromos:
# - APOS A SOPA
# - A SACADA DA CASA
# - A TORRE DA DERROTA
# - O LOBO AMA O BOLO
# - ANOTARAM A DATA DA MARATONA
# frase = input("Digite uma frase: ")
# palindromo = frase.replace(" ", "")
# print(f"o inverso de {palindromo} é: {palindromo[30::-1]}")
# if palindromo == palindromo[::-1]:
#     print("é um palindromo")
# else:
#     print("não é um palindromo")

# DESAFIO 054
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre:
# 1. Quantas pessoas ainda não atingiram a maioridade.
# 2. E quantas já são maiores.
# menores =0
# maiores = 0
# for c in range(1,8):
#     nascimento = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
#     idade =  date.today().year - nascimento
#     if idade >=18:
#         maiores = maiores +1
#     else:
#         menores = menores +1
# print(f"Pessoas maiores de idade: {maiores}")
# print(f"Pessoas menores de idade: {menores}")

# DESAFIO 055
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
# pesado=0
# leve=0
# for x in range (1,6):
#     kg  = float(input(f'Peso da {x}ª pessoa: '))
#     if x ==1:
#         leve = kg
#         pesado = kg
#     else:
#         if leve < kg:
#             leve = kg
#         if  pesado >kg:
#             pesado = kg
#
# print(f" O maior peso lido foi de {pesado}Kg.")
# print(f" O menor peso lido foi de {leve}Kg.")
# DESAFIO 056
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# 1. A média da idade do grupo.
# 2. Qual é o nome do homem mais velho.
# 3. Quantas mulheres têm menos de 20 anos.
# velho = 0
# novas = 0
# media = 0
# nomevelho= ''
# for x in range(1,5):
#     print("-"*5,f"{x}ª PESSOA","-"*5)
#     nome = input("Nome: ")
#     idade = int(input("Idade: "))
#     Sexo = str(input("Sexo (M/F): ")).strip().upper()
#     media = idade+media
#     if x == 1 and Sexo == "M":
#         velho = idade
#         nomevelho = nome
#     if Sexo == "F" and idade < 20:
#             novas = novas + 1
#     if Sexo == "M" and idade > velho:
#             velho = idade
#             nomevelho = nome
#
# print(f"Média de idade do grupo é de {media/4:.1f} anos")
# print(f"O homem mais velho se chama {nomevelho} e tem {velho} anos")
# if novas ==0:
#     print("Não há mulheres menores de 20 anos")
# else:
#     print(f"Ao todo são {novas} mulhere(s) com menos de 20 anos")
''' DESAFIO 057
Faça um programa que leia o sexo de uma pessoa,mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

'''
DESAFIO 058
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
'''
'''
DESAFIO 059
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
'''
DESAFIO 060
Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex:
5! = 5 x 4 x 3 x 2 x 1 = 120
'''
'''
DESAFIO 061
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
'''
'''DESAFIO 062
Melhore o DESAFIO 60, perguntando para o usuario se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos'''
'''
DESAFIO 063
Escreva um programa que leia um número n inteiro qualquer e
 mostre na tela os n primeiros elementos de uma sequencia de fibonacci'''
'''
DESAFIO 064
Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, MOSTRE QUANTOS NºS
foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''
'''
DESAFIO 065
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
MOSTRE A MÉDIA ENTRE TODOS os valores e qual foi o maior e o menor. O programa deve perguntar
se ele quer ou não CONTINUAR a digitar valores'''