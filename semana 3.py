# Ejemplo de Técnicas de Programación

# 1. Abstracción
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        return "Conduciendo un coche."

class Bicicleta(Vehiculo):
    def conducir(self):
        return "Conduciendo una bicicleta."


# 2. Encapsulación
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes.")

    def obtener_saldo(self):
        return self.__saldo


# 3. Herencia
class Animal:
    def hacer_sonido(self):
        pass

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


# 4. Polimorfismo
class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio ** 2)

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# Ejemplo de uso
if __name__ == "__main__":
    # Abstracción
    coche = Coche()
    bicicleta = Bicicleta()
    print(coche.conducir())
    print(bicicleta.conducir())

    # Encapsulación
    cuenta = CuentaBancaria("Juan")
    cuenta.depositar(100)
    print(cuenta.obtener_saldo())
    cuenta.retirar(50)
    print(cuenta.obtener_saldo())

    # Herencia
    gato = Gato()
    perro = Perro()
    print(gato.hacer_sonido())
    print(perro.hacer_sonido())

    # Polimorfismo
    circulo = Circulo(5)
    cuadrado = Cuadrado(4)
    print("Área del círculo:", circulo.area())
    print("Área del cuadrado:", cuadrado.area())
