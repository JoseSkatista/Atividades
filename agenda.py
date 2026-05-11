#programa para imprimir uma agenda diária
#com horários de 15 em 15 minutos
for hora in range(24):
    for minuto in range(0,60,15):
        print(f"{hora:02d}:{minuto:02d}")