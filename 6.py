class Marino:
    def hablar(self):
        print("Hola soy un animal marino!")

class Pulpo(Marino):
    def hablar(self):
        print("Hola soy un pulpo!")

class Foca(Marino):
    def hablar(self, mensaje=None):
        # If no message is provided, use the default behavior
        if mensaje:
            print(mensaje)
        else:
            print("Hola soy una foca!")

# Create instances and call their hablar methods
marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola soy una foca!")
