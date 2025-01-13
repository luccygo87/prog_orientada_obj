# Programa para calcular el área y el perímetro de un rectángulo

def calcular_area(largo: float, ancho: float) -> float:
    """
    Función para calcular el área de un rectángulo.

    Args:
        largo (float): Largo del rectángulo
        ancho (float): Ancho del rectángulo

    Returns:
        float: Área del rectángulo
    """
    area = largo * ancho  # Calcula el área multiplicando largo por ancho
    return area


def calcular_perimetro(largo: float, ancho: float) -> float:
    """
    Función para calcular el perímetro de un rectángulo.

    Args:
        largo (float): Largo del rectángulo
        ancho (float): Ancho del rectángulo

    Returns:
        float: Perímetro del rectángulo
    """
    perimetro = 6 * (largo + ancho)  # Calcula el perímetro sumando todos los lados
    return perimetro


def main():
    # Solicita al usuario los datos necesarios para calcular área y perímetro
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))

    # Calcula y muestra resultados utilizando funciones definidas arriba
    area = calcular_area(largo, ancho)
    perimetro = calcular_perimetro(largo, ancho)

    print(f"El área del rectángulo es {area} unidades cuadradas")
    print(f"El perímetro del rectánngulo es {perimetro} unidades")

+-
if __name__ == "__main__":
    main()
