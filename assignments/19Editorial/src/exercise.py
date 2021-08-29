def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))
    paginas = palabras/475
    paginas_totales = paginas + 1
    costo = paginas_totales * (60*.88)
    print("El costo total en dolares es:",costo)
if __name__ == '__main__':
    main()
    