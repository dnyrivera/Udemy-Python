# print()_________________________________________________________________

print(123434)
print("Donny", "Rivera", "Negrao", sep="*", end=" | ")
print("Donny", "Rivera", "Negrao", sep="-")

# Strings e Aspas_________________________________________________________

print("aspas simples")
print("aspas duplas")
print("""aspas triplas""")
print("Essa é uma 'string' (str)")
print('Essa é uma "string" (str)')
print('Esse é meu "texto" (str)')
print(r"Quebra de \n Linha")  # colocar o r na frente para cortar a funcao.

# Tipos de dados Primitivos ______________________________________________
# string - integer - float - boolean

print("Luiz", type("Luiz"), bool("Luiz"))
print(10, type(10), str(10), float(10), bool(10))
print(10.10, type(10.10), int(10.10), bool(10.10))
print("True", 10 == 10, type(True), int(True))

# Operadores Aritmeticos _________________________________________________
# + , - , * , / , // , ** , &, ()

print("Adicao:", 10 + 10)
print("Subtracao:", 10 - 10)
print("Multiplicacao:", 10 * 10)
print("Divisao:", 10 / 10)

print("Multiplicacao String:", "A" * 10)
print("Concatenar String:", "5" + "5")

print("Divisao Inteira:", 10.5 // 3)
print("Potencia:", 10**2)
print("Modulo Divisão:", 10 % 3)
