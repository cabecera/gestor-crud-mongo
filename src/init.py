from cliente import *
from productos import *
from pedidos import *

# === Menú principal ===
def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Menu cliente")
        print("2. Menu productos")
        print("3. Menu pedidos")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_pedidos()
        # elif opcion == "4":
        #     buscar_cliente_ciudad()
        # elif opcion == "5":
        #     buscar_cliente_fecha()
        # elif opcion == "6":
        #     eliminar_cliente()
        elif opcion == "0":
            print("Muchas gracias. Adiós!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()