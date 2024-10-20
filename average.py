def list_length():
    while True:
        try:
            AMOUNT = int(input("Introduzca el número de elementos de la lista: "))
            if AMOUNT > 0:
                return AMOUNT
            print("El valor ha de ser mayor que '0'.")
        except ValueError:
            print("El valor debe ser un número entero mayor que '0'.")

def number_input(AMOUNT, amount_counter):
    while True:
        try:
            number = float(input(f"Añada el número {amount_counter} de {AMOUNT} a la lista: "))
            return number
        except ValueError:
            print("El valor introducido no es válido.")

def average_list(numbers_list):
    average = 0
    for _ in range(len(numbers_list)):
        average = average + numbers_list[_]
    try:
        return average / len(numbers_list)
    except ArithmeticError:
        return 0


list_numbers = []
print(f"----- PROGRAMA PARA CALCULAR EL PROMEDIO DE UNA LISTA DE NÚMEROS -----\n")
AMOUNT = list_length()
for i in range(AMOUNT):
    list_numbers.append(number_input(AMOUNT, i + 1))
print(f"El promedio de los números introducidos es: {average_list(list_numbers)}")
