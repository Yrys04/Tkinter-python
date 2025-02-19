import tkinter as tk
from tkinter import ttk
import math

class CustomCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Modern Calculator")
        self.geometry("350x500")
        self.config(bg="#222")
        self.result_var = tk.StringVar()

        # Поле ввода
        self.entry = ttk.Entry(self, textvariable=self.result_var, font=("Arial", 20), justify="right")
        self.entry.pack(fill="both", padx=10, pady=10, ipady=10)

        # Кнопки
        self.create_buttons()

    def create_buttons(self):
        button_frame = tk.Frame(self, bg="#222")
        button_frame.pack(fill="both", expand=True)

        buttons = [
            ("C", 1, 0, "red"), ("(", 1, 1, "#666"), (")", 1, 2, "#666"), ("/", 1, 3, "orange"),
            ("7", 2, 0, "#444"), ("8", 2, 1, "#444"), ("9", 2, 2, "#444"), ("*", 2, 3, "orange"),
            ("4", 3, 0, "#444"), ("5", 3, 1, "#444"), ("6", 3, 2, "#444"), ("-", 3, 3, "orange"),
            ("1", 4, 0, "#444"), ("2", 4, 1, "#444"), ("3", 4, 2, "#444"), ("+", 4, 3, "orange"),
            ("0", 5, 0, "#444"), (".", 5, 1, "#666"), ("=", 5, 2, "green"), ("√", 5, 3, "blue")
        ]

        for (text, row, col, color) in buttons:
            btn = tk.Button(button_frame, text=text, font=("Arial", 16), bg=color, fg="white",
                            width=5, height=2, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(6):
            button_frame.rowconfigure(i, weight=1)
            button_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.result_var.set("")
        elif char == "=":
            try:
                self.result_var.set(eval(self.result_var.get()))
            except:
                self.result_var.set("Ошибка")
        elif char == "√":
            try:
                self.result_var.set(math.sqrt(float(self.result_var.get())))
            except:
                self.result_var.set("Ошибка")
        else:
            self.result_var.set(self.result_var.get() + char)

if __name__ == "__main__":
    app = CustomCalculator()
    app.mainloop()
