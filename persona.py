class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self.edad
    
    def setEdad(self, edad):
        self._edad = edad

    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self._altura = altura

    def getSexo(self):
        return self.sexo
    
    def setSexo(self, sexo):
        self._sexo = sexo