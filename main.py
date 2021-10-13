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

        elif opc == 0:
            print('Cerrando programa ...')

        else:
            if len(libros) == 0:
                print('El vector no contiene libros, utilice la opción 1\n')

            elif opc == 2:
                opc_sm2 = -1

                while opc_sm2 != 3:
                    m.print_opc1_submenu()
                    opc_sm2 = int(input('Opción: '))
                    index = -1

                    if opc_sm2 != 3:

                        cant_rev = int(input('Cantidad de revisiones a agregar: '))
                        while cant_rev <= 0:
                            print('\n(RECORDATORIO): Debe ser una cantidad positiva mayor a 0')
                            cant_rev = int(input('Cantidad de revisiones a agregar: '))

                        if opc_sm2 == 1:

                            isbn_req = input('ISBN BUSCADO: ')
                            while len(isbn_req) < 10:
                                print('(RECORDATORIO): El ISBN debe tener una longitud igual a 10')
                                isbn_req = input('ISBN BUSCADO: ')

                            index = m.isbn_search(libros, isbn_req)
                            
                            if index != -1:
                                print('Libro de ISBN', isbn_req, 'encontrado...')
                                print(libros[index])
                                m.add_rev(libros, index, cant_rev)
                                print('Se agregaron las revisiones con éxito')

                            else:
                                print('Libro no cargado')

                        elif opc_sm2 == 2:
                            title = str(input('Ingrese el titulo del libro que esta buscando: '))
                            index = m.buscar_titulo(libros, title)

                            if index != -1:
                                print('Libro', title, 'encontrado...')
                                print(libros[index])
                                m.add_rev(libros, index, cant_rev)
                                print('Se agregaron las revisiones con éxito')

                            else:
                                print('El libro que esta buscando no existe.')

                        else:
                            print('Opción inválida')

                    else:
                        print('Abortando...')
            elif opc == 3:
                libro_may_rev, idioma_libro, rating_libro = m.linear_search(libros)
                print('* El libro con mayor cantidad de reviciones es: ')
                print(libro_may_rev)
                promedio, msj = m.rating_promedio(idioma_libro, libros, rating_libro)
                print('* El promedio de rating en su idioma es de: ', promedio)
                print(msj)
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



