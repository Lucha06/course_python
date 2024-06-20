import numpy as np
"""
METODO DE BISECCION 
"""
# Definir la función
def f(x):
    return x ** 3 - 5


# Definir las variables a y b
a = 0.5
b = 2

# Definir la variable c
c = f(a)

# Ciclo iterativo
for i in range(18):
    print(f"Iteración {i + 1}")  # Número de iteración
    x = (a + b) / 2  # Define el valor de x y lo actualiza
    y = f(x)  # Define e imprime la variable y
    print(f"x = {x}")
    print(f"y = {y}")

    if c * f(x) > 0:  # Inicia el condicional
        a = x  # Actualiza el valor si se cumple la condición
    else:  # Si no cumple la condición entonces ...
        b = x  # Reemplaza el valor por b

"""
METODO DE NEWTON 
"""
import numpy as np


def MetNewton1(f, df, x1, m):
    """
    Método de Newton-Raphson para encontrar raíces de una función.

    Parámetros:
    f : function
        Función de la cual se quiere encontrar la raíz.
    df : function
        Derivada de la función f.
    x1 : float
        Aproximación inicial.
    m : float
        Tolerancia máxima permitida para el error.

    Retorna:
    x : float
        La raíz encontrada.
    """
    x = x1  # Aproximación inicial
    i = 1  # Inicializamos el contador
    error = abs(f(x))  # Inicializamos el error

    # Ciclo iterativo
    while error >= m and i < 100:
        x = x - f(x) / df(x)  # Fórmula de Iteración de Newton
        error = abs(f(x))  # Actualizar el error
        i += 1  # Incrementa el contador

    print('Tolerancia alcanzada en iteración', i)  # Imprime mensaje
    return x


# Ejemplo de uso
# Definir la función y su derivada
def f(x):
    return x ** 3 - 5


def df(x):
    return 3 * x ** 2


# Parámetros iniciales
x1 = 1.0
m = 1e-6

# Llamar a la función
root = MetNewton1(f, df, x1, m)
print('La raíz encontrada es:', root)

"""
METODO DE LA SECANTE 
"""
import numpy as np

# Definir la función
def f(x):
    return x**4 - 5

# Definir valores iniciales
x1 = 1
x2 = 3

# Evaluar la función en los valores iniciales
y1 = f(x1)
y2 = f(x2)

# Ciclo iterativo
for i in range(8):
    print(f"Iteración {i + 1}")  # Número de iteración
    x = x2 - ((x2 - x1) / (y2 - y1)) * y2  # Fórmula de la secante
    print(f"x = {x}")

    # Actualizar valores
    x1 = x2
    x2 = x
    y1 = f(x1)
    y2 = f(x2)

# Fin del ciclo iterativo
