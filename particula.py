from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0):
        self.id = id
        self.origen_x = origen_x
        self.origen_y = origen_y
        self.destino_x = destino_x
        self.destino_y = destino_y
        self.velocidad = velocidad
        self.red = red
        self.green = green
        self.blue = blue
        self.distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)

    def __str__(self):
        return (
            'ID: ' + str(self.id) + '\n'
            'Origen: (' + str(self.origen_x) + ',' + str(self.origen_y) + ')\n'
            'Destino: (' + str(self.destino_x) + ',' + str(self.destino_y) + ')\n'
            'Velocidad: ' + str(self.velocidad) + '\n'
            'Red: ' + str(self.red) + '\n'
            'Green: ' + str(self.green) + '\n'
            'Blue: ' + str(self.blue) + '\n'
            'Distancia: ' + str(self.distancia) + '\n'
        )
