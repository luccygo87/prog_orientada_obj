# Programación Tradicional

def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

def main_tradicional():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura (método tradicional) es: {promedio:.2f}")

# Programación Orientada a Objetos (POO)

class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

def main_poo():
    clima = Clima()
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        clima.ingresar_temperatura(temperatura)
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura (método POO) es: {promedio:.2f}")

# Menú principal
def main():
    print("Menú principal:")
    print("1. Calcular promedio semanal de temperatura (método tradicional)")
    print("2. Calcular promedio semanal de temperatura (método POO)")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        main_tradicional()
    elif opcion == 2:
        main_poo()
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()