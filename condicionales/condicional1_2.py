n1 = int(input("Ingrese el numero 1:\t"))
n2 = int(input("Ingrese el numero 2:\t"))
n3 = int(input("Ingrese el numero 3:\t"))

if (n1 > n2) and (n1 > n3):
	print(n1)
	if n2 > n3:
		print(n2)
		print(n3)
	else:
		print(n3)
		print(n2)
elif (n2 > n1) and (n2 > n3):
    print(n2)
    if n1 > n3:
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
elif (n3 > n1) and (n3 > n2):
    print(n3)
    if n1 > n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)