'''
Requerimientos obligatorios 
Datos de entrada 
El sistema deberá solicitar: 
El ingreso de un mínimo de 10 datos de entrada. De los cuales: 
Numéricos (5 mínimo). Ejemplos: 
Uso de CPU (%) 
Uso de memoria RAM (%) 
Espacio libre en disco (GB) 
Cantidad de usuarios conectados 
Cantidad de procesos activos 
Categóricos (3 mínimo). Opciones cerradas. Ejemplos: 
Sistema operativo (Linux / Windows Server) 
Estado del firewall (Activo / Inactivo) 
Tipo de servidor (Web / Base de datos / Archivos) 
Cadenas (2 mínimo) Ejemplos: 
Nombre del servidor 
Nombre del administrador responsable 
10 INPUTS: Numéricos 5, Categóricos 3 y Cadenas 2 
VALIDACIONES de ingreso: solo números, coincidencia de opciones  y mínimo un espacio ¿?
'''
#validar que se ingresen numeros
uso_cpu = int(input("Ingrese cuanto es el uso de su CPU (%) "))
uso_ram = float(input("Ingrese cuanto es el de memoria RAM (%) "))
espacio_libre_disco = float(input("Ingrese cuanto Espacio libre hay en el disco (GB) "))
usuarios_conectados  = int(input("Ingrese Cantidad de usuarios conectados "))
cantidad_procesos_activos = int(input("Ingrese Cantidad de Cantidad de procesos activos "))
#validar que se seleccionen las opciones
sistema_operativo = input("Seleccione su sistema operativo (Linux / Windows Server) ")
estado_firewall = input("Estado del firewall (Activo / Inactivo) ")
tipo_servidor = input("Seleccione su tipo de servidor (Web / Base de datos / Archivos) ")
#validar cadena 
nombre_servidor = input("Ingrese nombre del servidor ")
nombre_administrador = input("Ingrese nombre del administrador responsable ")