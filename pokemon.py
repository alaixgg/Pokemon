
class ataque_Behavior:
    def attack(self, opponent):
        pass
#Se implementan las clases de los ataques
        
class Impactrueno(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Impactrueno!")
        opponent.reduce_health(20)

class Rayo (ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Rayo!")
        opponent.reduce_health(10)

class Ataque_Rapido(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Ataque Rapido!")
        opponent.reduce_health(10)

class Placaje(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Impactrueno!")
        opponent.reduce_health(10)

class Lanzallamas(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Lanzallamas !")
        opponent.reduce_health(10)

class Gruñido(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Gruñido !")
        opponent.reduce_health(10)

class Arañazo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Arañazo!")
        opponent.reduce_health(10)

class Ascuas(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Ascuas!")
        opponent.reduce_health(10)

class Placaje(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó placaje !")
        opponent.reduce_health(10)

class Burbuja(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Burbuja!")
        opponent.reduce_health(10)

class Rayo_Burbuja (ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Rayo Burbuja !")
        opponent.reduce_health(10)
    
class Drenadoras(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Drenadoras!")
        opponent.reduce_health(10)

class Tacleada(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Tacleada !")
        opponent.reduce_health(10)

class Supersonico(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Supersonico !")
        opponent.reduce_health(10)

class Picotazo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Picotazo!")
        opponent.reduce_health(10)

class Remolino(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Remolino!")
        opponent.reduce_health(10)
    
class Tornado(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Tornado !")
        opponent.reduce_health(10)

class Latigo_Cepa(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Latigo Cepa!")
        opponent.reduce_health(10)
    
class Somnifero(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Somnifero !")
        opponent.reduce_health(10)

class Pistola_agua(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Pistola de agua!")
        opponent.reduce_health(10)

class Hidropulso(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Hidropulso !")
        opponent.reduce_health(10)
    
class Tajo_Cruzado(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Tajo Cruzado !")
        opponent.reduce_health(10)

class Hipercolmillo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Hipercolmillo !")
        opponent.reduce_health(10)

class Golpe_Cabeza(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Golpe cabeza !")
        opponent.reduce_health(10)
    
class Lodo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Uso Lodo !")
        opponent.reduce_health(10)

class Golpe_cabeza (ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó golpe Cabeza!")
        opponent.reduce_health(10)

class lodo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó lodo!")
        opponent.reduce_health(10)

class Bomba_lodo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Bomba Lodo!")
        opponent.reduce_health(10) 

class Ataque_acido(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Ataque Acido !")
        opponent.reduce_health(10)

class Infortunio(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Infortunio !")
        opponent.reduce_health(10)
        
"""class (ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó  !")
        opponent.reduce_health(10)  """

#Clase base de pokemons
        

class Pokemon:
    def __init__(self, nombre, salud, ataque_Behavior):
        self.nombre = nombre
        self.salud = salud
        self.ataque_Behavior = ataque_Behavior

    def attack(self, ataque, opponent):    
        if ataque in self.ataques:
            self.ataques[ataque].attack(opponent)
        else:
            print(f"{self.nombre} no conoce el ataque {ataque}.")

    def reduce_health(self, cantidad):
        self.health -= cantidad
        print(f"{self.name} ha perdido {cantidad} puntos de salud. Salud restante: {self.salud}")


#Clases de pokemons
        
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 100)
        self.ataques = {
            "Impactrueno": Impactrueno(),
            "Rayo": Rayo(),
            "Ataque Rápido": Ataque_Rapido(),
            "Placaje": Placaje()
        }

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__("Caterpie", 100)
        self.ataques = {
            "Placaje": Placaje(),
            "Tacleada": Tacleada(),
            "Supersónico": Supersonico(),
            "Drenadoras": Drenadoras()
        }

class Pidgeotto(Pokemon):
    def __init__(self):
        super().__init__("Pidgeotto", 100)
        self.ataques = {
            "Picotazo": Picotazo(),
            "Remolino": Remolino(),
            "Tornado": Tornado(),
            "Ataque Rápido": Ataque_Rapido()
        }


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 100)
        self.ataques = {
            "Látigo Cepa": Latigo_Cepa(),
            "Drenadoras": Drenadoras(),
            "Placaje": Placaje(),
            "Somnífero": Somnifero()
        }

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 100)
        self.ataques = {
            "Lanzallamas": Lanzallamas(),
            "Gruñido": Gruñido(),
            "Arañazo": Arañazo(),
            "Ascuas": Ascuas()
        }

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 100)
        self.ataques = {
            "Pistola Agua": Pistola_agua(),
            "Burbuja": Burbuja(),
            "Ataque Rápido": Ataque_Rapido(),
            "Placaje": Placaje()
        }

class Krabby(Pokemon):
    def __init__(self):
        super().__init__("Krabby", 100)
        self.ataques = {
            "Burbuja": Burbuja(),
            "Rayo Burbuja": Rayo_Burbuja(),
            "Placaje": Placaje(),
            "Tajo Cruzado": Tajo_Cruzado()
        }

class Raticate(Pokemon):
    def __init__(self):
        super().__init__("Raticate", 100)
        self.ataques = {
            "Hipercolmillo": Hipercolmillo(),
            "Ataque Rápido": Ataque_Rapido(),
            "Placaje": Placaje(),
            "Golpe Cabeza": Golpe_Cabeza()
        }

class Muk(Pokemon):
    def __init__(self):
        super().__init__("Muk", 100)
        self.ataques = {
            "Lodo": Lodo(),
            "Bomba Lodo": Bomba_lodo(),
            "Ataque Ácido": Ataque_acido(),
            "Infortunio": Infortunio()
        }

class Kingler(Pokemon):
    def __init__(self):
        super().__init__("Kingler", 100)
        self.ataques = {
            "Hidropulso": Hidropulso(),
            "Rayo Burbuja": Rayo_Burbuja(),
            "Rayo": Rayo(),
            "Placaje": Placaje()
        }

"""class (Pokemon):
    def __init__(self):
        super().__init__("",0 , ataque_Behavior) """
    



if __name__ == "__main__":
    pass