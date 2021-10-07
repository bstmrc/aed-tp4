# main

import modulo as m

def main():
    opc = -1

    while opc != 8:
        m.print_menu()
        opc = int(input('OPCIÓN: '))


if __name__ == '__main__':
    main()
