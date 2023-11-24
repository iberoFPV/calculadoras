from tkinter import *

# Función para calcular el tamaño de fuente adecuado
def calculate_font_size():
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    font_size = int(min(window_width, window_height) / 15)
    return font_size

# Función para actualizar el tamaño de fuente de los botones
def update_font_size():
    font_size = calculate_font_size()
    for button in buttons:
        button.config(font=("Helvetica", font_size))

# Función llamada al cambiar el tamaño de la ventana
def on_resize(event):
    update_font_size()

# Función llamada al presionar un botón numérico o de operación
def press(num):
    current_equation = equation.get()
    if current_equation == "ERROR":
        equation.set("")

    if num == "=":
        try:
            total = str(eval(current_equation))
            equation.set(total)
        except Exception as e:
            equation.set("ERROR")
    else:
        equation.set(current_equation + str(num))

# Función llamada al presionar el botón "="
def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set("ERROR")

# Función llamada al presionar el botón "Clear"
def clear_pressed():
    equation.set("")

# Crear la ventana principal
root = Tk()
root.configure(
    background="#333333"
)  # Color de fondo similar al de la calculadora de iOS
root.title("Calculadora")

# Configuración del tamaño fijo y no redimensionable
root.geometry("250x300")
root.resizable(False, False)

# Configurar el peso de las filas y columnas para que no se expandan
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Variable de texto para la expresión en la calculadora
equation = StringVar()

# Estilo para la entrada de texto
entry_style = {
    "font": ("Helvetica", calculate_font_size()),
    "fg": "white",
    "bg": "#222222",
    "justify": "right",
}

# Crear la entrada de texto para la expresión
expression_entry = Entry(root, textvariable=equation, **entry_style)
expression_entry.grid(row=0, column=0, columnspan=4, sticky="nswe", padx=10, pady=10)

# Posiciones y configuraciones de los botones
button_positions = [
    (1, 0, "7"),
    (1, 1, "8"),
    (1, 2, "9"),
    (2, 0, "4"),
    (2, 1, "5"),
    (2, 2, "6"),
    (3, 0, "1"),
    (3, 1, "2"),
    (3, 2, "3"),
    (4, 0, "0", 2),
    (4, 2, "."),
    (5, 3, "="),
    (5, 2, "C"),
    (1, 3, "+"),
    (2, 3, "-"),
    (3, 3, "*"),
    (4, 3, "/"),
]

# Crear una lista de botones
buttons = [
    Button(
        root,
        text="7",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(7),
    ),
    Button(
        root,
        text="8",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(8),
    ),
    Button(
        root,
        text="9",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(9),
    ),
    Button(
        root,
        text="4",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(4),
    ),
    Button(
        root,
        text="5",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(5),
    ),
    Button(
        root,
        text="6",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(6),
    ),
    Button(
        root,
        text="1",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(1),
    ),
    Button(
        root,
        text="2",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(2),
    ),
    Button(
        root,
        text="3",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(3),
    ),
    Button(
        root,
        text="0",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press(0),
    ),
    Button(
        root,
        text=".",
        font=("Helvetica", calculate_font_size()),
        bg="#666",
        fg="white",
        command=lambda: press("."),
    ),
    Button(
        root,
        text="+",
        font=("Helvetica", calculate_font_size()),
        bg="#FF9500",
        fg="white",
        command=lambda: press("+"),
    ),
    Button(
        root,
        text="-",
        font=("Helvetica", calculate_font_size()),
        bg="#FF9500",
        fg="white",
        command=lambda: press("-"),
    ).grid(row=2, column=3, sticky="nsew", padx=5, pady=5),
    Button(
        root,
        text="*",
        font=("Helvetica", calculate_font_size()),
        bg="#FF9500",
        fg="white",
        command=lambda: press("*"),
    ),
    Button(
        root,
        text="/",
        font=("Helvetica", calculate_font_size()),
        bg="#FF9500",
        fg="white",
        command=lambda: press("/"),
    ).grid(row=4, column=3, sticky="nsew", padx=5, pady=5),
    Button(
        root,
        text="=",
        font=("Helvetica", calculate_font_size()),
        bg="#FF9500",
        fg="white",
        command=equalpress,
    ),
    Button(
        root,
        text="Clear",
        font=("Helvetica", calculate_font_size()),
        bg="#FF3B30",
        fg="white",
        command=clear_pressed,
    ).grid(row=5, column=0, columnspan=3, sticky="nsew", padx=5, pady=5),
]

# Colocar los botones en la interfaz gráfica
for item in button_positions:
    row, col, text, *span = item
    colspan = span[0] if span else 1
    button = buttons.pop(0) if buttons else None
    if button:
        button.configure(
            text=text,
            font=("Helvetica", calculate_font_size()),
            command=lambda t=text: press(t),
        )
        button.grid(
            row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5
        )

# Configurar el evento de redimensionamiento y la tecla de atajo para limpiar la pantalla
root.bind("<KeyPress-c>", lambda event: clear_pressed())
root.bind("<Configure>", lambda event: on_resize(event))

# Iniciar el bucle principal de la aplicación
root.mainloop()
