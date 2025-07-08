from cliente import *

# === Menú principal ===
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar cliente")
        print("2. Actualizar cliente")
        print("3. Buscar cliente por nombre")
        print("4. Eliminar cliente")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            actualizar_cliente()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()