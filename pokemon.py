import random
import time 

class ataque_Behavior:
    def attack(self):
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
        self.ataque = ataque_Behavior

    def attack(self, ataque, opponent):    
        if ataque in self.ataque:
            self.ataque[ataque].attack(opponent)
        else:
            print(f"{self.nombre} no conoce el ataque {ataque}.")

    def reduce_salud(self, cantidad):
        self.salud -= cantidad
        print(f"{self.nombre} ha perdido {cantidad} puntos de salud. Salud restante: {self.salud}")


#Clases de pokemons
        
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 100, ataque_Behavior())  
        self.ataques = {
            "Impactrueno": Impactrueno(),
            "Rayo": Rayo(),
            "Ataque Rápido": Ataque_Rapido(),
            "Placaje": Placaje()
        }

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__("Caterpie", 100, ataque_Behavior())
        self.ataques = {
            "Placaje": Placaje(),
            "Tacleada": Tacleada(),
            "Supersónico": Supersonico(),
            "Drenadoras": Drenadoras()
        }

class Pidgeotto(Pokemon):
    def __init__(self):
        super().__init__("Pidgeotto", 100, ataque_Behavior())
        self.ataques = {
            "Picotazo": Picotazo(),
            "Remolino": Remolino(),
            "Tornado": Tornado(),
            "Ataque Rápido": Ataque_Rapido()
        }

# Repite el mismo patrón para el resto de las clases de Pokémon...

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 100, ataque_Behavior())
        self.ataques = {
            "Látigo Cepa": Latigo_Cepa(),
            "Drenadoras": Drenadoras(),
            "Placaje": Placaje(),
            "Somnífero": Somnifero()
        }

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 100, ataque_Behavior())
        self.ataques = {
            "Lanzallamas": Lanzallamas(),
            "Gruñido": Gruñido(),
            "Arañazo": Arañazo(),
            "Ascuas": Ascuas()
        }

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 100, ataque_Behavior())
        self.ataques = {
            "Pistola Agua": Pistola_agua(),
            "Burbuja": Burbuja(),
            "Ataque Rápido": Ataque_Rapido(),
            "Placaje": Placaje()
        }

class Krabby(Pokemon):
    def __init__(self):
        super().__init__("Krabby", 100, ataque_Behavior())
        self.ataques = {
            "Burbuja": Burbuja(),
            "Rayo Burbuja": Rayo_Burbuja(),
            "Placaje": Placaje(),
            "Tajo Cruzado": Tajo_Cruzado()
        }

class Raticate(Pokemon):
    def __init__(self):
        super().__init__("Raticate", 100, ataque_Behavior())
        self.ataques = {
            "Hipercolmillo": Hipercolmillo(),
            "Ataque Rápido": Ataque_Rapido(),
            "Placaje": Placaje(),
            "Golpe Cabeza": Golpe_Cabeza()
        }

class Muk(Pokemon):
    def __init__(self):
        super().__init__("Muk", 100, ataque_Behavior)
        self.ataques = {
            "Lodo": Lodo(),
            "Bomba Lodo": Bomba_lodo(),
            "Ataque Ácido": Ataque_acido(),
            "Infortunio": Infortunio()
        }

class Kingler(Pokemon):
    def __init__(self):
        super().__init__("Kingler", 100, ataque_Behavior)
        self.ataques = {
            "Hidropulso": Hidropulso(),
            "Rayo Burbuja": Rayo_Burbuja(),
            "Rayo": Rayo(),
            "Placaje": Placaje()
        }

"""class (Pokemon):
    def __init__(self):
        super().__init__("",0 , ataque_Behavior) """

#     
def seleccionar_pokemon():
    pokemones_seleccionados = []
    print("Elige un Pokémon:")
    print("1. Pikachu")
    print("2. Caterpie")
    print("3. Pidgeotto")
    print("4. Bulbasaur")
    print("5. Charmander")
    print("6. Squirtle")
    print("7. Krabby")
    print("8. Raticate")
    print("9. Muk")
    print("10. Kingler")
    eleccion_pokemon = input("Ingresa un Pokémon: ")

    if eleccion_pokemon == "1":
        return Pikachu()
    elif eleccion_pokemon == "2":
        return Caterpie()
    elif eleccion_pokemon == "3":
        return Pidgeotto()
    elif eleccion_pokemon == "4":
        return Bulbasaur()
    elif eleccion_pokemon == "5":
        return Charmander()
    elif eleccion_pokemon == "6":
        return Squirtle()
    elif eleccion_pokemon == "7":
        return Krabby()
    elif eleccion_pokemon == "8":
        return Raticate()
    elif eleccion_pokemon == "9":
        return Muk()
    elif eleccion_pokemon == "10":
        return Kingler()
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 10.")

    return pokemones_seleccionados

