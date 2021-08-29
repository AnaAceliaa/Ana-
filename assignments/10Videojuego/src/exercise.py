def main():
    # escribe tu código abajo de esta línea
    juegos_nuevos = int(input("Dame la cantidad de juegos nuevos :"))
    juegos_usados = int(input("Dame la cantidad de juegos usados: "))

    total = (1000 * juegos_nuevos) + (350 * juegos_usados)
    print("Eltotal de la compra es :", total)
if __name__ == '__main__':
    main()
