L = [5,7,2,9,4,1,3]

maior = max(L)
menor = min(L)
soma = 0

ordenada = sorted(L)
inversa = sorted(L, reverse = True)

print("====================================================")
print("Tamanho da Lista:",len(L))
print("Maior valor da Lista:",maior)
print("Menor valor da Lista:",menor)
print("Soma de todos os Valores da Lista:",soma)
print("====================================================")
print("Lista em ordem crescente:",ordenada)
print("Lista em ordem decrescente:",inversa)
