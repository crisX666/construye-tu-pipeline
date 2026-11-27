"""Pruebas automatizadas del módulo de descuentos · Actividad práctica 1.

Reglas del negocio
  RN-01  Precio y cantidad deben ser positivos.
  RN-02  10 o más unidades: 10 % de descuento.
  RN-03  Cliente frecuente: 5 % adicional.
  RN-04  Descuento máximo: 15 %.

Los totales esperados se calcularon a mano a partir de las reglas,
no ejecutando el código.
"""
import pytest

from descuentos import calcular_total

# (id, descripción, precio, cantidad, cliente_frecuente, total esperado)
CASOS_VALIDOS = [
    ("CP-01", "5 uds, sin cliente frecuente (0 %)",         100,   5,    False, 500.00),
    ("CP-02", "5 uds, cliente frecuente (5 %)",             100,   5,    True,  475.00),
    ("CP-03", "20 uds, sin cliente frecuente (10 %)",       100,   20,   False, 1800.00),
    ("CP-04", "20 uds, cliente frecuente (15 %)",           100,   20,   True,  1700.00),
    ("CP-05", "Límite: 9 uds, sin cliente frecuente",       100,   9,    False, 900.00),
    ("CP-06", "Límite: 9 uds, cliente frecuente",           100,   9,    True,  855.00),
    ("CP-07", "Límite: 10 uds, sin cliente frecuente",      100,   10,   False, 900.00),
    ("CP-08", "Límite: 10 uds, cliente frecuente",          100,   10,   True,  850.00),
    ("CP-09", "Límite: 11 uds, sin cliente frecuente",      100,   11,   False, 990.00),
    ("CP-10", "Límite: 11 uds, cliente frecuente",          100,   11,   True,  935.00),
    ("CP-11", "Importe mínimo: precio 0.01, 1 ud",          0.01,  1,    False, 0.01),
    ("CP-12", "Redondeo a 2 decimales: 3 × 19.99, frecuente", 19.99, 3,  True,  56.97),
    ("CP-13", "Tope del 15 %: 1000 uds, frecuente",         10,    1000, True,  8500.00),
]

# (id, descripción, precio, cantidad)
CASOS_INVALIDOS = [
    ("CP-14", "Cantidad = 0",          100, 0),
    ("CP-15", "Cantidad negativa (-1)", 100, -1),
    ("CP-16", "Precio = 0",             0,   5),
    ("CP-17", "Precio negativo (-50)",  -50, 5),
]


@pytest.mark.parametrize(
    "id_caso, descripcion, precio, cantidad, frecuente, esperado",
    CASOS_VALIDOS,
    ids=[caso[0] for caso in CASOS_VALIDOS],
)
def test_total_con_descuento(id_caso, descripcion, precio, cantidad, frecuente, esperado):
    assert calcular_total(precio, cantidad, frecuente) == esperado


@pytest.mark.parametrize(
    "id_caso, descripcion, precio, cantidad",
    CASOS_INVALIDOS,
    ids=[caso[0] for caso in CASOS_INVALIDOS],
)
def test_rechaza_valores_no_positivos(id_caso, descripcion, precio, cantidad):
    with pytest.raises(ValueError, match="positivos"):
        calcular_total(precio, cantidad)
