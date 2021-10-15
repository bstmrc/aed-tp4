# modulo
import os.path
from Registro import *
import pickle


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
    m = [[0] * cols for f in range(fils)]
    for reg in v:
        if 2000 <= reg.anio <= 2022:
            f = reg.cod_idioma - 1
            c = reg.anio - 2000
            if m[f][c] == None:
                m[f][c] = reg
            elif reg.rating > m[f][c].rating:
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
                print('|Idioma: ', f + 1, '|Año: ', c + 2000, '|Rating: ', m[f][c].rating, '|Título: ',
                      m[f][c].titulo)


def linear_search(v):
    """Buscar Mayor Cantidad de Revisiones"""
    idioma_libro = None
    libro_may_rev = None
    rating_libro = None
    x = 0
    for i in range(len(v)):
        if v[i].cant_rev > x:
            x = v[i].cant_rev
            libro_may_rev = v[i]
            idioma_libro = v[i].cod_idioma
            rating_libro = v[i].rating
    return libro_may_rev, idioma_libro, rating_libro


def rating_promedio(x, v, y):
    n = len(v)
    promedio = 0
    total_rating = 0
    suma_rating = 0
    for i in range(n):
        if v[i].cod_idioma == x:
            total_rating += 1
            suma_rating += v[i].rating
    promedio = suma_rating // total_rating
    if promedio > y:
        msj = '* El rating es menor al del promedio.'
    elif promedio < y:
        msj = '* El rating es mayor al del promedio.'
    else:
        msj = '* El rating es igual al del promedio.'
    return promedio, msj


def mostrar_archivo_mat(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe')
        return
    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    while m.tell() < t:
        mat = pickle.load(m)
        print(mat)
    m.close()


def generar_archivo_matriz(mat, fd):
    m = open(fd, 'wb')
    cont = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] != None:
                pickle.dump(mat[f][c], m)
                cont += 1
    m.close()
    print('--' * 40)
    print(cont, 'registros grabados')
    print('Archivo "', fd, '" generado.')
    print('--' * 40)


def decade_range(f_year, l_year):
    """
    retorna un vector de acumulacion correspondiente
    a la cantidad de peliculas por década
    """
    l_year -= 10
    decades_range = []
    for decada in range(f_year, l_year + 1, 10):
        f_year_decade = decada
        l_year_decade = decada + 10
        decades_range.append([f_year_decade, l_year_decade])

    return decades_range

def cont_dec(vec_reg):
    counter = [0] * 10
    for libro in vec_reg:
        if libro.anio < 2000:
            decada_index = ((libro.anio - 1900) // 10)
            counter[decada_index] += 1

    return counter


def mostrar_cont(vec):
    decades = decade_range(1900, 2000)
    for cant in range(len(vec)):
        if vec[cant] != 0:
            print('Libros publicados en la década', decades[cant][0], '-', decades[cant][1], \
                ':', vec[cant])


def mayor(vec):
    decades = decade_range(1900, 2000)
    mayor = max(vec)
    index = -1 

    for cont in range(len(vec)):
        if mayor == vec[cont]:
            index = cont

    print('\nDécada con mayor cantidad de publicaciones: ', decades[index][0], '-', decades[index][1])


