# main

import modulo as m

def main():
    opc = -1
    libros = []

    while opc != 8:
        m.print_menu()
        opc = int(input('OPCIÓN: '))
        
        if opc == 1:
            libros = m.cargar_vector('libros.csv')
            m.mostrar_vector(libros)


if __name__ == '__main__':
    main()
