valorManzana = float(input("valor"))
cantidadManzanas = float(input("cantidad"))
descuento = 0
total = valorManzana*cantidadManzanas


if cantidadManzanas >= 10:
    descuento = total - (valorManzana*cantidadManzanas)*.10
    
    print(descuento)
elif cantidadManzanas>=30:
    descuento = total - (valorManzana*cantidadManzanas)*.10
    
else:
    print("gracias por su compra sin descuento")
    print(total)

    
    
    