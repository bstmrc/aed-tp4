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

        elif opc == 8:
            print('Cerrando programa ...')

        else:
            if len(libros) == 0:
                print('El vector no contiene libros, utilice la opción 1\n')

            else:
                if opc == 2:
                    opc_sm1 = -1

                    while opc_sm1 != 3:
                        m.print_opc1_submenu()
                        opc_sm1 = int(input('Opción: '))

                        if opc_sm1 == 1:
                            isbn_req = input('ISBN BUSCADO: ')
                            m.isbn_search(libros, isbn_req)

                        elif opc_sm1 == 2:
                            pass
                        elif opc_sm1 == 3:
                            print('Abortando...')
                        else:
                            print('Opción inválida')

if __name__ == '__main__':
    main()
