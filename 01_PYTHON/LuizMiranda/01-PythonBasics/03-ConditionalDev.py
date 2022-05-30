# IF / ELIF / ELSE Conditional______________________________________________

from socket import INADDR_ALLHOSTS_GROUP
import string
from traceback import print_tb
from unicodedata import name


if False:
    print("Verdadeiro 01")
elif True:
    print("Verdadeiro 02")
elif False:
    print("Verdadeiro 03")
else:
    print("Não é verdadeiro")

# Relacional Operators ______________________________________________________
# == , < , <= , > , >= , != -> Return True or False

var_01 = 1
var_02 = "Donny"

print(var_01 == var_02)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

limit_teenage = 18
limit_adult = 30

if age >= limit_teenage and age <= limit_adult:
    print(f"{name} can get the loan")
else:
    print(f"{name} can't get the loan")

# Logical Operators _________________________________________________________
# and, or , not, in e not in

name = "Donny rivera"

if "rdave" not in name:
    print("Don't Exists")
else:
    print("Exists")


a = 0
b = 1
c = 0

for i in range(1, 10):
    c = b
    b = b + a
    a = c
print(b)


i = 0
number = int(input("number: "))

while (number <= 0) or (number > 125):
    print("Invalid Value")
    i += 1
    number = int(input("Number: "))
print(i)


a = ""
b = 0

if not b:
    print("Por favor preencha o valor de B")

nome = "Luiz Otavio"

if "vio" not in nome:
    print("Executei")
else:
    print("Existe o texto")

usuario = input("Nome do usuario: ")
senha = input("Senha do usuario: ")

usuario_bd = "donny"
senha_bd = "123456"

if usuario_bd == usuario and senha_bd == senha:
    print("Voce está logado no sistema")
else:
    print("Usuario e senha invalidos")

# Quantity of Caracteres _________________________________________________________

usuario = input("Digite seu usuario: ")
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("Voce precisa digitar pelo menos 6 caracteres")
else:
    print("Voce foi cadastrado no sistema")


string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")

print(f"A quantidade total de caracteres digitados foi {len(string1) + len(string2)}")
print(string2.__len__())  # Default function

# Documentation and Bult-in Functions  ____________________________________________

num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

# Numeros inteiros e positivos
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Não foi possivel converter os numeros para realizar contas")

num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except:
    print("Não foi possivel converter os numeros para realizar contas")


# Placeholders ____________________________________________________________________
# pass / ... elipse

valor = True

if valor:
    ...
else:
    print("Tchau")
