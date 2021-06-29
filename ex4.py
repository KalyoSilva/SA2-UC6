while(True):
    try:
        size = int(input("Informe o tamanho da linha: "))
        break
    except:
        print("Comando inválido, tente novamente.")

for x in range(size):
    print("_", end ="")

input("\n\nPrograma finalizado, pressione ENTER para sair.")
