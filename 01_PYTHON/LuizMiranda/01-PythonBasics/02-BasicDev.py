# Variaveis ______________________________________________________________

# Iniciar com letra, pode contar numeros, separar '_' e usar letras minusculas
nome = "Donny"
idade = 38
altura = 1.75
peso = 95
e_maior = idade > 18
imc = peso / (altura**2)

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Peso:", peso)
print("Maior:", e_maior)
print(nome, "tem", idade, "anos e seu IMC é:", imc)

# Formatar Strings_______________________________________________________

# f-string
print(f"Fstring: {nome} tem {idade} anos e seu IMC é: {imc:.2f}")
# format
print("Format Vazio: {} tem {} anos e seu IMC é: {:.2f}".format(nome, idade, imc))
print("Format Numerado: {0} tem {1} anos e seu IMC é: {2:.2f}".format(nome, idade, imc))
print(
    "Format Nomeado: {nome} tem {idade} anos e seu IMC é: {imc:.2f}".format(
        nome=nome, idade=idade, imc=imc
    )
)

# Input()__________________________________________________________________

name = input("Enter your name: ")
# print(f"Seu nome é {name} e o tipo é {type(name)}")

number_01 = int(input("Enter the first number: "))
number_02 = int(input("Enter the second number:  "))

print(f"Soma:", number_01 + number_02)
