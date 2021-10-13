# modulo
import os.path
from Registro import *


def print_menu():
    '''Printea el menú principal'''
    menu = '\t\t\tMENÚ DE OPCIONES\n' + ('==' * 20) + '\n1. Carga\n2. Sumar Revision\n' \
           + '3. Mayor revisiones\n4. Popularidad 2000\n5. Publicaciones por década\n' \
           + '6. Guardar populares\n7. Mostrar archivo\n0. SALIR\n' + ('==' * 20)

    print(menu)


def add_in_order(v, reg):
    '''Cargar archivo en el registro ordenado por ISBN'''
    izq, der = 0, len(v) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if reg.isbn == v[c].isbn:
            pos = c
            break
        if reg.isbn < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def cargar_vector(fd):
    ''' Leer archivo y cargarlo en un vector'''
    v = []
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe')
    else:
        m = open(fd, mode="rt", encoding="utf8")
        pos = 1
        for linea in m:
            if linea[-1] == '\n':
                linea = linea[:-1]
            if pos != 1:
                token = linea.split(',')
                reg = Libro(token[0], int(token[1]), int(token[2]), int(token[3]), float(token[4]), token[5])
                add_in_order(v, reg)
            pos += 1
        m.close()
    return v


def mostrar_vector(v):
    '''Muestra el vector'''
    for i in range(len(v)):
        print(v[i])


def print_opc1_submenu():
    """
    imprime en pantalla el submenu para la opcion 1
    """
    menu = '\tMODO DE BÚSQUEDA\n' + ('==' * 20) + '\n1. Por ISBN\n2. Por TÍTULO\n' \
           + '3. CACELAR\n'
    print(menu)


def isbn_search(vec, isbn):
    """
    Realiza una busqueda binaria por isbn requerido
    desde el programa principal
    """

    inicio, final = 0, len(vec) - 1
    index = 0
    while inicio <= final:
        centro = (inicio + final) // 2

        if isbn == vec[centro].isbn:
            index = centro
            return index

        if isbn < vec[centro].isbn:
            final = centro - 1
        else:
            inicio = centro + 1

    return -1


def add_rev(vec, index, cant):
    """Agrega una revision al registro indicado."""
    vec[index].cant_rev += cant


def mayor_rating(v):
    '''Función para encontrar el mayor rating'''
    may = 0
    for i in range(len(v)):
        if v[i].rating > v[may].rating:
            may = i
    return may


def generar_matriz(v):
    '''Generar matriz con el mayor rating'''
    fils, cols = 27, 22
    m = [[None] * cols for f in range(fils)]
    for reg in v:
        if 2000 <= reg.anio <= 2022:
            f = reg.cod_idioma - 1
            c = reg.anio - 2000
            if m[f][c] == None:
                m[f][c] = reg
            else:
                if reg.rating > m[f][c].rating:
                    m[f][c] = reg
    return m


def mostar_matriz(mat):
    """
    Muestra por pantalla el resultado de las casillas de
    la matriz que obtuvieron un valor
    """
    cad = 'Libro más popular de idioma {} en el año {}: {}'
    for idioma in range(len(mat)):
        for anio in range(len(mat[idioma])):
            if mat[idioma][anio] != None:
                cad = cad.format(idioma + 1, anio + 2000, mat[idioma][anio].titulo)
                print(cad)


def buscar_titulo(v, x):
    """busqueda secuencial"""

    for i in range(len(v)):
        if x == v[i].titulo:
            return i
    return -1


def recorrer_mat(m):
    '''Recorrer matriz para verla, ya que la otra funcion no me muestra la matriz'''
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] != None:
                print('|Libro: ', m[f][c].titulo, '|Idioma: ', f + 1, '|Año: ', c + 2000, '|Mayor rating: ', m[f][c].rating)


def principal():
    print('Prueba')
    v = cargar_vector('libros.csv')
    mat = generar_matriz(v)
    # mostar_matriz(mat)
    recorrer_mat(mat)


if __name__ == '__main__':
    principal()
