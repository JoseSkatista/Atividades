n_desejado = int(input("Quantos números perfeitos você deseja encontrar? "))
encontrados = 0
numeros_testados = 2 #começa no 2 pois o 1 não é perfeito
print(f"Buscando os {n_desejado} primeiros números perfeitos")
while encontrados < n_desejado:
    soma_divisores = 0
#encontra os divisores do 'numero testado'
    for i in range(1, numeros_testados):
        if numeros_testados % i == 0:
            soma_divisores += i
    #verificar se a soma é igual ao número
    if soma_divisores == numeros_testados:
        encontrados += 1
    print(f"{encontrados}. número perfeito encontrado: {numeros_testados}")      