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