def calcular_total(precio, cantidad, cliente_frecuente=False):
    if precio <= 0 or cantidad <= 0:
        raise ValueError("precio y cantidad deben ser positivos")
    subtotal = precio * cantidad
    descuento = 0
    if cantidad >= 10:  # RN-02: 10 o más unidades
        descuento = 0.10
    if cliente_frecuente:
        descuento += 0.05
    return round(subtotal * (1 - descuento), 2)
