# Imprimimos nuestro nombre apellido y fecha de nacimiento

print("Bruno")
print("Bonomo")
print("11 de octubre 2000")

# Mostrar cadena con un solo print con comillas triples

# print("""Bruno
# Bonomo
# 11 de octubre 2000""")


# Armamos variables con nuestros datos y luego imprimimos

Nombre = "Bruno"
Apellido = "Bonomo"
Espacio = " "
Fecha_de_Nacimiento = "11 de octubre de 2000"
Edad = 23
Año_de_Nacimiento = "2000"

NombreCompleto = (Nombre + Espacio + Apellido)
print(NombreCompleto)


#Solicitamos al usuario que ingrese su nombre, apellido y edad

UserNombreApellido = input("Ingresa tu nombre y apellido")
UserEdad = int(input("Ingrese su edad"))

#Longitud de string de nuestra variable Fecha_de_Nacimiento


#len(Fecha_de_Nacimiento)

Lista_edades_Users = [18, 22, 25, 28, 32, 35, 40, 42, 46]
NombresUsers = ["Juan", "Martin", "Bruno", "Matias", "Santiago", "Ezequiel"]

#Eliminamos Users que ya no necesitamos

#NombresUsers[:2] = []
#print(NombresUsers)


#Agregamos nuevos nombres de usuario a la lista

NombresUsers.append("Pablo")
NombresUsers.append("Cecilia")
print(NombresUsers)

#Longitud de la lista

#len(Lista_edades_Users)


#Buscamos nuestro item en la lista para saber en que indice se encuentra

Lista_edades_Users.index(35)


#Agregamos tupla de datos con ciudades de nuestros usuarios

CiudadesUsers = ("Buenos Aires", "Palermo", "Caballito", "Recoleta", "Belgrano", "Lomas de Zamora")
print(CiudadesUsers)


#Pedimos al usuario que ingrese su ciudad donde reside

CiudadUser = input("¿En que ciudad vivis actualmente?")

#Convertimos la lista de nombres de usuarios en una tupla

#tuple(NombresUsers)

# Igualdad    Nombre == ("Bruno")


#Cantidad de usuarios, incrementamos +1 a medida que se van sumando

CantidadUsers = 6
CantidadUsers += 1
print(CantidadUsers)


#Insertamos un condicional para ver si los usuarios son mayores de 18 años

edad = int(input("Ingrese su edad para continuar"))
if edad >= 18:
  print("Es un adulto")
if edad <= 18:
  print("No es un adulto")
elif edad <= 15:
  print("Debe ingresar una edad para continuar")
if True:
  print("Cumple con los requisitos")
else:
  print("No cumple con los requisitos establecidos")


# Sumamos While para contar la cantidad de usuarios

num = 1
while num > 0:
 print(f"{num}")
 num -=1
 print("Usuario Ingresado!")

#Ingresos = 1
#while Ingresos <= 3:
# txt = input("Ingrese numero de usuario: ")
#  if txt == "1":
#    print("Usuario Ingresado", Ingresos)
#    break
#    Ingresos +=1
#  else:
#    print("Has agotado tus tres intentos")

# Sentencia For

#for valor in Lista_edades_Users:
#  print("Soy un item de la lista")

#Recorremos Nombres de usuario con un For

#for letra in NombresUsers:
#  print(letra)


# Creamos un conjunto

ConjuntoDeportes = {"Futbol", "Tenis", "Basquet", "Handball", "Atletismo"}
ConjuntoDeportes.add("Voley")
print(ConjuntoDeportes)

# Agregamos un SET

#mi_lista = list({1,2,3,4})
#mi_set = set(mi_lista)
#print(type(mi_set))

#Agregamos Diccionarios

# colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
# type(colores)

# EDADES USERS CON DICCIONARIOS [18, 22, 25, 28, 32, 35, 40, 42, 46]
# ["Juan", "Martin", "Bruno", "Matias", "Santiago", "Ezequiel"]

