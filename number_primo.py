#Faça um código pra listar todos os divisores de um número ou dizer que o número é primo caso ñ existam divisores

while True:
    num=int(input("\nDigite um número inteiro positivo: "))
    #conta divisores
    qtd_divisores = 0
    print(f"Divisores de {num}: ",end="")
    # loop para encontrar e exibir os divisores
    for i in range(1, num+1):
        if num%i==0:
            print(i, end=" ") #exibe o divisor
            qtd_divisores +=1
#verificar se o número é primo baseado na QTD
print()
if qtd_divisores == 2:
    print(f"Conclusão: O número {num} é primo!!")
else:
    print(f"Conclusão: O número {num} não é primo!! (possui {qtd_divisores} divisores)")   

#opção para inserir novo número
continuar = input("\nDeseja analisar outro número?(S/N): ")
upper()
if continuar !="S":
    "break"