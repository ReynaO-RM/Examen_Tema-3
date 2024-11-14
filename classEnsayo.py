from classLibro import Libro

class Ensayo(Libro):
    def __init__(self):
        super().__init__()
        self._tema = ""
        self._tipo = ""
        self._estilo = ""

    def getTema(self):
        return self._tema
    def setTema(self, tema):
        self._tema = tema

    def getTipo(self):
        return self._tipo
    def setTipo(self, tipo):
        self._tipo = tipo

    def getEstilo(self):
        return self._estilo
    def setEstilo(self, estilo):
        self._estilo = estilo

    def mostrarInfoEnsayo(self):
        parentInfo = super().mostrarInfoLibro()
        return f"{parentInfo}, Tema: {self._tema}, Tipo: {self._tipo}, Estilo: {self._estilo}"