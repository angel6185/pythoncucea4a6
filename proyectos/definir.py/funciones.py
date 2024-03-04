def calcularimpuesto (cantidadsiniva, porcentajedeiva):
  IVA=cantidadsiniva * (porcentajedeiva*.01)
  if porcentajedeiva == 0:
    porcentajedeiva = 21
  return IVA 
  

impuesto = calcularimpuesto (50, 16)
print(impuesto)
