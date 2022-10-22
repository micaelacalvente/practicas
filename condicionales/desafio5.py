#La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre del barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
# La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos 
# con nombre posterior a la M, y la sección B el resto.
# Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.

barrio = input("Ingrese el nombre de su barrio: ")
ubicacion = int(input("Donde se ubica su barrio? \n 1.CENTRO \n 2.NO CENTRO: \n"))

if barrio.lower() < "m" and ubicacion == 1:
    print("SECCION A")
elif barrio.lower() > "m" and ubicacion == 2:
    print("SECCION A")
elif barrio.lower() >= "m" and ubicacion == 1:
    print("SECCION B")
elif barrio.lower() <= "m" and ubicacion == 2:
    print("SECCION B")
else:
    print("Valor ingresado no valido")