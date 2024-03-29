import random

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

#     
def seleccionar_pokemon():
    contador = 0
    pokemones_seleccionados = []

    while contador <= 3:
        def elegir_pokemon():
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
            eleccion_pokemon = input("Ingresa el número correspondiente al Pokémon: ")

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

        pokemon_seleccionado = elegir_pokemon()
        pokemones_seleccionados.append(pokemon_seleccionado)
        contador += 1

#Jugador & Maquina
class Dos_Jugadores:
    def __init__(self):
        self.pokemon_seleccionados_jugador1 = []
        self.pokemon_seleccionados_jugador2 = []

    def seleccionar_pokemon(self):
        print("¡Entrenador 1, es tu turno de seleccionar tus Pokémones!")
        pokemonsJugador1 = []
        contador = 0
        while contador < 3:
            pokemon_seleccionado = seleccionar_pokemon()
            pokemonsJugador1.append(pokemon_seleccionado)
            contador += 1
        self.pokemon_seleccionados_jugador1 = pokemonsJugador1
        print("El Entrenador 1 ha elegido los siguientes Pokémones:", self.pokemon_seleccionados_jugador1)

        print("¡Ahora tu, entrenador 2, es tu turno de seleccionar tus Pokémones!")
        pokemonsJugador2 = []
        contador = 0
        while contador < 3:
            pokemon_seleccionado = seleccionar_pokemon()
            pokemonsJugador2.append(pokemon_seleccionado)
            contador += 1
        self.pokemon_seleccionados_jugador2 = pokemonsJugador2
        

        print("El Entrenador 1 ha elegido los siguientes Pokémones:", self.pokemon_seleccionados_jugador1)
        print("El Entrenador 2 ha elegido los siguientes Pokémones:", self.pokemon_seleccionados_jugador2)


class Maquina:
    def __init__(self):
        self.nombre = "Máquina"
        self.pokemon = None

    def seleccionar_pokemon(self):
            J1 = seleccionar_pokemon()
            self.pokemon = random.choice(seleccionar_pokemon)

        

    def elegir_ataque(self):
        # Lógica para que la máquina seleccione un ataque
        pass

#Funcion de seleccion del modo de juego
    
def seleccionar_modo_juego():
    eleccion_modo_juego = input("SELECCIONE EL MODO DE JUEGO\n1. 2 Jugadores\n2. Jugar contra un Botsito\n")
    if eleccion_modo_juego == "1":
        return Dos_Jugadores()
    elif eleccion_modo_juego == "2":
        return Maquina()
    else:
        print("Elija un modo de juego válido.")
        return seleccionar_modo_juego()
    
#Creacion de las batallas

class Batalla(Pokemon):
    seleccionar_pokemon()
    
    seleccionar_modo_juego()
    pass
    
    #inic
    


    # Aquí puedes usar la matriz pokemones_seleccionados



# Ejemplo de uso



if __name__ == "__main__":
    seleccionar_pokemon()
   # seleccionar_modo_juego()
    pass