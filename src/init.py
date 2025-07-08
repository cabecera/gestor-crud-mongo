from cliente import *

# === Menú principal ===
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar cliente")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()