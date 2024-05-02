""" ANTONIO ARIAS URETA - 02/05/2024
    AGENDA PARA GUARDAR CONTACTOS USANDO ARCHIVO '.json' """

# Importamos 'os' para poder "pausar" el flujo del programa
# y 'agend_fd' que contiene las funciones creadas
# para el manejo de los contactos.
from os import system
import agend_fd

# Creamos el diccionario donde guardaremos los contactos.
contacts = {}

# Declaramos e inicializamos la constante con el nombre
# del archivo que contendrá los contactos.
CONTACTS_FILE = "contactsFE20XyA"

# Comprobamos si existe el fichero 'CONTACTS_FILE'(.json) y
# si existe "cargamos" su contenido en el diccionario.
contacts = agend_fd.exist_file(contacts, CONTACTS_FILE)

# Iniciamos el programa con un bucle "infinito"
# que solo se romperá con la opción '6'.
while True:

    option = agend_fd.menu()                    # Mostramos el menu y capturamos
                                                # la opción del usuario.

    match option:

        case "1":
            agend_fd.find_contact(contacts)     # Buscamos el contacto y lo mostramos.

        case "2":
            agend_fd.add_contact(contacts)                              # Añadimos nuevo contacto.
            contacts = agend_fd.save_contacts(contacts, CONTACTS_FILE)  # Lo guardamos en
                                                                        #'CONTACTS_FILE.json'.

        case "3":
            agend_fd.del_contact(contacts)                              # Borramos el contacto que
                                                                        # elija el usuario.
            contacts = agend_fd.save_contacts(contacts, CONTACTS_FILE)  # Guardamos la nueva
                                                                        #lista de contactos
                                                                        # en 'CONTACTS_FILE.json'.

        case "4":
            agend_fd.modify_contact(contacts)                           # Modificamos el contacto
                                                                        # que elija el usuario.
            contacts = agend_fd.save_contacts(contacts, CONTACTS_FILE)  # Guardamos lista actuali.
                                                                        # en 'CONTACTS_FILE.json'.

        case "5":
            agend_fd.list_contacts(contacts)                # Listamos por terminal el contenido
                                                            # de la agenda.

        case "6":
            print("\n\t\tSaliendo de la agenda.........\n\n")   # Salimos del bucle infinito
            break                                               # terminando el programa.


        case _:
            print("\n\t\tLa opción escogida no es válida.\n\n")     # En caso de escoger una opción
            system("pause")                                         # no válida, mostramos mensaje
                                                                    # por terminal.
