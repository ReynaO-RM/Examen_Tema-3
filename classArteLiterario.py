class ArteLiterario:
    def __init__(self):
        self._tipoArte = ""
        self._movimiento = ""
        self._influencia = ""

    def getTipoArte(self):
        return self._tipoArte
    def setTipoArte(self, tipoArte):
        self._tipoArte = tipoArte

    def getMovimiento(self):
        return self._movimiento
    def setMovimiento(self, movimiento):
        self._movimiento = movimiento

    def getInfluencia(self):
        return self._influencia
    def setInfluencia(self, influencia):
        self._influencia = influencia

    def mostrarInfoArte(self):
        return f"Tipo de arte: {self._tipoArte}, Movimiento: {self._movimiento}, Influencia: {self._influencia}"