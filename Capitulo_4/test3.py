#importação do módulo calc.py
from calc import *

#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

#armazenando a soma
soma = somar(valor1, valor2)
menos = subtrair(valor1, valor2)
multi = multiplicar(valor1,valor2)
divide = dividir(valor1,valor2)

#exibindo a soma
print("A soma é {}".format(soma))
print("A subtração é {}".format(menos))
print("A multiplicação é {}".format(multi))
print("A divisão é {}".format(divide))