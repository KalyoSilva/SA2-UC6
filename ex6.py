while(True):
    try:
        print("==============================================")
        hr = float(input("Informe o valor em horas:"))

        s = hr*3600
        print("")
        print(hr,"horas equivalem a",s,"segundos.")
        break
    except:
        print("Valor inválido, tente novamente.")

print("==============================================")
input("Programa finalizado, pressione ENTER para sair")
