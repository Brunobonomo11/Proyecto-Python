#SOLICITAMOS AL USUARIO QUE INGRESE ALGUNOS DE SUS DATOS PARA PODER MOSTRARLOS EN CONSOLA

Usuario1 = "Matias"
Usuario2 = "Veronica"
Usuario3 = "Santiago"
Usuario4 = "Bruno"
Usuario5 = "Martin"
Espacio = " "

Apellido_Usuario1 = "Lopez"
Apellido_Usuario2 = "Gonzalez"
Apellido_Usuario3 = "Calo"
Apellido_Usuario4 = "Bonomo"
Apellido_Usuario5 = "Rivera"

Edad_Usuario1 = int(input(Usuario1 + " Introduzca su edad: "))
Edad_Usuario2 = int(input(Usuario2 + " Introduzca su edad: "))
Edad_Usuario3 = int(input(Usuario3 + " Introduzca su edad: "))
Edad_Usuario4 = int(input(Usuario4 + " Introduzca su edad: "))

Nombre_Completo_Usuario1 = (Usuario1 + Espacio + Apellido_Usuario1)
Nombre_Completo_Usuario2 = (Usuario2 + Espacio + Apellido_Usuario2)
Nombre_Completo_Usuario3 = (Usuario3 + Espacio + Apellido_Usuario3)
Nombre_Completo_Usuario4 = (Usuario4 + Espacio + Apellido_Usuario4)

print(Nombre_Completo_Usuario1)
print(Nombre_Completo_Usuario2)
print(Nombre_Completo_Usuario3)
print(Nombre_Completo_Usuario4)

Ciudad_Usuario1 = input(Usuario1 + " ¿En que ciudad reside actualmente: ")
Ciudad_Usuario2 = input(Usuario2 + " ¿En que ciudad reside actualmente: ")
Ciudad_Usuario3 = input(Usuario3 + " ¿En que ciudad reside actualmente: ")
Ciudad_Usuario4 = input(Usuario4 + " ¿En que ciudad reside actualmente: ")

Nombres_Usuarios_completa = ["Matias", "Veronica", "Santiago", "Bruno", "Martin", "Antonio", "Carla", "Camila", "Marcela"]
Nombres_Usuarios_completa.append("Enrique")
Nombres_Usuarios_completa.append("Delfina")

print(Nombres_Usuarios_completa)

CiudadesUsuarios = ("Palermo", "Caballito", "Recoleta", "Belgrano", "Lomas de Zamora", "Boedo", "Devoto", "Villa del Parque", "Microcentro")
print(CiudadesUsuarios)

Cantidad_de_Usuarios = 9
Cantidad_de_Usuarios += 2
print(Cantidad_de_Usuarios)

Nombres_Usuarios_completa.append("Roberto")
Nombres_Usuarios_completa.append("Claudia")

Nombres_Usuarios_completa.pop(5)
print(Nombres_Usuarios_completa)

Profesiones_Tuplas_Usuarios = ("Ingeniero", "Medico", "Bombero", "Policia", "Economista", "Psicologa", "Pediatra", "Cajero", "Vendedor")

Profesion_Usuario1 = input(Usuario1 + " ¿Cual es su profesion actualmente: ")
Profesion_Usuario2 = input(Usuario2 + " ¿Cual es su profesion actualmente: ")
Profesion_Usuario3 = input(Usuario3 + " ¿Cual es su profesion actualmente: ")
Profesion_Usuario4 = input(Usuario4 + " ¿Cual es su profesion actualmente: ")
Profesion_Usuario5 = input(Usuario5 + " ¿Cual es su profesion actualmente: ")

# A CADA USUARIO LE RESTAMOS $30.000 DE SU SUELDO QUE TIENE QUE APORTAR AL ESTADO

Sueldo_Usuario1 = (283000)
Sueldo_Usuario2 = (298000)
Sueldo_Usuario3 = (359000 - 30000)
Sueldo_Usuario4 = (409000 - 30000)
Sueldo_Usuario5 = (426000 - 30000)
print(Sueldo_Usuario1)
print(Sueldo_Usuario2)
print(Sueldo_Usuario3)
print(Sueldo_Usuario4)
print(Sueldo_Usuario5)

#INSERTAMOS UN CONDICIONAL PARA VER SI LOS SUELDOS PERTENCEN A LA LISTA EN DONDE EL ESTADO LES DESCUENTA $30.000 (USUARIOS QUE TIENEN SUELDOS ARRIBA DE $300.0000)

