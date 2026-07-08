import tkinter as tk

# 1. Main Window Set Up Karna
root = tk.Tk()
root.title("Hifza's Calculator 🤖")
root.geometry("350x450")
root.configure(bg="#2c3e50")  # Beautiful Dark Background


# Buttons ke click ko handle karne ke liye function
def button_click(number):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, str(current) + str(number))


def clear_screen():
    screen.delete(0, tk.END)


def calculate():
    try:
        result = eval(screen.get())
        screen.delete(0, tk.END)
        screen.insert(0, str(result))
    except:
        screen.delete(0, tk.END)
        screen.insert(0, "Error")


# 2. Calculator ki Screen (Entry Box)
screen = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
screen.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=10)

# 3. Buttons Design Karna
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# 4. Buttons ko Loop ke zariye Screen par lagana
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), bg="#2ecc71", fg="white", width=5, height=2,
                        command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), bg="#e74c3c", fg="white", width=5, height=2,
                        command=clear_screen)
    elif text in ['/', '*', '-', '+']:
        btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), bg="#3498db", fg="white", width=5, height=2,
                        command=lambda t=text: button_click(t))
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14), bg="#ecf0f1", fg="black", width=5, height=2,
                        command=lambda t=text: button_click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# App ko chalate rakhna (Yeh hamesha aakhir mein hota hai)
root.mainloop()



