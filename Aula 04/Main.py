from Calculadora import *
from Lambda import *

class main:
    x=int(input("Escolha a sua operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha: "))
    if(x==1):
        A=int(input("Digite o seu Número 1: "))
        B=int(input("Digite o seu Número 2: "))
        print(Lambda.Adi(A,B))
    if(x==2):
        A=int(input("Digite o seu Número 1: "))
        B=int(input("Digite o seu Número 2: "))
        print(Lambda.Sub(A,B))
    if(x==3):
        A=int(input("Digite o seu Número 1: "))
        B=int(input("Digite o seu Número 2: "))
        print(Lambda.Mul(A,B))
    if(x==4):
        A=int(input("Digite o seu Número 1: "))
        B=int(input("Digite o seu Número 2: "))
        print(Lambda.Div(A,B))