if Sueldo_Usuario1 > 300000:
  print("Usted ha aportado correctamente sus $30.000")
if Sueldo_Usuario1 < 300000:
  print("Usted no pertenece a la lista para aportar al estado")
else:
  print("Usted no ha ingresado su valor remunerativo")
  
  
if Sueldo_Usuario2 > 300000:
  print("Usted ha aportado correctamente sus $30.000")
if Sueldo_Usuario2 < 300000:
  print("Usted no pertenece a la lista para aportar al estado")
else:
  print("Usted no ha ingresado su valor remunerativo")
  

if Sueldo_Usuario3 > 300000:
  print("Usted ha aportado correctamente sus $30.000")
if Sueldo_Usuario3 < 300000:
  print("Usted no pertenece a la lista para aportar al estado")
else:
  print("Usted no ha ingresado su valor remunerativo")
  

if Sueldo_Usuario4 > 300000:
  print("Usted ha aportado correctamente sus $30.000")
if Sueldo_Usuario4 < 300000:
  print("Usted no pertenece a la lista para aportar al estado")
else:
  print("Usted no ha ingresado su valor remunerativo")

#SUMAMOS WHILE PARA SUMAR LA CANTIDAD DE USUARIOS

num = 1
while num > 0:
 print(f"{num}")
 num -=1
 print("Usuario Ingresado!")

# CREAMOS UN CONJUNTO CON LAS EMPRESAS EN LA QUE TRABAJA CADA USUARIO

Empresas_Usuarios = {"Coca Cola", "Serenisima", "Accenture", "Carrefour", "Rouge"}
Empresas_Usuarios.add("Perfumerie")
print(Empresas_Usuarios)

Edades_Usuarios = {"Matias": 26, "Veronica": 29, "Bruno" : 23, "Martin": 35, "Antonio": 45, "Carla":39}

Edades_Usuarios["Bruno"]

#AGREGAMOS UN NUEVO USUARIO CON SU RESPECTIVA EDAD AL DICCIONARIO

Edades_Usuarios["Cecilia"] = 37
print(Edades_Usuarios)

# AGREGAMOS ITEMS PARA CONOCER NOMBRES Y EDADES DE CADA USUARIO

Edades_Usuarios.items()
for clave, valor in Edades_Usuarios.items():
      print(clave, valor)


#DEFINIMOS FUNCIONES PARA SALUDAR AL USUARIO

def Saludamos_Al_Usuario(nombre):
  saludando = print("Hola", nombre, "¿Como estas?")
  return saludando

Saludamos_Al_Usuario("Bruno")

#DEFINIMOS FUNCIONES PARA SABER LOS AÑOS QUE TIENE DE ANTIGUEDAD CADA USUARIO EN LA EMPRESA

def Tiempo_En_Empresa_Usuario1(Actualidad,Inicio):
  return Actualidad - Inicio
Años_En_Empresa1 = Tiempo_En_Empresa_Usuario1(2024,2015)

print(Años_En_Empresa1)

def Tiempo_En_Empresa_Usuario2(Actualidad,Inicio):
  return Actualidad - Inicio
Años_En_Empresa2 = Tiempo_En_Empresa_Usuario2(2024,2010)

print(Años_En_Empresa2)

def Tiempo_En_Empresa_Usuario3(Actualidad,Inicio):
  return Actualidad - Inicio
Años_En_Empresa3 = Tiempo_En_Empresa_Usuario3(2024,2002)

print(Años_En_Empresa3)

def Tiempo_En_Empresa_Usuario4(Actualidad,Inicio):
  return Actualidad - Inicio
Años_En_Empresa4 = Tiempo_En_Empresa_Usuario4(2024,2019)

print(Años_En_Empresa4)

# Uso de *Args

def suma(*args):
  return sum(args)

suma(5, 5, 3)

#Agreamos Try-Except con ekse para sumar cantidad de usuarios

while (True):
  try:
    a = float(input("Introduzca su numero de usuario: "))
    b = float(input("Introduce otro numero de usuario: "))
    print(round(a + b))
  except:
      print("Ha ocurrido un error. Tienes que introducir 2 numeros. ")
  else:
        print("La suma se ha realizado correctamente")
        break
  finally:
    print("Fin del bucle")