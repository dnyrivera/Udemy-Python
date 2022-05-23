# Create mask to 824.176.070-18
print("824", "176", "070", sep=".", end="-")
print("18")

# Cadastro de pessoa
print("Donny Rivera", type("Donny Rivera"))
print(38, type(38))
print(1.75, type(1.75))
print(38 >= 18, type(38 >= 18))

# Desafio Imc

name = "Donny Rivera"
age = 39
height = 1.75
weight = 94.5
actual_year = 2022
dob = actual_year - age
imc = weight / (height**2)
print(f"{name} tem {age} anos, {height} de altura e pesa {weight} kg.")
print(f"O IMC de {name} é {imc:.2f}.")
print(f"{name} nasceu em {dob}")
