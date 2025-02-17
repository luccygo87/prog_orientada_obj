import tkinter as tk

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dashboard")

        # Agrega tus widgets y funcionalidades aquí
        self.label = tk.Label(self.root, text="Hola, mundo!")
        self.label.pack()

        # Agrega un botón para cerrar la ventana
        self.button = tk.Button(self.root, text="Cerrar", command=self.root.destroy)
        self.button.pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()