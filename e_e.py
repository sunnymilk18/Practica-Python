#nombre de usuario
usuario = "admin"

#contraseña
contrasenia = "123"

diccionarioHuevos = {"huevos de gallina":50, "huevos de pato":150, "huevos de codorniz":50, "huevos de avestruz":800}
diccionarioDespachos = {"ID despacho":"0", "Nombre o razon social":"0", "Rut":"0", "Tipo de huevo":"0", "Direccion":"0", "Fecha de envio":"0", "Cantidad de huevos":0, "Precio total":0}
listaDiccionarioDespachos = []
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
    print("a.- Asignacion de precios de huevos")
    print("b.- Creacion de despachos")
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
                        valorhuevo = int(input("Ingrese el nuevo valor: "))
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
                    valorhuevo = int(input("Ingrese el nuevo valor: "))
                    while valorhuevo < 150:
                        print("El valor no puede ser menor a 150, porfavor ingrese un valor nuevamente")
                        valorhuevo = int(input("Ingrese el nuevo valor: "))
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
                    valorhuevo = int(input("Ingrese el nuevo valor: "))
                    while valorhuevo < 50:
                        print("El valor no puede ser menor a 50, porfavor ingrese un valor nuevamente")
                        valorhuevo = int(input("Ingrese el nuevo valor: "))
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
                    valorhuevo = int(input("Ingrese el nuevo valor: "))
                    while valorhuevo < 800:
                        print("El valor no puede ser menor a 800, porfavor ingrese un valor nuevamente")
                        valorhuevo = int(input("Ingrese el nuevo valor: "))
                    diccionarioHuevos["huevos de avestruz"] = valorhuevo
                    print("El cambio se a echo correctamente")
                    print("Valor de huevos de avestruz ahora es:$", diccionarioHuevos["huevos de avestruz"])
                    print("")
                except:
                    print("Se a detectado una anomalia en el cambio de precios, se a vuelto al menu")
                    print("")
            
            elif opcionHuevo == "5":
                opcion = None

        #submenu (opcion b) creacion de despachos.
        elif opcion == "b":
                #ingreso de id despacho
                for idDespacho in range(limiteIdDespacho):
                    idDdespacho += 1
                    diccionarioDespachos["ID despacho"]=idDdespacho
                    listaDiccionarioDespachos.append({"ID despacho":idDdespacho})

                    if idDdespacho != limiteIdDespacho:
                        break
                print("")

                #ingreso de nombre
                nombreRazonSocial = input("Ingrese su nombre o razon social: ")
                diccionarioDespachos["Nombre o razon social"]=nombreRazonSocial
                listaDiccionarioDespachos.append({"Nombre o razon social":nombreRazonSocial})
                print("")
            
                #ingreso de rut
                rut = input("Ingrese su rut (No utilize puntos ni guion): ")
                while len(rut) != 8 and len(rut) != 9:
                    rut = input("Ingrese su rut (No utilize puntos ni guion): ")
                diccionarioDespachos["Rut"]=rut
                listaDiccionarioDespachos.append({"Rut":rut})
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
                        print("Error, selecciona una de las opciones disponibles")
                diccionarioDespachos["Tipo de huevo"]=tipoDeHuevo
                listaDiccionarioDespachos.append({"Tipo de huevo":tipoDeHuevo})
                bandera2 = True
                print("")
                
                #ingreso de direccion
                direccion = input("Ingrese su direccion: ")
                diccionarioDespachos["Direccion"]=direccion
                listaDiccionarioDespachos.append({"Direccion":direccion})
                print("")
                
                #ingreso fecha de envio
                while bandera2 == True:
                    print("1.- Lunes")
                    print("2.- Martes")
                    print("3.- Miercoles")
                    print("4.- Jueves")
                    print("5.- Viernes")
                    print("6.- Sabado")
                    print("7.- Domingo")
                    diaEnvio = input("Ingrese una opcion para registrar el dia de envio: ")

                    if diaEnvio == "1":
                        diaEnvio = "Lunes"
                        bandera2 = False
                    elif diaEnvio == "2":
                        diaEnvio = "Martes"
                        bandera2 = False
                    elif diaEnvio == "3":
                        diaEnvio = "Miercoles"
                        bandera2 = False
                    elif diaEnvio == "4":
                        diaEnvio = "Jueves"
                        bandera2 = False
                    elif diaEnvio == "5":
                        diaEnvio = "Viernes"
                        bandera2 = False
                    elif diaEnvio == "6":
                        diaEnvio = "Sabado"
                        bandera2 = False
                    elif diaEnvio == "7":
                        diaEnvio = "Domingo"
                        bandera2 = False
                    else:
                        print("Error, ingrese una opcion valida")
                        print("")
                bandera2 = True
                print("")
                                
                while bandera2 == True:
                    numeroDiaEnvio = input("ingrese el numero del dia: ")
                    
                    if len(numeroDiaEnvio) < 3:
                        bandera2 = False
                    else:   
                        print("Error, debe ser un numero del 1 al 31")
                bandera2 = True
                print("")

                while bandera2 == True:
                    print("1.- Enero")
                    print("2.- Febrero")
                    print("3.- Marzo")
                    print("4.- Abril")
                    print("5.- Mayo")
                    print("6.- Junio")
                    print("7.- Julio")
                    print("8.- Agosto")
                    print("9.- Septiembre")
                    print("10.- Octubre")
                    print("11.- Noviembre")
                    print("12.- Diciembre")
                    mesEnvio = input("Ingrese una opcion para el mes de envio: ")
                    
                    if mesEnvio == "1":
                        mesEnvio = "Enero"
                        bandera2 = False
                    elif mesEnvio == "2":
                        mesEnvio = "Febrero"
                        bandera2 = False
                    elif mesEnvio == "3":
                        mesEnvio = "Marzo"
                        bandera2 = False
                    elif mesEnvio == "4":
                        mesEnvio = "Abril"
                        bandera2 = False
                    elif mesEnvio == "5":
                        mesEnvio = "Mayo"
                        bandera2 = False
                    elif mesEnvio == "6":
                        mesEnvio = "Junio"
                        bandera2 = False
                    elif mesEnvio == "7":
                        mesEnvio = "Julio"
                        bandera2 = False
                    elif mesEnvio == "8":
                        mesEnvio = "Agosto"
                        bandera2 = False
                    elif mesEnvio == "9":
                        mesEnvio = "Septiembre"
                        bandera2 = False
                    elif mesEnvio == "10":
                        mesEnvio = "Octubre"
                        bandera2 = False
                    elif mesEnvio == "11":
                        mesEnvio = "Noviembre"
                        bandera2 = False
                    elif mesEnvio == "12":
                        mesEnvio = "Diciembre"
                        bandera2 = False
                    else:
                        print("Error, ingrese una opcion valida")
                bandera2 = True          
                diccionarioDespachos["Fecha de envio"]=diaEnvio + " " + numeroDiaEnvio + " " + mesEnvio
                listaDiccionarioDespachos.append({"Fecha de envio":diaEnvio + " " + numeroDiaEnvio + " " + mesEnvio})
                print("")
                
                #ingreso de la cantidad de huevos
                while bandera2 == True:
                    cantidadHuevos = int(input("Ingrese la cantidad de huevos que desea enviar: "))
                    
                    if cantidadHuevos >= 50 and cantidadHuevos <= 10000:
                        bandera2 = False
                    else:
                        print("Error, la cantidad minima de envio es de 50 hasta un maximo de 10.000")
                diccionarioDespachos["Cantidad de huevos"]=cantidadHuevos
                listaDiccionarioDespachos.append({"Cantidad de huevos":cantidadHuevos})
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
                        diccionarioDespachos["Precio total"]=totalPrecioHuevos
                        listaDiccionarioDespachos.append({"Precio total":totalPrecioHuevos})
                        bandera2 = False
                    elif convenio == "no":
                        totalPrecioHuevos = cantidadHuevos * diccionarioHuevos[tipoDeHuevo]
                        diccionarioDespachos["Precio total"]=totalPrecioHuevos
                        listaDiccionarioDespachos.append({"Precio total":totalPrecioHuevos})
                        bandera2 = False
                    else:
                        print("Error, vuelva a ingresar la informacion")
                bandera2 = True
                listaDiccionarioDespachos.append("----------------------------")
                listaDiccionarioDespachos.append("----------------------------")
                opcion = None
                print("")
                
        #lista de huevos mas precios    
        elif opcion == "c":
            print(" Producto: Huevo de gallina")
            print("\t   Precio:$", diccionarioHuevos["huevos de gallina"])
            print("---------------------------------")
            print(" Producto: Huevo de pato")
            print("\t   Precio:$", diccionarioHuevos["huevos de pato"])
            print("---------------------------------")
            print(" producto: Huevo de codorniz")
            print("\t   Precio:$", diccionarioHuevos["huevos de codorniz"])
            print("---------------------------------")
            print(" Producto: Huevo de avestruz")
            print("\t   Precio:$", diccionarioHuevos["huevos de avestruz"])
            print("")
            opcion = None
       
        #lista de despachos guardados
        elif opcion == "d":
            for listdesp in listaDiccionarioDespachos:
                print(listdesp)
            opcion = None
            print("")       
            
        #cerrar aplicacion
        elif opcion == "e":
            opcion = None
            print("El programa se a cerrado")
            bandera = False
            break