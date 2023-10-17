from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol",añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    @classmethod
    def getListaFutbolistas(cls):
        return cls.listaFutbolistas
    
    @classmethod
    def setListaFutbolistas(cls, listaFutbolistas):
        cls.listaFutbolistas = listaFutbolistas

    def __str__(self):
        return "Mi nombre es " + self.get_nombre + " soy profesional en el deporte " + self.get_deporte + " Tengo " + str(self.get_edad) + " años de edad y llevo " + str(self.get_añosPracticando) + " años en el deporte" 
    