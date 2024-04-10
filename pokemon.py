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
    
    def mostrar_ataques_disponibles(self):
        print(f"Ataques para {self.nombre}:")
        for ataque in self.ataques:
            print("-", ataque)
            


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
# Jugador vs Jugador
class Dos_Jugadores:
    def __init__(self):
        self.pokemon_seleccionados_jugador1 = []
        self.pokemon_seleccionados_jugador2 = []

        print("***MODO DE JUEGO:*** \n VS 2 Entrenadores\n\n")

        # Elección de Pokémons para el jugador 1
        print("¡Entrenador 1, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_jugador1 = []
        for _ in range(3):
            pokemon_seleccionado = seleccionar_pokemon()
            self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
        print("El entrenador ha elegido los siguientes Pokémones:")
        for pokemon in self.pokemon_seleccionados_jugador1:
            pokemon.mostrar_ataques_disponibles()

        # Elección de Pokémons para el jugador 2
        print("\n¡Entrenador 2, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_jugador2 = []
        for _ in range(3):
            pokemon_seleccionado = seleccionar_pokemon()
            self.pokemon_seleccionados_jugador2.append(pokemon_seleccionado)
        print("El entrenador ha elegido los siguientes Pokémones:")
        for pokemon in self.pokemon_seleccionados_jugador2:
            pokemon.mostrar_ataques_disponibles()

    def ejecutar(self):
        print("¡Comienza el juego!")
        turno = 1
        while not self.hay_ganador():
            if turno == 1:
                self.turno_jugador(self.pokemon_seleccionados_jugador1, self.pokemon_seleccionados_jugador2)
                turno = 2
            else:
                self.turno_jugador(self.pokemon_seleccionados_jugador2, self.pokemon_seleccionados_jugador1)
                turno = 1
        print("¡Fin del juego!")

    def turno_jugador(self, atacantes, oponentes):
        print("\nTurno del Jugador:")
        for pokemon in atacantes:
            if pokemon.salud <= 0:
                print(f"{pokemon.nombre} no puede atacar. Ha sido derrotado.")
                continue
            print(f"\nEs el turno de {pokemon.nombre}.")
            pokemon.mostrar_ataques_disponibles()
            print("(Escriba el nombre del ataque)")
            ataque_elegido = input(f"Elige un ataque para {pokemon.nombre}: ")
            pokemon.attack(ataque_elegido, oponentes[-1] if oponentes[-1].salud > 0 else oponentes[0])
            break  # Salir después del primer ataque

    def hay_ganador(self):
        
        if all(pokemon.salud == 0 for pokemon in self.pokemon_seleccionados_jugador1):
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

        # Elección de Pokémons
        pok_aleatorio = input("Deseas:\n1. Tener un equipo aleatorio\n2. Elige tus pokemons por tu cuenta\n")
        if pok_aleatorio == '1':
            print("¡Botsito Rocket va a elegir tus pokemones de manera aleatoria!")
            time.sleep(1)
            print("Botsito Rocket está escogiendo los pokemones...")
            while len(self.pokemon_seleccionados_jugador1) < 3:
                pokemon_seleccionado = random.choice([Pikachu(), Squirtle(), Bulbasaur(), Charmander(), Caterpie(), Pidgeotto(), Krabby(), Raticate(), Muk(), Kingler()])
                self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
                time.sleep(2)
            print("El Botsito Rocket ha elegido los siguientes Pokémones:")
            for pokemon in self.pokemon_seleccionados_jugador1:
                print(pokemon.nombre)
                pokemon.mostrar_ataques_disponibles()

        elif pok_aleatorio == '2':
            print("¡Entrenador, es tu turno de seleccionar tus Pokémones!")
            self.pokemon_seleccionados_jugador1 = []
            contador = 0
            while contador != 3:
                contador += 1
                pokemon_seleccionado = seleccionar_pokemon()
                self.pokemon_seleccionados_jugador1.append(pokemon_seleccionado)
            print("El entrenador ha elegido los siguientes Pokémones:")
            for pokemon in self.pokemon_seleccionados_jugador1:
                print(pokemon.nombre)
                pokemon.mostrar_ataques_disponibles()
        else: 
            print("Elige una opción válida!")  

        time.sleep(1)
        print("\n\n¡Botsito Rocket, es tu turno de seleccionar tus Pokémones!")
        self.pokemon_seleccionados_maquina = []
        time.sleep(1)
        print("Botsito Rocket, está escogiendo sus pokemones...")
        while len(self.pokemon_seleccionados_maquina) < 3:
            pokemon_seleccionado = random.choice([Pikachu(), Squirtle(), Bulbasaur(), Charmander(), Caterpie(), Pidgeotto(), Krabby(), Raticate(), Muk(), Kingler()])
            self.pokemon_seleccionados_maquina.append(pokemon_seleccionado)
        time.sleep(2)
        print("El Botsito Rocket ha elegido los siguientes Pokémones:")
        for pokemon in self.pokemon_seleccionados_maquina:
            print(pokemon.nombre)
            pokemon.mostrar_ataques_disponibles()

    def ejecutar(self):
        print("¡Comienza el juego!")
        turno = 1
        while not self.hay_ganador():
            if turno == 1:
                self.turno_jugador(self.pokemon_seleccionados_jugador1, self.pokemon_seleccionados_maquina)
                turno = 2
            else:
                self.turno_maquina(self.pokemon_seleccionados_maquina, self.pokemon_seleccionados_jugador1)
                turno = 1
        print("¡Fin del juego!")

    def turno_jugador(self, atacantes, oponentes):
        print("\nTurno del Jugador:")
        for pokemon in atacantes:
            if pokemon.salud <= 0:
                print(f"{pokemon.nombre} no puede atacar. Ha sido derrotado.")
                continue
            print(f"\nEs el turno de {pokemon.nombre}.")
            time.sleep(0.2)
            pokemon.mostrar_ataques_disponibles()
            print("(Escriba el nombre del ataque)")
            ataque_elegido = input(f"Elige un ataque para {pokemon.nombre}: ")
            pokemon.attack(ataque_elegido, oponentes[-1] if oponentes[-1].salud > 0 else oponentes[0])
            break  # Salir después del primer ataque

    def turno_maquina(self, atacantes, oponentes):
        print(f"\nTurno del Botsito Rocket:")
        for pokemon in atacantes:
            if pokemon.salud <= 0:
                print(f"{pokemon.nombre} no puede atacar. Ha sido derrotado.")
                continue
            print(f"\nEs el turno de {pokemon.nombre}.")
            # Seleccionar un ataque aleatorio
            ataque = random.choice(list(pokemon.ataques.keys()))
            objetivo = oponentes[-1] if oponentes[-1].salud > 0 else oponentes[0]
            if objetivo.salud <= 0:
                print(f"{objetivo.nombre} no puede ser atacado. Ha sido derrotado.")
                continue
            pokemon.attack(ataque, objetivo)
            break  # Salir después del primer ataque

    def hay_ganador(self):
        
        if all(pokemon.salud <= 0 for pokemon in self.pokemon_seleccionados_jugador1):
            print("¡El Jugador 2 ha ganado!")
            return True
        elif all(pokemon.salud <= 0 for pokemon in self.pokemon_seleccionados_maquina):
            print("¡El Jugador 1 ha ganado!")
            return True
        return False
    
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