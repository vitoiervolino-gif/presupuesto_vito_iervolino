EFECTIVO="efectivo"
TRANSFERENCIA = "transferencia"
IVA = 0.21
def buscar_posicion(listas,nombre):
    for i in range(len(listas)):
        if listas[i] == nombre:
            return i
    return -1
def calcular_descuento(pago, subtotal, EFECTIVO="efectivo"):
    if pago == EFECTIVO:
        descuento = (subtotal * 10) / 100
    else:
        descuento = 0
    return descuento, subtotal - descuento
def calcular_iva (subtotal_desc, IVA, subtotal):
    iva = subtotal * IVA
    total = iva + subtotal_desc
    return total, iva
