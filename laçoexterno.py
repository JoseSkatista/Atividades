#laço externo que percorre os números de 1 a 10
for i in range(1,11):
    print(f"\nTabuada do {i}")#/n é pra quebrar linha
    #laço interno calcula a multiplicação
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")