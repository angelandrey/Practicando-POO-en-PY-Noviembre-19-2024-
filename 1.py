class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        # Corrected f-string formatting
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultados(self):
        # Corrected print statements with quotes
        if self.nota >= 7:
            print("Has APROBADO!")
        else:
            print("Has REPROBADO!")

# Corrected string literals for names
estudiante1 = Estudiante("Andrey", 10)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Tito", 5)
estudiante2.imprimir()
estudiante2.resultados()
