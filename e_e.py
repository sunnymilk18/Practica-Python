usuario = "admin"
contrasenia = "123"
diccionarioHuevos = {"huevos de gallina":50, "huevos de pato":150, "huevos de codorniz":50, "huevos de avestruz":800}

userName = input("Ingrese su nombre de usuario: ")
userName = userName.lower()
password = input("Ingrese su contraseña: ")
print("")

while userName != usuario or password != contrasenia:
    print("Error en su usuario o contraseña")
    print("Porfavor ingrese nuevamente su usuario y contraseña")
    userName = input("Ingrese su nombre de usuario: ")
    userName = userName.lower()
    password = input("Ingrese su contraseña: ")

print("a.- Asignacion de precios de huevos")
print("b.- Creacion de despachos")
print("c.- Listar huevos")
print("d.- Listar despachos")
opcion = input("ingrese la opcion que desea realizar: ")
opcion = opcion.lower()
print("")

while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d":
    print("Error, porfavor ingrese una de las opciones disponibles.")
    print("a.- Asignacion de precios de huevos")
    print("b.- Creacion de despachos")
    print("c.- Listar huevos")
    print("d.- Listar despachos")
    opcion = input("ingrese la opcion que desea realizar: ")
    opcion = opcion.lower()

if opcion == "a":
    print("1.- Asignar precio a huevos de Gallina")
    print("2.- Asignar precio a huevos de Pato")
    print("3.- Asignar precio a huevos de Codorniz")
    print("4.- Asignar precio a huevos de Avestruz")
    opcionHuevo = input("Ingrese la opcion a la que desea modificar el precio: ")
    print("")

    if opcionHuevo == "1":
        try:
            valorhuevo = int(input("Ingrese el nuevo valor: $"))
            while valorhuevo < 50:
                print("El valor no puede ser menor a $50, porfavor ingrese un valor nuevamente")
                valorhuevo = int(input("Ingrese el nuevo valor: "))
            diccionarioHuevos["huevos de gallina"] = valorhuevo
            print("El cambio se a echo correctamente")
            print("valor de huevos de gallina ahora es:$",diccionarioHuevos["huevos de gallina"])
        except:
            print("Se a detectado una anomalia en el cambio de precios, el programa se a cerrado")
    
    if opcionHuevo == "2":
        try:
            valorhuevo = int(input("Ingrese el nuevo valor: "))
            while valorhuevo < 150:
                print("El valor no puede ser menor a 150, porfavor ingrese un valor nuevamente")
                valorhuevo = int(input("Ingrese el nuevo valor: "))
            diccionarioHuevos["huevos de pato"] = valorhuevo
            print("El cambio se a echo correctamente")
            print("Valor de huevos de pato ahora es:$", diccionarioHuevos["huevos de pato"])
        except:
            print("Se a detectado una anomalia en el cambio de precios, el programa se a cerrado")
    
    if opcionHuevo == "3":
        try:
            valorhuevo = int(input("Ingrese el nuevo valor: "))
            while valorhuevo < 50:
                print("El valor no puede ser menor a 50, porfavor ingrese un valor nuevamente")
                valorhuevo = int(input("Ingrese el nuevo valor: "))
            diccionarioHuevos["huevos de codorniz"] = valorhuevo
            print("El cambio se a echo correctamente")
            print("Valor de huevos de codorniz ahora es:$", diccionarioHuevos["huevos de codorniz"])
        except:
            print("Se a detectado una anomalia en el cambio de precios, el programa se a cerrado")

        