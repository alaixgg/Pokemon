    
    def recibir_daño(self, daño):
        self.salud -= daño
        if self.salud < 0:
            print(f"{self.nombre}, ha muerto")

    def mostrar_estado(self):
        print(f"{self.nombre}: tiene, {self.salud} de salud")

    def elegir_ataque(self, ataque):
        if ataque in self.ataques:
            print(f"{self.nombre} utiliza {self.ataques[ataque]}")
        else:
            print("Elija un ataque válido")
