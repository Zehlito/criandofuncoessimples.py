#CRIANDO FUNÇÕES SIMPLES EM PYTHON

def calculadoraSoma(num1,num2):
    soma = num1+num2
    return soma
def calculadoraSub(num1,num2):
    sub = num1-num2
    return sub
def calculadoraMulti(num1,num2):
    multi = num1*num2
    return multi
def calculadoraDiv(num1,num2):
    div = num1/num2
    return div
def numeroQuadrado(num1):
    quadra= num1**2
    return quadra
#ALGUNS EXEMPLOS

import minha_biblioteca #BIBLIOTECA QUE EU CRIEI ;)

#muito fácil criar e importar bibliotecas!!!

print(minha_biblioteca.calculadoraSoma(8,6))

print(minha_biblioteca.calculadoraSub(8,6))

print(minha_biblioteca.calculadoraMulti(8,6))

print(minha_biblioteca.calculadoraDiv(8,6))

print(minha_biblioteca.numeroQuadrado(8))