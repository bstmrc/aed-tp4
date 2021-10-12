# modulo
import os.path
from Registro import *


def print_menu():
    '''Printea el menú principal'''
    menu = '\tMENÚ DE OPCIONES\n' + ('==' * 20) + '\n1. Carga\n2. Sumar Revision\n' \
           + '3. Mayor revisiones\n4. Popularidad 2000\n5. Publicaciones por década\n' \
           + '6. Guardar populares\n7. Mostrar archivo\n0. SALIR\n'

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
    '''Mostrar el vector'''
    for i in range(len(v)):
        print(v[i])


def print_opc1_submenu():
    menu = '\tMODO DE BÚSQUEDA\n' + ('==' * 20) + '\n1. Por ISBN\n2. Por TÍTULO\n' \
            + '3. CACELAR\n'
    print(menu)


def isbn_search(vec, isbn):
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
    vec[index].cant_rev += cant


def mostar_matriz(mat):
    cad = 'Libro más popular de idioma {} en el año {}: {}'
    for idioma in range(len(mat)):
        for anio in range(len(mat[idioma])):
            if mat[idioma][anio] != 0:
                cad.format(idioma, anio, mat[idioma][anio])
                print(cad)
                

