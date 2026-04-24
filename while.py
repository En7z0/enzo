#calculadora de soma usando while
print( "bienvenido ala calculador de suma")
while True:
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero"))
    print(f "el resultado es {n1+n2}") # pyright: ignore[reportUndefinedVariable]
    con = input("desea continuar? (si/no ):")
    if con.lower() != "si":
        print("gracias por usar la calculadora")
        break