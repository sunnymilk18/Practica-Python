from datetime import datetime

#autentificacion de usuario y contraseña
def login():

	usuario = "admin"
	contrasenia = "123"
	contador = 0
	intentos = 3
	while contador < intentos:
		userName = input("Ingrese su nombre de usuario: ")
		password = input("Ingrese su contraseña: ")
		if userName.lower() == usuario and password == contrasenia:
			userVerified = {"verificado":True}
			return userVerified
		else:
			print("\nError en su usuario o contraseña\n")
			contador += 1
	userVerified = {"verificado":False, "mensaje":"A alcanzado el numero maximo de intentos"}
	return userVerified

#Menu principal
def menu_Principal():
	global idDespacho
	global busqueda

	while True:
		print("""
+-----------------------------------------------------+                                                     
|      Distribuidora de huevos mayorista All Eggs     |
|                        S.A                          |
+-----------------------------------------------------+""")
		print("1.- Asignacion de precios de huevos")
		print("2.- Crear despacho")
		print("3.- Listar huevos")
		print("4.- Listar despachos")
		print("5.- Salir del programa")
		opcion = input("ingrese la opcion que desea realizar ")
		print("")
		if opcion == "1":
			asignacion_Precio_Huevos()
		elif opcion == "2":
			crear_Despachos()
			idDespacho += 1
		elif opcion == "3":
			listar_Huevos()
			print("")
		elif opcion == "4":
			while True:
				print("1.- Buscar despacho por fecha")
				print("2.- Buscar despacho por rut")
				print("3.- Listar todos los despachos")
				print("4.- Volver al menu anterior")
				mostrarDespacho = input("Ingrese la opcion que desea realizar: ")
				if mostrarDespacho == "1":
					busqueda = input("Ingrese la fecha que desea buscar: ")
					listar_Despacho_Fecha_Rut()
				elif mostrarDespacho == "2":
					busqueda = input("Ingrese la fecha que desea buscar: ")
					listar_Despacho_Fecha_Rut()
				elif mostrarDespacho == "3":
					listar_Despachos()
				elif mostrarDespacho == "4":
					break
				else:
					print("\nError, ingrese una opcion valida\n")
		elif opcion == "5":
			salirPrograma = input("Si desea salir del programa escriba SI, caso contrario escriba NO: ")
			if salirPrograma.lower() == "si":
				break
			elif salirPrograma.lower() == "no":
				pass
			else:
				print("\nError, ingreso de datos incorrecto, se a vuelto al menu principal")			
		else:
			print("Error, ingrese nuevamente una opcion")

#modificacion de precios a los huevos
def asignacion_Precio_Huevos():
	while True:
		try:
			print("")
			print("1.- Asignar precio a huevos de Gallina")
			print("2.- Asignar precio a huevos de Pato")
			print("3.- Asignar precio a huevos de Codorniz")
			print("4.- Asignar precio a huevos de Avestruz")
			print("5.- Volver al menu anterior")
			asignarPrecio = input("Ingrese la opcion a la que desea modificar el precio: ")
			print("")
			if asignarPrecio == "1":
				valorHuevo = int(input("ingrese el nuevo valor: "))
				while valorHuevo < 50:
					print("El valor no puede ser menor a $50, porfavor ingrese un valor nuevamente:")
					valorHuevo = int(input("ingrese el nuevo valor: "))
					print("")
				huevos[0][1]=valorHuevo
			elif asignarPrecio == "2":
				valorHuevo = int(input("Ingrese el nuevo valor: "))
				while valorHuevo < 150:
					print("El valor no puede ser menor a $150, porfavor ingrese un valor nuevamente")
					valorHuevo = int(input("ingrese el nuevo valor: "))
					print("")
				huevos[1][1]=valorHuevo
			elif asignarPrecio == "3":
				valorHuevo = int(input("Ingrese el nuevo valor: "))
				while valorHuevo < 50:
					print("El valor no puede ser menor a $50, porfavor ingrese un valor nuevamente")
					valorHuevo = int(input("ingrese el nuevo valor: "))
					print("")
				huevos[2][1]=valorHuevo
			elif asignarPrecio == "4":
				valorHuevo = int(input("Ingrese el nuevo valor: "))
				while valorHuevo < 800:
					print("El valor no puede ser menor a $800, porfavor ingrese un valor nuevamente")
					valorHuevo = int(input("ingrese el nuevo valor: "))
					print("")
				huevos[3][1]=valorHuevo
			elif asignarPrecio == "5":
				asignarPrecio = None
				break
			else:
				print("Error, ingrese una opcion valida")
			print("")
			print("El precio se a modificado satisfactoriamente")
		except:
			print("Se a detectado una anomalia en el cambio de precios, se a vuelto al menu anterior")
			print("")

