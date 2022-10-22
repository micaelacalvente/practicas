#Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
print("Hola, ingrese tres numeros para ser ordenados: ")
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
n3 = int(input("Ingrese un numero final: "))

if n1 > n2 and n2 > n3:
    print(n1, n2, n3)
elif n1 > n2 and n2 < n3:
    print(n1, n3, n2)
elif n2 > n1 and n1 > n3:
    print(n2, n1, n3)
elif n2 > n1 and n1 < n3:
    print(n2, n3, n1)
elif n3 > n1 and n1 > n2:
    print(n3, n1, n2)
elif n3 > n1 and n1 < n2:
    print(n3, n2, n1)