import tkinter as tk
from tkinter import ttk
from gui.app import GastosHromigas

def main():
    ventana = tk.Tk()
    app = GastosHromigas(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()    