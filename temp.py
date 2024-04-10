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