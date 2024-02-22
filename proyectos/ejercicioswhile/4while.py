contador = 0
numero=int(input("Ingrese un Numero del 0 a 20"))

while numero not in range(0,20):
    print ("El numero es incorrecto")
    numero=int(input("Numero"))
    contador += 1
print(f"El numero ingresado es{numero}")

print(f"se han leido {contador} veces")