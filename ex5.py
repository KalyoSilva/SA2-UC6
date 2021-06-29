x = []
print("==================================================")
while(True):
    try:
        size = int(input("informe o tamanho de sua lista:"))
        break
    except:
        print("Valor inválido, tente novamente")

def enumerar():
    
    print("==================================================")
    for y in range(len(x)):
        print("[",(y+1),"]-->",x[y])

print("==================================================")
while(True):
    for z in range(size):
        try:
            val = input("valor a ser adicionado na lista: ")
            x.append(val)
        except:
            print("Comando inválido, tente novamente.")
    enumerar()
    break

print("==================================================")
input("Programa finalizado, pressione ENTER para sair.")



