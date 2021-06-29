soma = 0

while(True):
    try:
        print("===========================================")
        for x in range(4):
            nota = float(input("Informe o valor da nota:"))
            soma = soma+nota;
        media = soma/4
        print("===========================================")
        print("Média final:",media)
        if(media > 1):
            print("A média é positiva!")
        else:
            print("a média é negativa!")
        break
    except:
        print("Comando inválido, tente novamente.")
