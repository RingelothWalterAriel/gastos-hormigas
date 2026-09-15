import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x400")
ventana.resizable(False, False)
ventana.configure(bg="#009cea")

tk.Label(
    ventana,
    text = "Hola, ingrese su nombre",
    font = ("Arial", 14),
  
).pack(pady=(20, 0), padx= 10,)

entrada_texto=tk.Entry(ventana)
entrada_texto.pack()                      


boton = tk.Button(
    ventana,
    text= "Aceptar",
    font=("Arial",14),
    cursor="hand2"
                )
boton.pack ()
  

ventana.mainloop()