print("Hola! Seleccione un tipo de receta, para el cual desea ver sus ingredientes")
print("1 - Receta 1")
print("2 - Receta 2")
print("Selecciona opcion 1 u opcion 2") 

receta_elegida = input("> ")

if receta_elegida == "1" or receta_elegida == "2":
    print("Los ingredientes disponibles son:")
    print("1 - VERDURAS")
    print("2 - BERENJENAS")

    if receta_elegida == "1":
        # Mostrar los ingredientes de la receta 1
        print("3 - APIO")
        print("4 - LENTEJAS")
    else:
        print("3 - MORRON")
        print("4 - CEBOLLA")

    print("Selecciona opcion 1 , 2, 3 o 4") 
    ingrediente_elegido1 = input("> Ingrediente 1: ")
    ingrediente_elegido2 = input("> Ingrediente 2: ")
    ingrediente_elegido3 = input("> Ingrediente 3: ")

    # "La receta elegida fue la receta " + receta_elegida
    print(f"La receta elegida fue la receta {receta_elegida}")
    print("Los ingredientes elegidos fueron:")

    # Verificamos el nombre del ingrediente 1 elegido
    if ingrediente_elegido1 == "1":
        print("VERDURAS")
    elif ingrediente_elegido1 == "2":
        print("BERENJENAS")
    elif ingrediente_elegido1 == "3" and receta_elegida == "1":
        print("APIO")
    elif ingrediente_elegido1 == "3" and receta_elegida == "2":
        print("MORRON")
    elif ingrediente_elegido1 == "4" and receta_elegida == "1":
        print("LENTEJAS")
    elif ingrediente_elegido1 == "4" and receta_elegida == "2":
        print("CEBOLLAS")
    else:
        print("El ingrediente 1 elegido es incorrecto")

 # Verificamos el nombre del ingrediente 2 elegido
    if ingrediente_elegido2 == "1":
        print("VERDURAS")
    elif ingrediente_elegido2 == "2":
        print("BERENJENAS")
    elif ingrediente_elegido2 == "3" and receta_elegida == "1":
        print("APIO")
    elif ingrediente_elegido2 == "3" and receta_elegida == "2":
        print("MORRON")
    elif ingrediente_elegido2 == "4" and receta_elegida == "1":
        print("LENTEJAS")
    elif ingrediente_elegido2 == "4" and receta_elegida == "2":
        print("CEBOLLAS")
    else:
        print("El ingrediente 2 elegido es incorrecto")

  # Verificamos el nombre del ingrediente 2 elegido
    if ingrediente_elegido3 == "1":
        print("VERDURAS")
    elif ingrediente_elegido3 == "2":
        print("BERENJENAS")
    elif ingrediente_elegido3 == "3" and receta_elegida == "1":
        print("APIO")
    elif ingrediente_elegido3 == "3" and receta_elegida == "2":
        print("MORRON")
    elif ingrediente_elegido3 == "4" and receta_elegida == "1":
        print("LENTEJAS")
    elif ingrediente_elegido3 == "4" and receta_elegida == "2":
        print("CEBOLLAS")
    else:
        print("El ingrediente 3 elegido es incorrecto")
else:
    # La opcion ingresada es incorrecta
    print("La opcion ingresada no corresponde a un  numero de receta valido.")