#nombre de usuario y contraseña
usuario, contrasenia = "admin", "123"

diccionarioHuevos = {"huevos de gallina":50, "huevos de pato":150, "huevos de codorniz":50, "huevos de avestruz":800}
diccionarioDespachos = {"ID despacho":0, "Nombre o razon social":"0", "Rut":"0", "Direccion":"0", "Fecha de envio":"0", "Tipo de huevo":"0", "Cantidad de huevos":0, "Precio unitario":0, "Descuento":0, "Precio total":0}
llaveDespachos = []
valorDespachos = []
bandera = True
bandera2 = True
idDdespacho = 1000000
limiteIdDespacho = 9999999

#login usuario y contraseña.
userName = input("Ingrese su nombre de usuario: ")
userName = userName.lower()
password = input("Ingrese su contraseña: ")
print("")

#comprobacion de usuario y contraseña.
while userName != usuario or password != contrasenia:
    print("Error en su usuario o contraseña")
    print("Porfavor ingrese nuevamente su usuario y contraseña")
    print("")
    userName = input("Ingrese su nombre de usuario: ")
    userName = userName.lower()
    password = input("Ingrese su contraseña: ")
    print("")

#menu de opciones.
while bandera == True:
    print("+--------------------------------------------+")
    print("|                                            |")
    print("| Distribuidora de huevos mayorista All Eggs |")
    print("|                    S.A                     |")
    print("+--------------------------------------------+")
    print("")
    
    print("a.- Asignacion de precios de huevos")
    print("b.- Crear Despacho")
    print("c.- Listar huevos")
    print("d.- Listar despachos")
    print("e.- Salir del programa")
    opcion = input("Ingrese la opcion que desea realizar: ")
    opcion = opcion.lower()
    print("")
    if opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d" and opcion != "e":
        print("Error, ingrese una de las opciones disponibles") 
        print("")

    #submenu (opcion a) asignar precios a huevos.
    while opcion == "a" or opcion == "b" or opcion == "c" or opcion == "d" or opcion == "e":        
        if opcion == "a":
            print("1.- Asignar precio a huevos de Gallina")
            print("2.- Asignar precio a huevos de Pato")
            print("3.- Asignar precio a huevos de Codorniz")
            print("4.- Asignar precio a huevos de Avestruz")
            print("5.- Volver a menu anterior")
            opcionHuevo = input("Ingrese la opcion a la que desea modificar el precio: ")
            print("")

            #si opcion 1, asignar precio a huevo de gallina.
            if opcionHuevo == "1":
                try:
                    valorhuevo = int(input("Ingrese el nuevo valor: $"))
                    while valorhuevo < 50:
                        print("El valor no puede ser menor a $50, porfavor ingrese un valor nuevamente")
                        valorhuevo = int(input("Ingrese el nuevo valor: $"))
                    diccionarioHuevos["huevos de gallina"] = valorhuevo
                    print("El cambio se a echo correctamente")
                    print("Valor de huevos de gallina ahora es:$",diccionarioHuevos["huevos de gallina"])
                    print("")
                except:
                    print("Se a detectado una anomalia en el cambio de precios, se a vuelto al menu")
                    print("")

            #si opcion 2, asignar precio a huevo de pato.       
            elif opcionHuevo == "2":
                try:
                    valorhuevo = int(input("Ingrese el nuevo valor: $"))
                    while valorhuevo < 150:
                        print("El valor no puede ser menor a $150, porfavor ingrese un valor nuevamente")
                        valorhuevo = int(input("Ingrese el nuevo valor: $"))
                    diccionarioHuevos["huevos de pato"] = valorhuevo
                    print("El cambio se a echo correctamente")
                    print("Valor de huevos de pato ahora es:$", diccionarioHuevos["huevos de pato"])
                    print("")
                except:
                    print("Se a detectado una anomalia en el cambio de precios, se a vuelto al menu")
                    print("")

            #si opcion 3, asignar precio a huevo de codorniz.        
            elif opcionHuevo == "3":
                try:
                    valorhuevo = int(input("Ingrese el nuevo valor: $"))
                    while valorhuevo < 50:
                        print("El valor no puede ser menor a $50, porfavor ingrese un valor nuevamente")
                        valorhuevo = int(input("Ingrese el nuevo valor: $"))
                    diccionarioHuevos["huevos de codorniz"] = valorhuevo
                    print("El cambio se a echo correctamente")
                    print("Valor de huevos de codorniz ahora es:$", diccionarioHuevos["huevos de codorniz"])
                    print("")
                except:
                    print("Se a detectado una anomalia en el cambio de precios, se a vuelto al menu")
                    print("")

            #si opcion 4, asignar precio a huevo de avestruz.
            elif opcionHuevo == "4":
                try:
                    valorhuevo = int(input("Ingrese el nuevo valor: $"))
                    while valorhuevo < 800:
                        print("El valor no puede ser menor a $800, porfavor ingrese un valor nuevamente")
                        valorhuevo = int(input("Ingrese el nuevo valor: $"))
                    diccionarioHuevos["huevos de avestruz"] = valorhuevo
                    print("El cambio se a echo correctamente")
                    print("Valor de huevos de avestruz ahora es:$", diccionarioHuevos["huevos de avestruz"])
                    print("")
                except:
                    print("Se a detectado una anomalia en el cambio de precios, se a vuelto al menu")
                    print("")
            #volver a menu anterior
            elif opcionHuevo == "5":
                opcion = None

        #submenu (opcion b) creacion de despachos.
        elif opcion == "b":
                #ingreso de id despacho
                for idDespacho in range(limiteIdDespacho):
                    idDdespacho += 1
                    diccionarioDespachos["ID despacho"]=idDdespacho
                    break
                print("")

                #ingreso de nombre
                while True:
                    nombreRazonSocial = input("Ingrese su nombre o razon social: ")
                    if not nombreRazonSocial or nombreRazonSocial.isspace():
                        print("Error, debe ingresar un nombre")
                        print("")
                    else:
                        break
                diccionarioDespachos["Nombre o razon social"]=nombreRazonSocial
                print("")
            
                #ingreso de rut
                while True:
                    rut = input("Ingrese su rut (No utilize puntos ni guion, ejemplo: 01234567): ")
                    if len(rut) != 8 and len(rut) != 9:
                        print("Error, ingrese nuevamente su rut")
                        print("")
                    else:
                        break
                diccionarioDespachos["Rut"]=rut
                print("")   
                
                #ingreso de direccion
                while True:
                    direccion = input("Ingrese su direccion: ")
                    if not direccion or direccion.isspace():
                        print("Error, ingrese nuevamente su direccion")
                        print("")
                    else:
                        break
                diccionarioDespachos["Direccion"]=direccion
                print("")
                
                #ingreso fecha de envio
                while bandera2 == True:
                    fechaEnvio = input("ingrese la fecha de envio (dd-mm-yyyy): ")
                    if len(fechaEnvio) == 10:
                        bandera2 = False
                    else:
                        print("Error, datos invalidos")
                        print("")
                bandera2 = True             
                diccionarioDespachos["Fecha de envio"]=fechaEnvio
                print("")
                
                #ingreso de tipo de huevo
                while bandera2 == True:
                    print("1.- Huevos de gallina")
                    print("2.- Huevos de pato")
                    print("3.- Huevos de codorniz")
                    print("4.- Huevos de avestruz")
                    tipoDeHuevo = input("Ingrese el tipo de huevo que desea registrar: ")
                    if tipoDeHuevo == "1":
                        tipoDeHuevo = "huevos de gallina"
                        bandera2 = False
                    elif tipoDeHuevo == "2":
                        tipoDeHuevo = "huevos de pato"
                        bandera2 = False
                    elif tipoDeHuevo == "3":
                        tipoDeHuevo = "huevos de codorniz"
                        bandera2 = False
                    elif tipoDeHuevo == "4":
                        tipoDeHuevo = "huevos de avestruz"
                        bandera2 = False
                    else:
                        print("Error, seleccione una de las opciones disponibles")
                        print("")
                diccionarioDespachos["Tipo de huevo"]=tipoDeHuevo
                bandera2 = True
                print("")
                
                #ingreso de la cantidad de huevos
                while bandera2 == True:
                    try:    
                        cantidadHuevos = int(input("Ingrese la cantidad de huevos que desea enviar: "))
                        if cantidadHuevos >= 50 and cantidadHuevos <= 10000:
                            bandera2 = False
                        else:
                            print("Error, la cantidad minima de envio es de 50 hasta un maximo de 10.000")
                    except:
                        print("Error, ingrese nuevamente un valor")
                        print("")
                diccionarioDespachos["Cantidad de huevos"]=cantidadHuevos
                diccionarioDespachos["Precio unitario"]=diccionarioHuevos[tipoDeHuevo]
                bandera2 = True
                print("")

                #descuento(solo si tiene convenio)
                while bandera2 == True:
                    convenio = input("¿Tiene convenio?, escriba 'si' en caso de tener, caso contrario escriba 'no': ")
                    convenio = convenio.lower()
                    if convenio == "si":
                        totalPrecioHuevos = cantidadHuevos * diccionarioHuevos[tipoDeHuevo]
                        descuento = totalPrecioHuevos * 0.1
                        totalPrecioHuevos = totalPrecioHuevos - descuento
                        diccionarioDespachos["Descuento"]=descuento
                        diccionarioDespachos["Precio total"]=totalPrecioHuevos
                        bandera2 = False
                    elif convenio == "no":
                        descuento = 0
                        totalPrecioHuevos = cantidadHuevos * diccionarioHuevos[tipoDeHuevo]
                        diccionarioDespachos["Descuento"]=descuento
                        diccionarioDespachos["Precio total"]=totalPrecioHuevos
                        bandera2 = False
                    else:
                        print("Error, vuelva a ingresar la informacion")
                        print("")
                bandera2 = True
                opcion = None
                for clave,valor in diccionarioDespachos.items():
                    llaveDespachos.append(clave)
                    valorDespachos.append(valor)
                print("El despacho se a creado con exito")
                print("")
                
        #lista de huevos mas precios    
        elif opcion == "c":
            print("+--------------------------------------------+")
            print("|                                            |")
            print("| Distribuidora de huevos mayorista All Eggs |")
            print("|                    S.A                     |")
            print("+--------------------------------------------+")
            print("|        Producto: Huevo de gallina          |")
            print("|\t   Precio:$", diccionarioHuevos["huevos de gallina"], "                      |")
            print("+--------------------------------------------+")
            print("|        Producto: Huevo de pato             |")
            print("|\t   Precio:$", diccionarioHuevos["huevos de pato"], "                     |")
            print("+--------------------------------------------+")
            print("|        Producto: Huevo de codorniz         |")
            print("|\t   Precio:$", diccionarioHuevos["huevos de codorniz"], "                      |")
            print("+--------------------------------------------+")
            print("|        Producto: Huevo de avestruz         |")
            print("|\t   Precio:$", diccionarioHuevos["huevos de avestruz"], "                     |")
            print("+--------------------------------------------+")
            opcion = None
            print("")
       
        #lista de despachos guardados
        elif opcion == "d":
            for c,v in zip(llaveDespachos,valorDespachos):
                if bandera2 == True:
                    print("+--------------------------------------------+")
                    print("|                                            |")
                    print("| Distribuidora de huevos mayorista All Eggs |")
                    print("|                    S.A                     |")
                    print("+--------------------------------------------+")
                    print(f"| {c:<21} {':'}{v:>19} |")
                    bandera2 = False
                if c == "Nombre o razon social":
                    print(f"| {c:<21} {':'}{v:>19} |") 
                if c == "Rut":
                    print(f"| {c:<21} {':'}{v:>19} |")
                if c == "Direccion":
                    print(f"| {c:<21} {':'}{v:>19} |")
                if c == "Fecha de envio":
                    print(f"| {c:<21} {':'}{v:>19} |")
                    print("+--------------------------------------------+")
                if c == "Tipo de huevo":
                    print(f"| {c:<21} {':'}{v:>19} |")
                if c == "Cantidad de huevos":
                    print(f"| {c:<21} {':'}{v:>19} |")
                if c == "Precio unitario":
                    print(f"| {c:<21} {':'}{v:>19} |")
                if c == "Descuento":
                    print(f"| {c:<21} {':'}{v:>19} |")
                    print("+--------------+-----------------------------+")
                if c == "Precio total":
                    print(f"               | {c:<10} {':'}  {v:>11} |")
                    print("               +-----------------------------+")
                    print("")
                    print("")
                    bandera2 = True
            opcion = None
            print("")       
            
        #cerrar aplicacion
        elif opcion == "e":
            opcion = None
            bandera = False
            print("El programa se a cerrado")