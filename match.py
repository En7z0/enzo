# explicacion uso de match :)

print("1.- Opcion 1")
print("2.- Opcion 2")
print("3.- Opcion 3")

try:
  op = int(input("Seleccione una opcion: "))
except ValueError:
  print("Entrada invalida: por favor ingrese un numero.")
else:
  match op:
    case 1:
      print("Ha seleccionado la opcion 1")
    case 2:
      print("Ha seleccionado la opcion 2")
    case 3:
      print("Ha seleccionado la opcion 3")
    case _:
      print("Opcion invalida")