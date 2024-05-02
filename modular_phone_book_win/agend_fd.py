""" ANTONIO ARIAS URETA - 02/05/2024
    ARCHIVO DE FUNCIONES DE LA AGENDA """
# Importamos las librerías para poder limpiar la pantalla
# y pausar el flujo del programa (os) así como guardar y recuperar
# los contactos en un archivo llamado " 'FILE_NAME'.json " (json, pathlib).
import os
import json
from pathlib import Path

# Definimos las funciones: ------------------------------------------

def exist_file(dictionary, file_name):
    """ Comprueba si existe el archivo 'file_name'.json """
    dictionary = {}
    if os.path.isfile(file_name + ".json"):
        data = Path(file_name + ".json").read_text(encoding="utf-8")
        dictionary = json.loads(data)
        return dictionary
    else:
        return dictionary


def menu():
    """ Muestra el menú y captura la opción escogida. """
    os.system("cls")
    print("\n\n\t\t---- AGENDA TELEFÓNICA ----\n")
    print("\t\t1.- Buscar contacto.")
    print("\t\t2.- Añadir contacto.")
    print("\t\t3.- Borrar contacto.")
    print("\t\t4.- Actualizar contacto.")
    print("\t\t5.- Mostrar lista de contactos.")
    print("\t\t6.- Salir.")
    opcion = input("\n\t\tSeleccione una opción: ")
    return opcion


def find_contact(dictionary):
    """ Busca en 'dictionary' si existe el contacto y muestra su teléfono. """
    os.system("cls")
    name = input("\n\n\t\tIntroduzca el nombre del contacto a buscar: ").upper()
    if name in dictionary:
        print(f"\n\t\tEl teléfono de {name} es: {dictionary[name]}\n\n")
        os.system("pause")
    else:
        print(f"\n\t\t{name} no se encuentra entre sus contactos.\n\n")
        os.system("pause")


def add_phone(name_func, dictionary):
    """Captura el valor del teléfono y lo asigna al nombre en el diccionario
        Esta función es utilizada por otras funciones. """
    phone_func = input(f"\n\n\t\tIntroduzca el teléfono de {name_func}: ")
    while (len(phone_func) < 9 or len(phone_func) > 11) or not phone_func.isnumeric():
        os.system("cls")
        print("\n\n\n\n\n\t\t\t***** ERROR ****")
        print("\n\t\tEl formato del teléfono no es válido.")
        print("\t\t(Utilice de 9 a 11 caracteres numéricos.)")
        phone_func = input(f"\n\n\t\tIntroduzca el teléfono de {name_func}: ")
    dictionary[name_func] = phone_func


def add_contact(dictionary):
    """ Añade un nuevo contacto comprobando que no exista con anterioridad.
        Invoca a la función 'add_phone' para guardar el teléfono. """
    os.system("cls")
    name = input("\n\n\t\tIntroduzca el nombre del nuevo contacto: ").upper()
    if name in dictionary:
        print(f"\n\t\tYa existe un contacto de nombre {name}.\n\n")
        os.system("pause")
    else:
        add_phone(name, dictionary)
        print(f"\n\t\tSe ha añadido {name} a la agenda con Tlf {dictionary[name]}\n\n")
        os.system("pause")


def del_contact(dictionary):
    """ Borramos el contacto seleccionado. """
    os.system("cls")
    name = input("\n\n\t\tIntroduzca el contacto que desea eliminar: ").upper()
    if name in dictionary:
        del dictionary[name]
        print(f"\n\t\t{name} ha sido eliminado de sus contactos.\n\n")
        os.system("pause")
    else:
        print(f"\n\t\t{name} no se encuentra entre sus contactos.\n\n")
        os.system("pause")


def modify_contact(dictionary):
    """ Modifica el teléfono del contacto seleccionado.
        Invoca a la función 'add_phone' para guardar el nuevo teléfono. """
    os.system("cls")
    name = input("\n\n\t\tIntroduzca el nombre del contacto que desea actualizar: ").upper()
    if name in dictionary:
        add_phone(name, dictionary)
        print("\n\t\tSe ha actualizado correctamente.")
        print(f"\n\t\tEl nuevo teléfono de {name} es: {dictionary[name]}\n\n")
        os.system("pause")
    else:
        print(f"\n\t\t{name} no se encuentra etre sus contactos.\n\n")
        os.system("pause")


def list_contacts(dictionary):
    """ Listamos el contenido de la agenda. """
    os.system("cls")
    if dictionary == {}:
        print("\n\n\n\t\t\t-------------- AGENDA VACÍA ---------------")
        print("\t\t\t-------------------------------------------\n\n")

    else:
        print("\n\n\n\t\t\t---------- LISTADO DE CONTACTOS -----------")
        print("\t\t\t-------------------------------------------")
        for names, phones in dictionary.items():
            print(f"\t\t\t{names:25}\t{phones:11}")
        print("\n\n")
    os.system("pause")


def save_contacts(dictionary, file_name):
    """ Ordenamos y "dumpeamos" el contenido del diccionario en 'contacts_json',
        después lo escribimos en el archivo 'file_name'.json. """
    dictionary = dict(sorted(dictionary.items()))
    contacts_json = json.dumps(dictionary)
    Path(file_name + ".json").write_text(contacts_json, encoding="utf-8")
    return dictionary
