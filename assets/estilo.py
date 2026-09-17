from tkinter import ttk 


#PALETA DE COLORES
BG_MAIN = "#EEE9FE" # FONDO PRINCIPAL
BG_WHITE = "#FCFCFD" # FONDO BLANCO
ACCENT = "#7C4DFF" # COLOR PRINCIPAL
GREEN = "#00C853" # COLOR VERDE
CORAL = "#FF6F61" # COLOR CORAL
TEXT_DARK = "#1A1A1A" # COLOR TEXTO OSCURO
TEXT_LIGHT = "#FAFAFA" # COLOR TEXTO CLARO

#COLORES DERIVADOS
ACCENT_HOVER = "#5E35B1" # COLOR PRINCIPAL OSCURO
GREEN_HOVER = "#00E676" # COLOR VERDE OSCURO
CORAL_HOVER = "#FF3D00" # COLOR CORAL OSCURO
BG_ENTRY = "#F5F5F5" # FONDO DE ENTRADAS
BORDER_COLOR = "#E0E0E0" # COLOR DE BORDE

def aplicar_color(style: ttk.Style):
    style.theme_use("clam")
    
    
    #frame principal
    style.configure("Main.TFrame", background=BG_MAIN)
    
    #header
    style.configure(
        "Header.TFrame",
        background=ACCENT
    )
    
    style.configure(
        "Header.TLabel",
        background=ACCENT,
        foreground=BG_WHITE,
        font=("Segoe UI", 30, "bold")
    )
    
    style.configure(
        "HeaderSubtitle.TLabel",
        background=ACCENT,
        foreground=TEXT_LIGHT,
        font=("Segoe UI", 14)
    )