class Libro:
    def __init__(self, titulo, cant_rev, anio, cod_idioma, rating, isbn):
        self.titulo = titulo
        self.cant_rev = cant_rev
        self.anio = anio
        self.cod_idioma = cod_idioma
        self.rating = rating
        self.isbn = isbn

    def __str__(self):
<<<<<<< HEAD
        s = '|Título:{:<20} |Cantidad de revisiones: {:>4} |Año {:>7} |Codigo del idioma: {:>4} |Rating: {:>4} |ISBN: {:>10} '
=======
        s = '|Título: {:<20} |Cantidad de revisiones: {:>4} |Año {:>7} |Codigo del idioma: {:>4} |Rating: {:>4} |ISBN: {:>10} '
>>>>>>> 9c34b4834b20c762f9bc38f2942ac3df45712d90
        s = s.format(self.titulo, self.cant_rev, self.anio, self.cod_idioma, self.rating, self.isbn)
        return s


