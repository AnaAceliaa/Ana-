def main():
    # Este programa calcula la cantidad necesaria de levadura segun los gramos de harina

    gramos_harina = float(input("Dame la harina en gramos: "))
    gramos_levadura = gramos_harina * 0.05
    print("Necesitas estos gramos de levadura:", gramos_levadura)
    pass


if __name__ == '__main__':
    main()
