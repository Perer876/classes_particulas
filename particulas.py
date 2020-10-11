from particula import Particula

class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0,particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

quark = Particula(100,7,5,4,1,15,144,120,40)
muon = Particula(101,45,12,90,41,15,210,1,2)
mis_particulas = Particulas()
mis_particulas.agregar_final(quark)
mis_particulas.agregar_inicio(muon)
mis_particulas.agregar_inicio(quark)
mis_particulas.mostrar()
