# tarea.py
print("Bienvenido al menú de programas")

def mostrar_menu():
	print("1.- Programa 1")
	print("2.- Programa 2")
	print("3.- Programa 3")
	print("0.- Salir")


def main():
	while True:
		mostrar_menu()
		try:
			entrada = input("Seleccione una opción: ").strip()
			if entrada == "":
				print("Entrada vacía. Intente de nuevo.")
				continue
			if entrada.lower() in ("0", "salir", "q"):
				print("Saliendo.")
				break
			opcion = int(entrada)
		except ValueError:
			print("Entrada inválida: por favor ingrese un número.")
			continue

		match opcion:
			case 1:
				print("Ha seleccionado el programa 1")
			case 2:
				print("Ha seleccionado el programa 2")
			case 3:
				print("Ha seleccionado el programa 3")
			case _:
				print("Opción inválida")


if __name__ == "__main__":
	main()

