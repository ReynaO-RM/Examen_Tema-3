from material_bibliografico import MaterialBibliografico

class Libro(MaterialBibliografico):
    def __init__(self):
        super().__init__()
        self._isbn = 0
        self._idioma = ""
        self._formato = ""

    def getIsbn(self):
        return self._isbn
    def setIsbn(self, isbn):
        self._isbn = isbn

    def getIdioma(self):
        return self._idioma
    def setIdioma(self, idioma):
        self._idioma = idioma

    def getFormato(self):
        return self._formato
    def setFormato(self, formato):
        self._formato = formato

    def mostrarInfoLibro(self):
        parentInfo= super().mostrarInfoBibliografico()
        return f"{parentInfo}, ISBN: {self._isbn}, Idioma: {self._idioma}, Formato: {self._formato}"