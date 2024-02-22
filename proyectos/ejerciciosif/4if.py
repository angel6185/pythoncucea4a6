print("Teclee el año que desea conocer si es biciesto")
año = int(input("año: "))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("Es biciesto")
else:
    print("No es biciesto")