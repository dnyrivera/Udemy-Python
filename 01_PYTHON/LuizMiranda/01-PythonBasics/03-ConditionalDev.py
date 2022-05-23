# IF / ELIF / ELSE Conditional______________________________________________

from socket import INADDR_ALLHOSTS_GROUP
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

for i in range(1,10):
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

