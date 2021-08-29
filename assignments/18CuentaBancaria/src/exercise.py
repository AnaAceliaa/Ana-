def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes pasado"))
    ingresos = float(input("Dame los ingresos"))
    egresos = float(input("Dame los egresos"))
    cheques = int(input("Dame el número de cheques expedidos"))
    saldo_final = saldo + ingresos - ((cheques * 13) + egresos)
    interes = saldo_final * 0.925
    print("El saldo final es:",interes)


if __name__ == '__main__':
    main()
