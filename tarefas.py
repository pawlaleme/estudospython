"""Este módulo contém um programa para cadastro de restaurantes.
Ele inclui funcionalidades para cadastrar, listar e ativar restaurantes.
"""


#import os
# pylint: disable=missing-function-docstring,

#Para criar as listas, podemos utilizar as seguintes variáveis:

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['emy','gui','lais','mari']
lista_de_anos = [1999,2023]

#Para percorrer todos os itens de uma lista com o loop for, você pode usar essa estrutura:
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(numero)

#Para fazer calcular a soma dos números impares de 1 a 10, você pode utilizar o seguinte código:
SOMA_IMPARES = 0
for i in range(1, 11, 2):
    SOMA_IMPARES += i
print(SOMA_IMPARES)

#Para imprimir os números de 1 a 10 de forma decrescente, você pode utilizar a seguinte estrutura:
for i in range(10, 0, -1):
    print(i)

# Para fazer uma tabuada interativa, você pode seguir o seguinte código:
    numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

#para fazer a soma dos elementos de uma lista com for e usar try except para validar:

lista_numeros = [10, 5, 8, 3, 7]
SOMA = 0

try:
    for numero in lista_numeros:
        SOMA += numero
    print(f"Soma dos elementos: {SOMA}")
except ValueError as e:
    print(f"Ocorreu um erro: {e}")

#Um modo de solucionar essa questão com uma validação de lista vazia é do seguinte modo:
lista_valores = [15, 20, 25, 30]
SOMA_VALORES = 0

try:
    for valor in lista_valores:
        SOMA_VALORES += valor
    MEDIA = SOMA_VALORES / len(lista_valores)
    print(f"Média dos valores: {MEDIA}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except ArithmeticError:
    print(f"Ocorreu um erro: {e}")
