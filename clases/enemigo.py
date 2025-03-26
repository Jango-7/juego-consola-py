import random


class Enemigo:
    def __init__(self, nombre, salud, danio):
        self.nombre = nombre
        self.salud = salud
        self.danio = danio
    
    def atacar(self):
        return random.randint(5, 15)
    
    def recibir_danio(self, danio):
        self.salud -= danio
        if self.salud <= 0:
            print(f'Has derrotado a {self.nombre}!')
            return True
        return False