num = int(input("Digite um número: "))
contador = 0
if num == 0:
    contador = 1
else:
    temp = num
    while temp > 0:
        temp //=10 #remove o ultimo digito 
        contador += 1   