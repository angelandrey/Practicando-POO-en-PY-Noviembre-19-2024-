class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        # Imprime el nombre completo
        print(f"{self.nombre} {self.apellido}")  # Usamos f-string para la concatenación

class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        # Llamamos al constructor de la clase base (Persona)
        super().__init__(nom, ape)
        self.carrera = carr

    def mostrar_carrera(self):
        # Muestra la carrera del estudiante
        print(f"Carrera: {self.carrera}")

# Ejemplo de uso:
estudiante = Estudiante("Andrey", "Muñoz", "Programacion")
estudiante.nombre_completo()  # Imprime el nombre completo
estudiante.mostrar_carrera()  # Imprime la carrera
