# En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para reciclar,
# de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra. 
# Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 
# Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento.

# descuento rojo: 100
# descuento amarillo: 20-100
# descuento blanco: -10

print("Bienvenido, le recuerdo que si presenta tapitas puede acceder a un descuento!")
tienda = input("Esta abierta la tienda?")

###tienda = "si"

while tienda == "si":
    tapitas = int(input("Ingrese la cantidad de tapitas que tiene: "))
    importe = float(input("Ingrese el total de su compra: "))
    if tapitas >= 100:
        print("Haz obtenido un descuento rojo!")
        descuentoR = float((40*importe)/100)
        print("El total de su compra es:", descuentoR)
    elif tapitas >= 20 and tapitas < 100:
        print("Haz obtenido un descuento amarillo!")
        descuentoA = float((25*importe)/100)
        print("El total de su compra es:", descuentoA)
    else:
        print("Lo siento el numero de tapitas no le corresponde ningun descuento")
        print("El total de su compra es:", importe)
        break

while tienda == "no":
    print("Lo siento, la tienda se encuentra cerrada, regrese en otro horario")
    break

##ctrl + c



