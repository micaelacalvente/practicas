# Debemos elaborar un programa en Python que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años 
# que viene usando insecticida en su plantación. Si hace 10 o más años, debemos emitir el mensaje 
# "Por favor solicite revisión de suelos en su plantación". Si hace menos de 10 años, debemos emitir el mensaje 
# "Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".

cantidad_años = int(input("Por favor ingrese la cantidad de años: "))
if (cantidad_años >= 10):
    print("Por favor solicite revisión de suelos en su plantación")
else:
    print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación")