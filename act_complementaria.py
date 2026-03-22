import string

def show_menu():
        print("- Opciones -" )
        print("1. Agregar equipo.")
        print("2. Agregar resultado.")
        print("3. Mostrar tabla.")
        print("4. Eliminar un equipo.")
        print("5. Salir.")
        print()

print("==============================================")
print("¡BIENVENIDO AL SISTEMA DE POSICIONES (FUTBOL)!")
print("==============================================")

table = {}
valid_options = [1, 2, 3, 4, 5]

# Bucle principal

while True:
        show_menu()
        choice = int(input("Seleccion: "))
        while choice not in valid_options:
            print("Opcion no valida. Por favor ingrese nuevamente.")
            print()
            choice = int(input("Seleccion: "))
        if choice == 1:
            name = input("Ingresa el nombre del equipo: ").lower()
            while name in table:
                print("Equipo ya existente. Por favor elija otro.")
                name = input("Ingresa el nombre del equipo: ").lower()
            table[name] = 0 # Agregamos al equipo con 0 puntos.
            print("Equipo agregado con exito.")
        if choice == 2:
                home = input("Ingrese el local: ")
                while home not in table:
                      print("Equipo desconocido")
                      print()
                      home = input("Ingrese el local: ")
                away = input("Ingrese el visitante: ")
                while away not in table:
                    print("Equipo desconocido.")
                    print()
                    away = input("Ingrese el visitante: ")
                result = input("Ingrese el resultado (ej 4-2): ")
                parts = result.split("-")
                while len(parts) != 2 or not (parts[0].isdigit or parts[1].isdigit):
                      print("Formato invalido. Por favor intente nuevamente")
                      print()
                      result = input("Ingrese el resultado (ej 4-2): ")
                goals = [int(x) for x in parts]
                if goals[0] > goals[1]:
                      table[home] += 3
                elif goals[1] > goals[0]:
                        table[away] += 3
                else:
                    table[home] += 1
                    table[away] += 1
                print("Resultado almacenado exitosamente.")
                print()
        if choice == 3:
              print(table)
        if choice == 5:
              print("Hasta pronto!")
              break