edades = {"Juan": 18, "Martin": 22, "Bruno" : 25, "Matias": 28, "Santiago": 32, "Ezequiel":35}


#Edad de un usuario en especifico en este caso Bruno

edades["Bruno"]


#Agregamos usuario y edad al diccionario

edades["Cecilia"] = 37
print(edades)


# Agregamos Insert para insertar una edad en un indice en especifico

Lista_edades_Users.insert(-1,44)
print(Lista_edades_Users)


# Agregamos get y Keys (Traer todas las claves del diccionario)

edades.get("Manuel", "no hay clave Manuel")
edades.keys()


# Agregamos Items

edades.items()
for clave, valor in edades.items():
      print(clave, valor)


#Definimos funciones

def saludar_con_nombre(nombre):
  saludando = print("Hola, nombre, ¿Cómo estás?")
  return saludando

saludar_con_nombre("Bruno")

# Uso de *Args

#def suma(*args):
# s = 0
#  for arg in args:
#      s += arg
#      return s

#suma(1, 3, 4, 2)

#float
#float(25)
#str(2.5)
#redondear un numero decimal round(2.6) // Devuelve 3 es el mas cercano


#Agreamos Try-Except con ekse para sumar cantidad de usuarios

while (True):
  try:
    a = float(input("Introduce un numero de usuario: "))
    b = float(input("Introduce otro numero de usuario: "))
    print(round(a + b))
  except:
      print("Ha ocurrido un error. Tienes que introducir 2 numeros. ")
  else:
        print("La suma se ha realizado correctamente")
        break
  finally:
    print("Fin del bucle")
    

#estudiante1_nombre = "Bruno"
#estudiante1_apellido = "Bonomo"
#estudiante1_ciudad = "Buenos Aires"

#La palabra class me permite crear clases
class Estudiante:

  #doble guion bajo init doble guin bajo __init__
  #funcion inicializadora (constructora) --- permite añadir argumentos para las caracteristicas
  def __init__(self, nombre, apellido, ciudad):
    self.nombre = nombre
    self.apellido = apellido
    self.ciudad = ciudad
    self.curso = "Python"  #variable local !!

    def asistir(self):
      print(f"La estudiante {self.mi_nombre} ha asistido a clase de {self.curso}! ")
      
est1 = Estudiante(nombre="Bruno", apellido="Bonomo", ciudad="Buenos Aires") #creando el objeto estudiante1 a partir de la clase Estudiante
estudiante2 = Estudiante("Santigo", "Lopez", "Baranquilla")
estudiante3 = Estudiante("Lucas", "Rojas", "Montevideo")

print(est1.nombre)

nombre1 = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su apellido: ")
ciudad1 = input("Ingrese su ciudad: ")

est4 = Estudiante(nombre1, apellido1, ciudad1)


class Libro:

  def __init__(self, titulo, autor, cant_pags):
    self.titulo = titulo
    self.autor = autor
    self.cant_pags = cant_pags

  def obtener_info(self):
    print(f"Título: {self.titulo} --- Autor: {self.autor} --- Cantidad de Páginas: {self.cant_pags}")

harry_potter_1 = Libro("Harry Potter y la Piedra Filosofal", "J.K.Rowling", 288)
harry_potter_1.obtener_info()

tlor_1 = Libro("El señor de los anillos - La comunidad del anillo", "J.R..R.Tolkien", 576)
tlor_1.obtener_info()

class Animal:

  #Iniciamos los atributos
  def __init__(self, especie, edad):
    self.especie = especie
    self.edad = edad

  #Creamos los 3 metodos
  def hablar(self):
    pass

  def moverse(self):
    pass

  def describime(self):
    return f"Soy un animal del tipo {type(self).__name__}"

animal1 = Animal("Felino", 3)

animal1.describime()

class Perro(Animal):
  pass

snoopy = Perro("Canino", 5)

snoopy.describime()