#creacion de despachos
def crear_Despachos():
	
	id = idDespacho
	while True:
		nombre = input("Ingrese su nombre o razon social: ")
		if len(nombre) == 0:
			print("Error, ingrese nuevamente su nombre")
		else:
			print("")
			break
	while True:
		rut = input("Ingrese su rut (No utilize puntos ni guion, ejemplo: 01234567): ")
		if len(rut) != 8 and len(rut) != 9:
			print("Error, ingrese nuevamente su rut")
		else:
			print("")
			break
	while True:
		direccion = input("Ingrese su direccion: ")
		if len(direccion) == 0:
			print("Error, ingrese nuevamente su direccion")
		else:
			print("")
			break
	while True:
		try:
			fecha = input("Ingrese la fecha de envio en el formato (DD-MM-YYYY): ")
			datetime.strptime(fecha, '%d-%m-%Y')
			print("")
			break
		except:
			print("Fecha invalida, ingrese nuevamente la fecha")
	while True:
		print("1.- Huevos de gallina")
		print("2.- Huevos de pato")
		print("3.- Huevos de codorniz")
		print("4.- Huevos de avestruz")
		tipoDeHuevo = input("ingrese el tipo de huevo: ")
		if tipoDeHuevo == "1":
			tipoDeHuevo = "huevos de gallina"
			indiceHuevos = 0
			valorHuevos = 1
			break
		if tipoDeHuevo == "2":
			tipoDeHuevo = "huevos de pato"
			indiceHuevos = 1
			valorHuevos = 1
			break
		if tipoDeHuevo == "3":
			tipoDeHuevo = "huevos de codorniz"
			indiceHuevos = 2
			valorHuevos = 1
			break
		if tipoDeHuevo == "4":
			tipoDeHuevo = "huevos de avestruz"
			indiceHuevos = 3
			valorHuevos = 1
			break
		else:
			print("Error, ingrese una opcion valida")
			print("")
	print("")
	precioUnitario = huevos[indiceHuevos][valorHuevos]
	while True:
		try:
			cantidadHuevos = int(input("Ingrese la cantidad de huevos que desea enviar: "))
			if cantidadHuevos >= 50 and cantidadHuevos <= 10000:
				break
			else:
				print("Error, la cantidad minima de envio es de 50 hasta un maximo de 10.000")
		except:
			print("Error, ingrese nuevamente un valor")
	while True:
		descuento = input("¿Tiene convenio?, escriba 'si' en caso de tener, caso contrario escriba 'no': ")
		if descuento == "si":
			precioTotal = cantidadHuevos * huevos[indiceHuevos][valorHuevos]
			descuento = (cantidadHuevos * huevos[indiceHuevos][valorHuevos]) * 0.1
			precioTotal = precioTotal - descuento
			break
		elif descuento == "no":
			precioTotal = cantidadHuevos * huevos[indiceHuevos][valorHuevos]
			descuento = 0
			break
		else:
			print("Error, ingrese nuevamente la informacion")
	print("")
	print("+----------------------------------+")
	print("|Despacho creado satisfactoriamente|")
	print("+----------------------------------+")
	print("")
	
	despachos[id]=nombre,rut,direccion,fecha,tipoDeHuevo,precioUnitario,cantidadHuevos,descuento,precioTotal

#lista de huevos con sus precios
def listar_Huevos():

	print(
"""
+-----------------------------------------------------+                                                     
|      Distribuidora de huevos mayorista All Eggs     |
|                        S.A                          |
+-----------------------------------------------------+	""")
	for huevo in huevos:
		print(
f"""|                                                     |
|Producto  :  {huevo[0]:<21}                   |
|Precio    :  ${huevo[1]:<21}                  |
+-----------------------------------------------------+""")

#lista de despachos con busqueda por fecha o rut
def listar_Despacho_Fecha_Rut():

	for k,v in despachos.items():
		if busqueda == v[3] or busqueda == v[1]:
			print(
			f"""
+-----------------------------------------------------+                                                     
|      Distribuidora de huevos mayorista All Eggs     |
|                        S.A                          |
+-----------------------------------------------------+			
|  ID                      : {k:<21}    {"|":<25}
|  Nombre o razon social   : {v[0]:<21}    {"|":<25}
|  Rut                     : {v[1]:<21}    {"|":<25}
|  Direccion               : {v[2]:<21}    {"|":<25}
|  Fecha de envio          : {v[3]:<21}    {"|":<25}
+-----------------------------------------------------+
|  Tipo de huevo           : {v[4]:<21}    {"|":<25}
|  Precio unitario         : {v[5]:<21}    {"|":<25}
|  Cantidad de huevos      : {v[6]:<21}    {"|":<25}
|  Descuento               : {v[7]:<21}    {"|":<25}
+-------------------+---------------------------------+
                    |  {"Precio Total":<10} :{v[8]:>11}      |
                    +---------------------------------+""")
	print("")

#listar la totalidad de los despachos creados
def listar_Despachos():

	for k,v in despachos.items():
		print(
			f"""
+-----------------------------------------------------------------------+                                                     
|           Distribuidora de huevos mayorista All Eggs                  |
|                             S.A                                       |
+-----------------------------------------------------------------------+			
|  ID                      : {k:>42} |                                   
|  Nombre o razon social   : {v[0]:>42} |
|  Rut                     : {v[1]:>42} |                             
|  Direccion               : {v[2]:>42} |                              
|  Fecha de envio          : {v[3]:>42} |                              
+-----------------------------------------------------------------------+
|  Tipo de huevo           : {v[4]:>42} |                      
|  Precio unitario         : {v[5]:>42} |                     
|  Cantidad de huevos      : {v[6]:>42} |                     
|  Descuento               : {v[7]:>42} |                     
+-------------------+---------------------------------------------------+
                    |  {"Precio Total":<10} :{v[8]:>25}          |
                    +---------------------------------------------------+""")
	print("")

despachos = {}
huevos = [["huevos de gallina", 50], ["huevos de pato", 150], ["huevos de codorniz", 50], ["huevos de avestruz", 800]]
idDespacho = 1000000

iniciar = login()
if iniciar["verificado"]:
	menu_Principal()	
else:
	print(iniciar["mensaje"])
	print("El programa se a cerrado")
