from classPoemario import Poemario
from classArteLiterario import ArteLiterario

class Antologia(Poemario, ArteLiterario):
    def __init__(self):
        super().__init__()
        self._estructura = ""
        self._numPoetas = ""
        self._edicion = 0

    def getEstructura(self):
        return self._estructura
    def setEstructura(self, estructura):
        self._estructura = estructura

    def getNumPoetas(self):
        return self._numPoetas
    def setNumPoetas(self, numPoetas):
        self._numPoetas = numPoetas

    def getEdicion(self):
        return self._edicion
    def setEdicion(self, edicion):
        self._edicion = edicion

    def mostrarInfoAntologia(self):
        parentInfo2= super().mostrarInfoPoemario()
        return f"{parentInfo2}, Estructura: {self._estructura}, Numero de Poetas: {self._numPoetas}, Edicion: {self._edicion}"