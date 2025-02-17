class Archivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.archivo_abierto = False
        print(f"Se ha creado un objeto Archivo con el nombre {nombre_archivo}")

    def abrir(self):
        if not self.archivo_abierto:
            self.archivo_abierto = True
            print(f"Se ha abierto el archivo {self.nombre_archivo}")
        else:
            print(f"El archivo {self.nombre_archivo} ya está abierto")

    def cerrar(self):
        if self.archivo_abierto:
            self.archivo_abierto = False
            print(f"Se ha cerrado el archivo {self.nombre_archivo}")
        else:
            print(f"El archivo {self.nombre_archivo} ya está cerrado")

    def __del__(self):
        if self.archivo_abierto:
            self.cerrar()
        print(f"Se ha eliminado el objeto Archivo con el nombre {self.nombre_archivo}")


# Crear un objeto Archibo
archivo1 = Archivo("LUCIA_UEA.txt")
archivo1.abrir()
archivo1.cerrar()

# Crear otro objeto Archibo
archivo2 = Archivo("LUCIA_UEA.txt")
archivo2.abrir()

# Eliminar los objetos
del archivo1
del archivo2

# Corregir error de sintaxis en la clase
class Archibo(Archivo):
    pass

class Archio(Archivo):
    pass

class Archvo(Archivo):
    pass

class Archo(Archivo):
    pass

class Archfo(Archivo):
    pass

class Archfile:
    def __init__(self, LUCIA_UEA):
      super().__init__()
      self.LUCIA_UEA = LUCIA_UEA
      # La siguiente línea es para darle una respuesta más amigable al usuario que ejecuta esta función.


def main():
  try:
     Archo("example.txt")
  except NameError as e:
     # Error cuando no encuentra las variables o funciones.
     return f"Hemos encontrado este error:{e}"

main()