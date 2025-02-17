import threading
import time

def tarea(nombre, tiempo):
    print(f"Hilo {nombre} iniciado.")
    time.sleep(tiempo)
    print(f"Hilo {nombre} finalizado después de {tiempo} segundos.")

hilo1 = threading.Thread(target=tarea, args=("A", 2.5))
hilo2 = threading.Thread(target=tarea, args=("B", 3.0))
hilo3 = threading.Thread(target=tarea, args=("C", 1.9))

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()

print("Todas las tareas han finalizado.")