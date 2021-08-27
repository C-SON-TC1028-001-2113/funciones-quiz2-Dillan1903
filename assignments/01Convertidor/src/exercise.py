# Escribe tus funciones abajo de esta línea

def main():
    # Escribe tu código abajo de esta línea
    pass
    print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm")
    res = int(input('Introduce una opcion: '))

    if res == 1:
        res = int(input("Introduce la cantidad: "))
        pies_cm = res * 30.48
        print(pies_cm)
        return
    elif res == 2:
        res= int(input('Introduce la cantidad: '))
        pulgadas_cm = res * 2.54
        print(pulgadas_cm)
        return
    elif res == 3:
        res = int(input('Introduce la cantidad: '))
        yardas_cm = res * 91.44
        print(yardas_cm)
        return
    else:
        res = int(input('Introduce la cantidad: '))
        print("Error")
        return
if __name__ == '__main__':
    main()
