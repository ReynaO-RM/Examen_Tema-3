from classLibro import Libro

class Novela(Libro):
    def __init__(self):
        super().__init__()
        self._genero = ""
        self._ambientacion = ""
        self._numCapitulos = 0

    def getGenero(self):
        return self._genero
    def setGenero(self, genero):
        self._genero = genero

    def getAmbientacion(self):
        return self._ambientacion
    def setAmbientacion(self, ambientacion):
        self._ambientacion = ambientacion

    def getNumCapitulos(self):
        return self._numCapitulos
    def setNumCapitulos(self, numCapitulos):
        self._numCapitulos = numCapitulos

    def mostrarInfoNovela(self):
        parentInfo= super().mostrarInfoLibro()
        return f"{parentInfo}, Genero: {self._genero}, Ambientacion: {self._ambientacion}, Numero de capitulos: {self._numCapitulos}"

