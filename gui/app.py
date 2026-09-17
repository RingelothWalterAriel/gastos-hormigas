import tkinter as tk
from tkinter import ttk, messagebox




class GastosHromigas:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Gastos Hormigas")
        root.geometry("700x600")
        root.resizable(False, False)
    
        
        #aplicar estilo
        self.style = ttk.Style(self.root)
        
        from assets.estilo import aplicar_color
        aplicar_color(self.style)
        
        self.frame = ttk.Frame(self.root, style = "Main.TFrame")
        self.frame.pack(fill = "x")
        
        self._menu_()
        self._crear_header_()
    
    
    
    
    def _menu_(self):
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)
        
        # Crear el menú archivo
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        
        menu_archivo.add_command(
            label = "Exportar PDF",
            accelerator = "Ctrl+E",
            command = self._exportar_pdf_
        )
        
        
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label = "Salir",
            accelerator = "Ctrl+Q",
            command = self._salir_ 
        )
           
        barra_menu.add_command(
            label = "Acerca de",
            command=self._acerca_de_
        )  
        
        #atajos de teclado
        self.root.bind("<Control-q>", self._salir_)
        self.root.bind("<Control-e>", self._exportar_pdf_)

    def _crear_header_(self):
        inner = ttk.Frame(self.frame, style = "Header.TFrame")
        inner.pack(ipadx=24, ipady=28)
        
        
        #titulo
        ttk.Label(
            inner,
            text = "Gastos Hormigas",
            style="Header.TLabel"
        ).pack()
        
        #subtitulo
        
        ttk.Label(
            inner,
            text = "Supervisar tus gastos hormigas es la mejor manera de ahorrar dinero.",
            style="HeaderSubtitle.TLabel"
        ).pack(pady=(2 , 0))
    
    def _exportar_pdf_(self, event=None):
        pass
    
    def _salir_(self, event=None):
        
        if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
           self.root.destroy() 
           
    def _acerca_de_(self):
        messagebox.showinfo(
            "Acerca de gastos hormigas",
        """
        Gastos innecesarios \n
        Supervisar tus gastos hormigas es la mejor manera de ahorrar dinero. \n
        
        """ 
        )             