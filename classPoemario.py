from classArteLiterario import ArteLiterario
from classLibro import Libro
from classArteLiterario import ArteLiterario

class Poemario(Libro, ArteLiterario):
    def __init__(self):
        super().__init__()
        self._numPoemas = 0
        self._metrica = ""
        self._lenguaje = ""

    def getNumPoemas(self):
        return self._numPoemas
    def setNumPoema(self, numPoema):
        self._numPoemas = numPoema

    def getMetrica(self):
        return self._metrica
    def setMetrica(self, metrica):
        self._metrica = metrica

    def getLenguaje(self):
        return self._lenguaje
    def setLenguaje(self, lenguaje):
        self._lenguaje = lenguaje

    def mostrarInfoPoemario(self):
        parentInfo= super().mostrarInfoLibro()
        parentInfo2= super().mostrarInfoArte()
        return f"{parentInfo}, {parentInfo2}, Numero de Poemas: {self._numPoemas}, Metrica: {self._metrica}, Lenguaje poetico: {self._lenguaje}"