class Universidad:
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carerra:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carerra):
    def __init__(self, Nombre, nombre, edad):
        # Initialize both parent classes
        Universidad.__init__(self, Nombre)
        self.nombre = nombre
        self.edad = edad
    
    def datos(self):
        # Printing the details of the student
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")

# Crear un objeto Estudiante
persona = Estudiante("Harvard", "Andrey", 16)
persona.carrera("Programación")  # Establecer la especialidad de programación
persona.datos()  # Mostrar los datos del estudiante
