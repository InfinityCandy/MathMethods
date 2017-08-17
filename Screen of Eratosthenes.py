numerosPrimos = []


n = int(input("Ingrese el numero: "))


for i in range(n):
    numerosPrimos.append(i + 1)

w = 1
while(True):
    x = w

    while(x < len(numerosPrimos)):
        if(numerosPrimos[x] == numerosPrimos[w]):
            numerosPrimos

        elif(numerosPrimos[x] % numerosPrimos[w] == 0):
            numerosPrimos[x] = 0
        x = x + 1

    for z in range(len(numerosPrimos)):
        if(numerosPrimos[z] != 1 and numerosPrimos[z] != 0 and  z > w):
            w = z
            break

    if (pow(numerosPrimos[w], 2) > n):
        break

numerosPrimosFinal = []

for y in range(len(numerosPrimos)):
   if(numerosPrimos[y] != 0 and numerosPrimos[y] != 1):
        numerosPrimosFinal.append(numerosPrimos[y])

print(numerosPrimosFinal)
