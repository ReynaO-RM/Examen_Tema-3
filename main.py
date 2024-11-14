from classNovela import Novela
from classEnsayo import Ensayo
from classAntologia import Antologia

def main():
    novela = Novela()
    novela.setTitulo("Don Quijote")
    novela.setAutor("Miguel de Cervantes")
    novela.setEditorial("Editorial X")
    novela.setIsbn(124789)
    novela.setIdioma("Español")
    novela.setFormato("Físico")
    novela.setGenero("Aventura")
    novela.setAmbientacion("Siglo XVII")
    novela.setNumCapitulos(11)

    ensayo = Ensayo()
    ensayo.setTitulo("La politica")
    ensayo.setAutor("Aristóteles")
    ensayo.setEditorial("Editorial Y")
    ensayo.setIsbn(896543)
    ensayo.setIdioma("Griego")
    ensayo.setFormato("Digital")
    ensayo.setTema("Filosofía")
    ensayo.setTipo("Crítico")
    ensayo.setEstilo("Persuasivo")

    antologia = Antologia()
    antologia.setTitulo("Ecos de la Noche")
    antologia.setAutor("Liana Cortés")
    antologia.setEditorial("Editorial Z")
    antologia.setIsbn(678235)
    antologia.setIdioma("Inglés")
    antologia.setFormato("eBook")
    antologia.setNumPoema(56)
    antologia.setMetrica("Versos libres")
    antologia.setLenguaje("Metafórico")
    antologia.setTipoArte("Lírica")
    antologia.setMovimiento("Romanticismo")
    antologia.setInfluencia("Bécquer")

    antologia.setEstructura("Por temas")
    antologia.setNumPoetas(72)
    antologia.setEdicion(3)

    print("Novela:")
    print(novela.mostrarInfoNovela())
    print("\nEnsayo:")
    print(ensayo.mostrarInfoEnsayo())
    print("\nAntología:")
    print(antologia.mostrarInfoAntologia())

if __name__ == "__main__":
    main()