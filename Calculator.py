import tkinter as tk

root = tk.Tk()
root.title("Hifza's Smart Calc 🤖")
root.geometry("380x540")
root.configure(bg="#0f172a")  # Premium Dark Slate Background


# Core Logic Functions
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            res = num1 + num2
        elif operation == "-":
            res = num1 - num2
        elif operation == "*":
            res = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Cannot divide by 0", fg="#f87171")
                return
            res = num1 / num2

        result_label.config(text=f"{round(res, 4)}", fg="#38bdf8")
    except ValueError:
        result_label.config(text="Enter valid numbers", fg="#f87171")


# --- UI DESIGN ---

# Main Card/Container (Modern Glass Box Look)
card = tk.Frame(root, bg="#1e293b", bd=0, padx=25, pady=25)
card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=480)

# App Title
title_label = tk.Label(card, text="Simple Calculator", font=("Segoe UI", 20, "bold"), bg="#1e293b", fg="#f8fafc")
title_label.pack(pady=(10, 25))

# Input Box 1 Style
lbl1 = tk.Label(card, text="First Number", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8")
lbl1.pack(anchor="w", padx=5)
entry1 = tk.Entry(card, font=("Segoe UI", 14), justify="center", bg="#0f172a", fg="#f8fafc", bd=0, highlightthickness=1,
                  highlightbackground="#334155", highlightcolor="#38bdf8")
entry1.pack(pady=(5, 15), ipady=8, fill="x")

# Input Box 2 Style
lbl2 = tk.Label(card, text="Second Number", font=("Segoe UI", 10), bg="#1e293b", fg="#94a3b8")
lbl2.pack(anchor="w", padx=5)
entry2 = tk.Entry(card, font=("Segoe UI", 14), justify="center", bg="#0f172a", fg="#f8fafc", bd=0, highlightthickness=1,
                  highlightbackground="#334155", highlightcolor="#38bdf8")
entry2.pack(pady=(5, 25), ipady=8, fill="x")

# Grid Frame for Buttons
btn_frame = tk.Frame(card, bg="#1e293b")
btn_frame.pack(fill="x", pady=5)

# Modern Styled Buttons (Hover effect ke sath)
button_config = {
    "font": ("Segoe UI", 11, "bold"),
    "fg": "white",
    "bd": 0,
    "height": 2,
    "activebackground": "#0284c7",
    "activeforeground": "white",
    "cursor": "hand2"
}

add_btn = tk.Button(btn_frame, text="Add", bg="#0284c7", **button_config, command=lambda: calculate("+"))
add_btn.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

sub_btn = tk.Button(btn_frame, text="Subtract", bg="#0284c7", **button_config, command=lambda: calculate("-"))
sub_btn.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

mul_btn = tk.Button(btn_frame, text="Multiply", bg="#0f766e", **button_config, command=lambda: calculate("*"))
mul_btn.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

div_btn = tk.Button(btn_frame, text="Divide", bg="#0f766e", **button_config, command=lambda: calculate("/"))
div_btn.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

# Make buttons look balanced
btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)

# Result Box Section
result_heading = tk.Label(card, text="Result", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="#64748b")
result_heading.pack(pady=(20, 2))

result_label = tk.Label(card, text="0", font=("Segoe UI", 24, "bold"), bg="#1e293b", fg="#38bdf8")
result_label.pack()

root.mainloop()