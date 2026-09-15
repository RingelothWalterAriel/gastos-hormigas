import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x400")
ventana.resizable(False, False)
ventana.configure(bg="#009cea")

def saludar():
    nombre = entrada_texto.get().strip()
    saludo_salida.config(text=f"Hola, {nombre}")

tk.Label(
    ventana,
    text = "Hola, ingrese su nombre",
    font = ("Arial", 14),
  
).pack(pady= 20, padx= 10,)

entrada_texto=tk.Entry(
    ventana,
    font=("Arial", 14) 
    )
entrada_texto.pack()                      


boton = tk.Button(
    ventana,
    text= "Saludar",
    font=("Arial",14),
    cursor="hand2",
    command=saludar
                )
boton.pack (pady = 20)
 
  
saludo_salida = tk.Label(
ventana,
    font = ("Arial", 14),
 )

saludo_salida.pack()

ventana.mainloop()