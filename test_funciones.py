from app.utils.funciones import *

# Prueba de funciones
print(es_sano(80, False))  # True
print(calcular_calorias([120, 200, 150]))  # 446.5
print(calcular_costo({"nombre": "Fresa", "precio": 1200}, {"nombre": "Choco", "precio": 500}, {"nombre": "Maní", "precio": 900}))  # 2600
print(calcular_rentabilidad(7500, {"nombre": "Fresa", "precio": 1200}, {"nombre": "Choco", "precio": 500}, {"nombre": "Maní", "precio": 900}))  # 4900
print(producto_mas_rentable({"nombre": "A", "rentabilidad": 4000}, {"nombre": "B", "rentabilidad": 2500}, {"nombre": "C", "rentabilidad": 11000}, {"nombre": "D", "rentabilidad": 3200}))  # "C"
