maior = 0
menor = 0
soma = 0

while(True):
    print("==================================================")
    for x in range(20):
        try:
            num = float(input("Informe um valor: "))
            if(x == 0):
                maior = num
                menor = num
            if(num > maior):
                maior = num
            elif(num < menor):
                menor = num
            soma = soma+num
            media = soma/20
        except:
            print("Comando inválido, tente novamente.")
        
    print("==================================================")
    print("Média:",media)
    print("Maior:",maior)
    print("Menor:",menor)
    print("==================================================")
    input("Programa finalizado, Aperte ENTER para reiniciar.")
    
