L = [5,7,2,9,4,1,3]

maior = 0
menor = 0
soma = 0

def Sort(matriz):
    for a in range(len(matriz)-1):
        if(matriz[a]>matriz[a+1]):
            maior = matriz[a]
            menor = matriz[a+1]
            
            matriz[a] = menor
            matriz[a+1] = maior

for x in range(len(L)):
    if(x == 0):
        maior = L[x]
        menor = L[x]
    if(L[x] > maior):
        maior = L[x]
    elif(L[x] < menor):
        menor = L[x]
    soma = soma+L[x]

for y in range(len(L)):
    Sort(L)

rev = []

for i in reversed(range(len(L))):
    rev.append(L[i])


print("====================================================")
print("Tamanho da Lista:",len(L))
print("Maior valor da Lista:",maior)
print("Menor valor da Lista:",menor)
print("Soma de todos os Valores da Lista:",soma)
print("====================================================")
print("Lista em ordem crescente:",L)
print("Lista em ordem decrescente:",rev)

input("")
