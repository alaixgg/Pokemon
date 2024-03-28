
class ataque_Behavior:
    def attack(self):
        pass
#Se implementan las clases de los ataques
class Tackle(ataque):
    def attack(self):
        print("¡Usó Tackle!")


class Pokemon:
    def __init__(self, nombre, salud, ataque_Behavior):
        self.nombre = nombre
        self.salud = salud
        self.ataque_Behavior = ataque_Behavior

    
    
    



if __name__ == "__main__":
    pass