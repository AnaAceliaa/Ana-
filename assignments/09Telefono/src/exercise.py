def main():
    # Este programa calcula el costo total mensual de un usuario del servicio telefonico.
    mensajes = int(input("Dame el numero de mensajes: "))
    megas = float(input("Dame el numero de megas: "))
    minutos = int(input("Dame el numero de minutos :"))

    costo_total = (mensajes * 0.80) + (megas + 0.80) + (minutos * 0.80)
    print("El costo mensual es:", costo_total)
if __name__ == '__main__':
    main()
