import tkinter as tk

def mostrar_azul():
    ventana_azul = tk.Toplevel(root)
    ventana_azul.configure(bg="blue")
    ventana_azul.geometry("200x200")

def mostrar_rojo():
    ventana_roja = tk.Toplevel(root)
    ventana_roja.configure(bg="red")
    ventana_roja.geometry("200x200")

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana con botones")

# Crear botones
boton_azul = tk.Button(root, text="Botón 1 (Azul)", command=mostrar_azul)
boton_azul.pack(pady=10)

boton_rojo = tk.Button(root, text="Botón 2 (Rojo)", command=mostrar_rojo)
boton_rojo.pack(pady=10)

# Configurar la ventana principal
root.geometry("300x150")
root.mainloop()
