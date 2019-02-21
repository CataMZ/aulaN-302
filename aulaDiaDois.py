# Exercicio 1
# - crie uma função que receba uma lista de 20 valores aleatórios, retornar apenas o maior valor e printar em tela.

# Resolucao:

# import random as r

# lista = []
# i = 1

# while i <=20:
#     lista.append(r.randrange(1, 100, 3))
#     i = i+1

# print(f'Essa foi a lista gerada aleatoriamente: {lista}')

# # f -> serve pra concatenar texto e funcao



# def maior_valor(lista):
#     return max(lista, key=int)

# m = maior_valor(lista)

# print(f'Maior valor é: {m}')

# ------------------------------------
# -*- coding: utf-8 -*-

# def retornar_itens_estoque(setor, *args):
#     print(f'Lista salva no estoque do setor: {setor}:')
#     for item in args:
#         print(item)

# retornar_itens_estoque('Administrativo', 'Documentos de A a Z', 'Livros de caixa', 'Computadores')

# ----------------------------------

# def lista_de_compras(pessoa, **kwargs):
#     fruta = kwargs.get('fruta')
#     if fruta is not None:
#         print(f'Na lista de compras do {pessoa} há uma fruta: {fruta}')

# lista_de_compras('Jureg', fruta='Abacate', massas='Macarrão', verdura='Couve')

# lista_de_compras('Irmão do Jorel', fruta= 'atemoia', bebida='Catuaba', sorvete='Limão')

# -----------------------------------

# Exercicio 2
# - crie uma lista com 10 numeros aleatorios, 
# itere essa lista e printar em tela os valores que são impares e pares.

# exemplo de resultado em tela:

# Essa foi a lista gerada aleatoriamente: [37, 52, 73, 91, 49, 67, 19, 64, 58, 22]
# ímpares: [37, 73, 91, 49, 67, 19]
# pares: [52, 64, 58, 22]

# Resolucao:

# import random as r

# lista = []
# lista_par = []
# lista_impar = []
# i = 1

# while i <=10:
#     lista.append(r.randrange(1, 100, 3))
#     i = i+1

# print(f'Essa foi a lista gerada aleatoriamente: {lista}')

# for a in lista:
#     if a % 2 != 0:
#         lista_impar.append(a)
#     else:
#         lista_par.append(a)

# print(f'impares: {lista_impar}')
# print(f'pares: {lista_par}')

# ----------------------------------------

# import math
# math.sqrt

# Exercicio 3
# - crie uma função python que calcule uma funcao de 2 grau

# Delta = B² - 4AC 
# Bhaskara = -B +- (raiz de delta)/ 2A



# Exercicio 4
# - faça um programa que leia o raio de um circulo e faça duas funçoes: uma que calcule a area do circulo e outra que calcule o cumprimento do circulo.

# area do circulo:

# A = pi . r2


