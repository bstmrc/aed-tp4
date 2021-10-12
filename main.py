# main

import modulo as m


def main():
    opc = -1
    libros = []
    csv_fd = 'libros.csv'
    libros = []
    while opc != 0:
        m.print_menu()
        opc = int(input('OPCIÓN: '))
        
        if opc == 1:
            libros = m.cargar_vector(csv_fd)
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
                            while len(isbn_req) < 10:
                                print('(RECORDATORIO): El ISBN debe tener una longitud igual a 10')
                                isbn_req = input('ISBN BUSCADO: ')

                            index = m.isbn_search(libros, isbn_req)
                            
                            if index != -1:
                                print('Libro de ISBN', isbn_req, 'encontrado...')
                                cant_rev = int(input('Cantidad de revisiones a agregar: '))
                                while cant_rev <= 0:
                                    print('\n(RECORDATORIO): Debe ser una cantidad positiva mayor a 0')
                                    cant_rev = int(input('Cantidad de revisiones a agregar: '))

                                m.add_rev(libros, index, cant_rev)
                                print('Se agregaron las revisiones con éxito')

                            else:
                                print('Libro no cargado')

                        elif opc_sm1 == 2:
                            ind = str(input('Ingrese el titulo del libro que esta buscando: '))
                            encontrado = m.buscar_titulo(libros, ind)
                            if encontrado == -1:
                                print('El libro que esta buscando no existe.')
                            else:
                                print(libros[encontrado])
                        elif opc_sm1 == 3:
                            print('Abortando...')
                        else:
                            print('Opción inválida')

                elif opc == 4:
                    mat = m.generar_matriz(libros)
                elif opc == 5:
                    pass
                elif opc == 6:
                    pass
                elif opc == 7:
                    pass


if __name__ == '__main__':
    main()



