print("Teclee el año que desea conocer si es biciesto")
año = float(input("año"))
if año % 400:
    print("es biciesto")
elif año % 100:
    print("no es biciesto")
elif año % 4:
        print("Es biciesto")
else:
        print("no es biciesto")
