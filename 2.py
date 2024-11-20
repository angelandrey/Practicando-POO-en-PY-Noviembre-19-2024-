class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 0.5

# Requesting user input for name and age
p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))

# Calling cumpleaños() twice
p.cumpleaños()
p.cumpleaños()

# Printing the result
print(f"{p.nombre} cumple {p.edad} años")
