#Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo sea mayor o igual que el primero.
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese hasta que número desea saber la multiplicidad: "))

contador = 0

for num in range(n1, n2):
    if num % 2 == 0:
        print(num)
        contador += 1

print ("hay", contador, "múltiplos de 2")