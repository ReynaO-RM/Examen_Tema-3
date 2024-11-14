#clase padre 1
class MaterialBibliografico:
    def __init__(self):
        self._titulo = ""
        self._autor = ""
        self._editorial = ""

    def getTitulo(self):
        return self._titulo
    def setTitulo(self, titulo):
        self._titulo = titulo

    def getAutor(self):
        return self._autor
    def setAutor(self, autor):
        self._autor = autor

    def getEditorial(self):
        return self._editorial
    def setEditorial(self, editorial):
        self._editorial = editorial

    def mostrarInfoBibliografico(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Editorial: {self._editorial}"