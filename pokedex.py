class ICharacter:
    def ataque(self):
        pass

    def super(self):
        pass

    def movimiento(self):
        pass

    def salud(self):
        pass

class Pikachu(ICharacter):
    def __init__(self):
        self.salud = 150

    def ataque(self):
        print("Pika pika")
        self.salud -= 20

    def super(self):
        print("Petruno")
        self.salud -= 45

    def movimiento(self):
        print("Paso")
        self.salud += 5

    def mostrar_salud(self):
        print(f"Salud: {self.salud}")

class Charmander(ICharacter):
    def __init__(self):
        self.salud = 165

    def ataque(self):
        print("")

    def super(self):
        print("")

    def movimiento(self):
        print("")

    def mostrar_salud(self):
        print(f"Salud: {self.salud}")

class Bulbasaur(ICharacter):
    def __init__(self):
        self.salud = 160

    def ataque(self):
        print("")

    def super(self):
        print("")

    def movimiento(self):
        print("")

    def mostrar_salud(self):
        print(f"Salud: {self.salud}")

class Squirtle(ICharacter):
    def __init__(self):
        self.salud = 155

    def ataque(self):
        print("")

    def super(self):
        print("")

    def movimiento(self):
        print("")

    def mostrar_salud(self):
        print(f"Salud: {self.salud}")


class Player:
    def __init__(self, pokemon: ICharacter) -> None:
        self.pokemon = pokemon

    def atacar(self):
        self.pokemon.ataque()

    def usar_super(self):
        self.pokemon.super()

    def usar_movimiento(self):
        self.pokemon.movimiento()

    def mostrar_salud(self):
        self.pokemon.mostrar_salud()

def Batalla(self, ataque, super, movimiento, salud):
    print("Elige tu pokemon:")
    pikachu = Pikachu()
    charmander = Charmander()
    player1 = Player(pikachu)
    player2 = Player(charmander)

    while pikachu.salud > 0 and charmander.salud > 0:
        print("Turno de jugador 1")
        player1.mostrar_salud()
        opcion = int(input("Elige una opción (1: Atacar, 2: Super, 3: Movimiento): "))
        if opcion == 1:
            player1.atacar()
        elif opcion == 2:
            player1.usar_super()
        elif opcion == 3:
            player1.usar_movimiento()

        print("Turno de jugador 2")
        player2.mostrar_salud()
        opcion = int(input("Elige una opción (1: Atacar, 2: Super, 3: Movimiento): "))
        if opcion == 1:
            player2.atacar()
        elif opcion == 2:
            player2.usar_super()
        elif opcion == 3:
            player2.usar_movimiento()

    print("El combate ha terminado.")
