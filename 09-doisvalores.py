x = int(input("Digite o dividendo (x): "))
y = int(input("Digite o divisor (y): "))
# guardar os valores originais
dividendo = x
divisor = y

# a lógica: Subtrair enquanto o x for maior ou igual ao divisor
while x >= y:
    x -= y
    quociente = 0
  
resto = x
print("-"*40)
print(f"O resultado do {dividendo} / {divisor}: ")
print(f"Quociente (divisão inteira): {quociente}")
print(f"Resto: {resto}")
print("-"*40)    