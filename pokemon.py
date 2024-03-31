import random
import time 

class ataque_Behavior:
    def attack(self, opponent):
        pass

    def reduce_salud(self, cantidad, opponent):
        opponent.reduce_salud(cantidad)
#Se implementan las clases de los ataques
#Fuentes de la cantidad de daño https://bulbapedia.bulbagarden.net/wiki/List_of_moves
class Impactrueno(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Impactrueno!")
        cantidad = 60 
        self.reduce_salud(cantidad, opponent)

class Rayo(ataque_Behavior):
    def attack(self, opponent):
        print("¡Usó Rayo!")
        cantidad = 10
        self.reduce_salud(cantidad, opponent)

class Ataque_Rapido(ataque_Behavior):
    def attack(self, opponent):
        print("¡Usó Ataque Rápido!")
        cantidad = 40
        self.reduce_salud(cantidad, opponent)


class Placaje(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Impactrueno!")
        opponent.reduce_salud(30)

class Lanzallamas(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Lanzallamas !")
        opponent.reduce_salud(50)

class Gruñido(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Gruñido !")
        opponent.reduce_salud(20)

class Arañazo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Arañazo!")
        opponent.reduce_salud(30)

class Ascuas(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Ascuas!")
        opponent.reduce_salud(45)


class Burbuja(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Burbuja!")
        opponent.reduce_salud(20)

class Rayo_Burbuja (ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Rayo Burbuja !")
        opponent.reduce_salud(40)
    
class Drenadoras(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Drenadoras!")
        opponent.reduce_salud(40)

class Tacleada(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Tacleada !")
        opponent.reduce_salud(40)

class Supersonico(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Supersonico !")
        opponent.reduce_salud(20)

class Picotazo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Picotazo!")
        opponent.reduce_salud(35)

class Remolino(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Remolino!")
        opponent.reduce_salud(60)
    
class Tornado(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Tornado !")
        opponent.reduce_salud(60)

class Latigo_Cepa(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Latigo Cepa!")
        opponent.reduce_salud(35)
    
class Somnifero(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Somnifero !")
        opponent.reduce_salud(20)

class Pistola_agua(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Pistola de agua!")
        opponent.reduce_salud(20)

class Hidropulso(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Hidropulso !")
        opponent.reduce_salud(40)
    
class Tajo_Cruzado(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Tajo Cruzado !")
        opponent.reduce_salud(40)

class Hipercolmillo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Hipercolmillo !")
        opponent.reduce_salud(80)

class Golpe_Cabeza(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Golpe cabeza !")
        opponent.reduce_salud(70)
    
class Lodo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Uso Lodo !")
        opponent.reduce_salud(40)

class Bomba_lodo(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Bomba Lodo!")
        opponent.reduce_salud(80) 

class Ataque_acido(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Ataque Acido !")
        opponent.reduce_salud(40)

class Infortunio(ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó Infortunio !")
        cantidad = 40
        opponent.reduce_salud(cantidad)
        
"""class (ataque_Behavior):
    def attack(self,opponent):
        print("¡Usó  !")
        opponent.reduce_health(10)  """



#Clase base de pokemons
class Pokemon:
    def __init__(self, nombre, salud, ataques):
        self.nombre = nombre
        self.salud = salud
        self.ataques = ataques

    def attack(self, ataque, opponent):    
        if ataque in self.ataques:
            self.ataques[ataque].attack(opponent)
        else:
            print(f"{self.nombre} no conoce el ataque {ataque}.")

    def reduce_salud(self, cantidad):
        self.salud -= cantidad
        print(f"{self.nombre} ha perdido {cantidad} puntos de salud. Salud restante: {self.salud}")


#Clases de pokemons
#Fuentes puntos de salud https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 100, ataque_Behavior())  
        self.ataques = {
            "Impactrueno": Impactrueno(),
            "Rayo": Rayo(),
            "Ataque Rápido": Ataque_Rapido()
        }

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__("Caterpie", 50, ataque_Behavior())
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
        super().__init__("Bulbasaur", 120, ataque_Behavior())
        self.ataques = {
            "Látigo Cepa": Latigo_Cepa(),
            "Drenadoras": Drenadoras(),
            "Placaje": Placaje(),
            "Somnífero": Somnifero()
        }

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 80, ataque_Behavior())
        self.ataques = {
            "Lanzallamas": Lanzallamas(),
            "Gruñido": Gruñido(),
            "Arañazo": Arañazo(),
            "Ascuas": Ascuas()
        }

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 90, ataque_Behavior())
        self.ataques = {
            "Pistola Agua": Pistola_agua(),
            "Burbuja": Burbuja(),
            "Ataque Rápido": Ataque_Rapido(),
            "Placaje": Placaje()
        }

class Krabby(Pokemon):
    def __init__(self):
        super().__init__("Krabby", 50, ataque_Behavior())
        self.ataques = {
            "Burbuja": Burbuja(),
            "Rayo Burbuja": Rayo_Burbuja(),
            "Placaje": Placaje(),
            "Tajo Cruzado": Tajo_Cruzado()
        }

class Raticate(Pokemon):
    def __init__(self):
        super().__init__("Raticate", 80, ataque_Behavior())
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
        super().__init__("Kingler", 110, ataque_Behavior)
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

# Jugador vs Jugador
class Dos_Jugadores:
    def __init__(self):
        self.pokemon_seleccionados_jugador1 = []
        self.pokemon_seleccionados_jugador2 = []

        print("***MODO DE JUEGO:*** \n VS 2 Entrenadores\n\n")

        # Elección de Pokémons para el jugador 1
        print("¡Entrenador 1, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_jugador1 = []
        pok_aleatorio = input("Deseas: \n1. Tener un equipo aleatorio\n2. Elegir tus pokemons por tu cuenta\n")

        if pok_aleatorio == '1':
            # Elección aleatoria de los Pokémon para el jugador 1
            print("El Botsito Rocket está eligiendo tus pokemones de manera aleatoria...")
            while len(self.pokemon_seleccionados_jugador1) < 3:
                pokemon_seleccionado = random.choice([Pikachu()])  # Agregar más Pokémon aquí
                self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
                time.sleep(2)
            print("El Botsito Rocket ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador1])

        elif pok_aleatorio == '2':
            # Elección manual de los Pokémon para el jugador 1
            print("Entrenador 1, es tu turno de seleccionar tus Pokémones!")
            contador = 0
            while contador != 3:
                contador += 1
                pokemon_seleccionado = seleccionar_pokemon()
                self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
            print("El entrenador ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador1])
        else:
            print("Eliga una opción válida.")

        # Elección de Pokémons para el jugador 2
        print("\n¡Entrenador 2, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_jugador2 = []
        pok_aleatorio = input("Deseas: \n1. Tener un equipo aleatorio\n2. Elegir tus pokemons por tu cuenta\n")

        if pok_aleatorio == '1':
            # Elección aleatoria de los Pokémon para el jugador 2
            print("El Botsito Rocket está eligiendo tus pokemones de manera aleatoria...")
            while len(self.pokemon_seleccionados_jugador2) < 3:
                pokemon_seleccionado = random.choice([Pikachu()])  # Agregar más Pokémon aquí
                self.pokemon_seleccionados_jugador2.append(pokemon_seleccionado)
                time.sleep(2)
            print("El Botsito Rocket ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador2])

        elif pok_aleatorio == '2':
            # Elección manual de los Pokémon para el jugador 2
            print("Entrenador 2, es tu turno de seleccionar tus Pokémones!")
            contador = 0
            while contador != 3:
                contador += 1
                pokemon_seleccionado = seleccionar_pokemon()
                self.pokemon_seleccionados_jugador2.append(pokemon_seleccionado)
            print("El entrenador ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador2])
        else:
            print("Eliga una opción válida.")

    def ejecutar(self):
        print("¡Comienza el juego!")
        while not self.hay_ganador():
            self.turno_jugador1()
            if self.hay_ganador():
                break
            self.turno_jugador2()
        print("¡Fin del juego!")

    def turno_jugador1(self):
        # Turno del jugador 1
        print("\nTurno del Jugador 1")
        for pokemon in self.pokemon_seleccionados_jugador1:
            if pokemon.salud <= 0:
                print(f"{pokemon.nombre} no puede atacar. Ha sido derrotado.")
                continue
            print(f"\nEs el turno de {pokemon.nombre}.")
            ataque_elegido = random.choice(list(pokemon.ataques.keys()))
            pokemon.attack(ataque_elegido, random.choice(self.pokemon_seleccionados_jugador2))
            time.sleep(2)

    def turno_jugador2(self):
        # Turno del jugador 2
        print("\nTurno del Jugador 2")
        for pokemon in self.pokemon_seleccionados_jugador2:
            if pokemon.salud <= 0:
                print(f"{pokemon.nombre} no puede atacar. Ha sido derrotado.")
                continue
            print(f"\nEs el turno de {pokemon.nombre}.")
            ataque_elegido = random.choice(list(pokemon.ataques.keys()))
            pokemon.attack(ataque_elegido, random.choice(self.pokemon_seleccionados_jugador1))
            time.sleep(2)

    def hay_ganador(self):
        # Verificar si hay un ganador
        if all(pokemon.salud <= 0 for pokemon in self.pokemon_seleccionados_jugador1):
            print("¡El Jugador 2 ha ganado!")
            return True
        elif all(pokemon.salud <= 0 for pokemon in self.pokemon_seleccionados_jugador2):
            print("¡El Jugador 1 ha ganado!")
            return True
        return False   


class Maquina:
   def __init__(self):
        self.pokemon_seleccionados_jugador1 = []
        self.pokemon_seleccionados_maquina = []
        
        print("***MODO DE JUEGO:*** \nJugar contra un Botsito\n\n")

        #Eleccion de Pokemons
   
        pok_aleatorio= input("Deseas  \n1. Tener un equipo aleatorios \n2.Elige tus pokemons, por tu cuenta")
        if pok_aleatorio == '1':
            print("¡Botsito Rocket, va elegir tus pokemones de manera aleatoria!")
            self.pokemon_seleccionados_maquina = []
            time.sleep(1)
            print("Botsito Rocket, está escogiendo los pokemones...")
            while len(self.pokemon_seleccionados_jugador1) < 3:
              pokemon_seleccionado = random.choice([Pikachu(), Squirtle(), Bulbasaur(), Charmander(), Caterpie(), Pidgeotto(), Krabby(), Raticate(), Muk(), Kingler()])
              self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
              time.sleep(2)
            print("El Botsito Rocket ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador1]) 

        elif pok_aleatorio == '2':
            print("¡Entrenador, es tu turno de seleccionar tus Pokémones!")
            self.pokemon_seleccionados_jugador1 = []
            contador = 0
            while contador != 3:
                 contador +=1
                 pokemon_seleccionado = seleccionar_pokemon()
                 self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
            print("El entrenador ha elegido los siguientes Pokémones:", [pokemon.nombre for pokemon in self.pokemon_seleccionados_jugador1]) 
        else: 
            print("Eliga una opcion valida! ")  

        time.sleep(1)
        print("\n\n¡Botsito Rocket, es tu turno de seleccionar tus Pokémones!")
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
       
        if len(self.pokemon_seleccionados_jugador1) == 0 or len(self.pokemon_seleccionados_maquina) == 0:
            if len(self.pokemon_seleccionados_jugador1) == 0:
                print("¡Gana el botsito Rocket!")
            else: 
                print("¡Gana el entrenador 1!")

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