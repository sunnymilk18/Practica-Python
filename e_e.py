usuario = "admin"
contrasenia = "123"
diccionarioHuevos = {"huevos de gallina":"50", "huevos de pato":150, "huevos de codorniz":50, "huevos de avestruz":800}

userName = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")

while userName != usuario or password != contrasenia:
    print("Error en su usuario o contraseña")
    print("Porfavor ingrese nuevamente su usuario y contraseña")
    userName = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

print("a.- Asignacion de precios de huevos")
print("b.- Creacion de despachos")
print("c.- Listar huevos")
print("d.- Listar despachos")
opcion = input("ingrese la opcion que desea realizar: ")

if opcion == "a":
    print("1.- Asignar precio a huevos de Gallina")
    print("2.- Asignar precio a huevos de Pato")
    print("3.- Asignar precio a huevos de Codorniz")
    print("4.- Asignar precio a huevos de Avestruz")
    opcionHuevo = input("Ingrese la opcion a la que desea modificar el precio: ")
   
    if opcionHuevo == "1":
        valorhuevo = input("ingrese el nuevo valor: ")
        while valorhuevo < "50":
            print("el valor no puede ser menor a 50, porfavor ingrese un valor nuevamente")
            valorhuevo = input("ingrese el nuevo valor: ")
        diccionarioHuevos["huevos de gallina"] = valorhuevo
        print(f"el cambio se a echo correctamente")
        print("valor de huevos de gallina ahora es:", diccionarioHuevos["huevos de gallina"])
    
    if opcionHuevo == 2:
        valorhuevo = int(input("ingrese el nuevo valor: "))
        while valorhuevo < 150:
            print("el valor no puede ser menor a 150, porfavor ingrese un valor nuevamente")
            valorhuevo = int(input("ingrese el nuevo valor: "))
        diccionarioHuevos["huevos de pato"] = valorhuevo
        print(f"el cambio se a echo correctamente")
        print("valor de huevos de pato ahora es:", diccionarioHuevos["huevos de pato"])