#Jugador & Maquina
class Dos_Jugadores:
    def __init__(self):
        self.pokemon_seleccionados_jugador1 = []
        self.pokemon_seleccionados_jugador2 = []

        print("***MODO DE JUEGO:*** \n VS 2 Entrenadores\n\n")

        #Eleccion de Pokemons
        print("¡Entrenador 1, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_jugador1 = []
        contador = 0
        while contador != 3:
            contador +=1
            pokemon_seleccionado = seleccionar_pokemon()
            self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
        print("El entrenador 1 ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador1])

        print("¡Entrenador 2, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_jugador2 = []
        contador = 0
        while contador != 3:
            contador +=1
            pokemon_seleccionado = seleccionar_pokemon()
            self.pokemon_seleccionados_jugador2.append(pokemon_seleccionado)
        print("El entrenador 2 ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador2])   
   

    
    def ejecutar(self):
        pass

class Maquina:
   def __init__(self):
        self.pokemon_seleccionados_jugador1 = []
        self.pokemon_seleccionados_maquina = []
        
        print("***MODO DE JUEGO:*** \nJugar contra un Botsito\n\n")

        #Eleccion de Pokemons
        print("¡Entrenador, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_jugador1 = []
        contador = 0
        while contador != 3:
            contador +=1
            pokemon_seleccionado = seleccionar_pokemon()
            self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
        print("El entrenador ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador1])   

        
        print("¡Botsito Rocket, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_maquina = []
        time.sleep(1)
        print("Botsito Rocket, está escogiendo sus pokemones...")
        while len(self.pokemon_seleccionados_maquina) < 3:
            pokemon_seleccionado = random.choice([Pikachu(), Squirtle(), Bulbasaur(), Charmander(), Caterpie(), Pidgeotto(), Krabby(), Raticate(), Muk(), Kingler()])
            self.pokemon_seleccionados_maquina.append(pokemon_seleccionado)
        time.sleep(2)
        print("El Botsito Rocket ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_maquina])   
        
    
   def ejecutar(self):
        print("¡Comienza el juego!")
        while not self.hay_ganador():
            self.turno_jugador()
            if self.hay_ganador():
                break
            self.turno_maquina()
        print("¡Fin del juego!")

   def turno_jugador(self):
        
        print("¡Es tu turno!")
        # Aquí deberías implementar la lógica del turno, como seleccionar un ataque, realizar el ataque, etc.

   def turno_maquina(self):
        # Lógica del turno de la máquina
        print("Turno de la máquina")
        # Aquí deberías implementar la lógica del turno de la máquina, como seleccionar un ataque aleatorio, realizar el ataque, etc.

   def hay_ganador(self):
        # Lógica para determinar si hay un ganador
        # Por ejemplo, si alguno de los jugadores se queda sin Pokémon, el otro jugador es el ganador
        return len(self.pokemon_seleccionados_jugador1) == 0 or len(self.pokemon_seleccionados_maquina) == 0


    #Funcion de seleccion del modo de juego
class juego:
    def __init__(self):
        self.modo_juego = None

    def seleccionar_modo_juego(self):
        eleccion_modo_juego = input("SELECCIONE EL MODO DE JUEGO\n1. 2 Jugadores\n2. Jugar contra un Botsito\n")
        if eleccion_modo_juego == "1":
            self.modo_juego = Dos_Jugadores()
        elif eleccion_modo_juego == "2":
            self.modo_juego = Maquina()
        else:
            print("Elija un modo de juego válido.")
        
        if self.modo_juego:
            self.modo_juego.seleccionar_pokemon()
            self.modo_juego.ejecutar()

            
#Creacion de las batallas

class Batalla(Pokemon):
     def __init__(self):
        self.pokemon_seleccionados_jugador1 = []
        self.pokemon_seleccionados_jugador2 = []

    
if __name__ == "__main__":
    
    juego = juego()
    juego.seleccionar_modo_juego()
    
    pass