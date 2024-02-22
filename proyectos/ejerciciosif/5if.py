print("A continuacion teclee 3 numeros")
numero1= float(input("numero1"))
numero2= float(input("numero2"))
numero3 = float(input("numero3"))


print("Los numeros que tecleaste son:")
if numero1==numero2==numero3 and numero3 ==numero1==numero2:
    print("Iguales los tres")
elif numero1==numero2 or numero1==numero3 or numero2==numero3:
    print("Dos numeros son iguales")
else:
    print("Los tres numeros son diferentes")
    