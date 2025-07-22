def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n - 1)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    elif n == 1:
        return fibonacci(n - 1) + fibonacci(n - 2)

def contar_letra(palabra, letra):
    if palabra == "":
        return 0
    if palabra[1] == letra:
        return 1 + contar_letra(palabra[1:], letra)
    else:
        return contar_letra(palabra[1:], letra)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

opcion = "0"
while opcion != "7":
    print("===MENÚ===")
    print("1.Calcular factorial de un número")
    print("2.Suma de los primeros N números naturales")
    print("3.Calcular el n-ésimo número del fibonacci")
    print("4.Contar cuántas veces aparece una letra en una palabra")
    print("5.Invertir cadena de texto")
    print("6.Calcular potencia de un número")
    print("7.Salir")
    opcion = input("\nSeleccione una opción: ")
    try:
        match opcion:
            case "1":
                n = int(input("Ingrese el número que desea calcular el factorial:"))
                print(f"El factorial de {n} es {factorial(n)}")
            case "2":
                n = int(input("Ingrese cuantos números desea sumar: "))
                print(suma(n))
            case "3":
                n = int(input("Ingrese el n-ésimo número que quiere calcular del fibonacci: "))
                print(f"F{n} = {fibonacci(n)}")
            case "4":
                palabra = input("Ingrese una palabra: ").lower()
                letra = input("¿Qué letra desea contar?: ")
                letra = letra[0].lower()
                print(f"La letra: {letra} aparece {contar_letra(palabra, letra)} veces")
            case "6":
                base = int(input("Ingresa la base: "))
                exponente = int(input("Ingresa el exponente: "))
                print(potencia(base, exponente))
            case "7":
                print("Saliendo")
            case __:
                print("Opción no disponible")
    except Exception as e:
        print("Ha ocurrido un error inesperadi: "+ str(e))