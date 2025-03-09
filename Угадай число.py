import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Угадай число")
        self.root.geometry("300x200")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Угадай число от 1 до 100!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Попробовать", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Новая игра", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess < self.number_to_guess:
                messagebox.showinfo("Результат", "Загаданное число больше!")
            elif user_guess > self.number_to_guess:
                messagebox.showinfo("Результат", "Загаданное число меньше!")
            else:
                messagebox.showinfo("Победа!", f"Вы угадали число за {self.attempts} попыток!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите число!")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.label.config(text="Угадай число от 1 до 100!")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()