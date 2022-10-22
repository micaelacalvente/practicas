# Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.
##Ingredientes comunes: Verduras y berenjena.
##Ingredientes Receta 1: Lentejas y apio.
##Ingredientes Receta 2: Morrón y Cebolla.
##Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú con los ingredientes 
# disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. 
# Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.

print("Bienvenido! Ingrese el tipo de receta que desee: \n 1.receta 1: lenteja y apio \n 2.receta 2: morron y cebolla ")
receta = int(input("Receta: "))
print("Que tipo de ingrediente desearia agregar? \n a.berenjena \n b.verdura")
ingrediente = input("Ingrediente: ")

if receta == 1 and ingrediente.lower() == "a":
    print("Receta 1: \n lenteja \n apio \n berenjena")
elif receta == 1 and ingrediente.lower() == "b":
    print("Receta 1: \n lenteja \n apio \n berenjena")
elif receta == 2 and ingrediente.lower() == "a":
    print("Receta 2: \n morron \n cebolla \n berenjena")
elif receta == 2 and ingrediente.lower() == "b":
    print("Receta 2: \n morron \n cebolla \n berenjena")
else:
    print("Valor ingresado no valido")

