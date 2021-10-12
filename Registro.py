class Libro:
    def __init__(self, titulo, cant_rev, ano, cod_idioma, rating, isbn):
        self.titulo = titulo
        self.cant_rev = cant_rev
        self.ano = ano
        self.cod_idoma = cod_idioma
        self.rating = rating
        self.isbn = isbn

    def __str__(self):
        s = '|Título:{:<30} |Cantidad de revisiones: {:>4} |Año {:>7} |Codigo del idioma: {:>4} |Rating: {:>4} |ISBN: {:>10} '
        s = s.format(self.titulo, self.cant_rev, self.ano, self.cod_idoma, self.rating, self.isbn)
        return s


