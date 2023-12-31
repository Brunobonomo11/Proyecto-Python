class Usuario1:

  def __init__(self, nombre, apellido, ciudad):
    self.nombre = nombre
    self.apellido = apellido
    self.ciudad = ciudad

    def Ingresado(self):
      print(f"El usuario {self.mi_nombre} ha ingresado su nombre de usuario {self.apellido}! ")
      
User1 = Usuario1(nombre="Bruno", apellido="Bonomo", ciudad="Buenos Aires") #creando el objeto estudiante1 a partir de la clase Estudiante
User2 = Usuario1("Santigo", "Lopez", "Baranquilla")
User3 = Usuario1("Lucas", "Rojas", "Montevideo")

print(User1.nombre)

nombre1 = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su apellido: ")
ciudad1 = input("Ingrese su ciudad: ")

est4 = Usuario1(nombre1, apellido1, ciudad1)


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