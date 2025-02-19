import tkinter as tk

# Функция для вычисления результата
def calculate():
    try:
        num1 = float(entry1.get())  # Получаем первое число
        num2 = float(entry2.get())  # Получаем второе число
        operation = operation_var.get()  # Получаем выбранную операцию

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Ошибка: деление на 0"
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите корректные числа")

# Создаем основное окно
root = tk.Tk()
root.title("Калькулятор")

# Устанавливаем размер окна
root.geometry("400x300")  # Размер окна 400x300 пикселей
root.config(bg="#f0f0f0")  # Цвет фона окна

# Заголовок
label = tk.Label(root, text="Калькулятор", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#4CAF50")
label.grid(row=0, column=0, columnspan=4, pady=20)

# Поля ввода для чисел
entry1 = tk.Entry(root, font=("Arial", 14), width=10, bd=2, relief="solid", justify="center")
entry1.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, font=("Arial", 14), width=10, bd=2, relief="solid", justify="center")
entry2.grid(row=1, column=2, padx=10, pady=10)

# Переменная для арифметической операции
operation_var = tk.StringVar(root)

# Кнопки для выбора операции
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.config(font=("Arial", 14), width=5)
operation_menu.grid(row=1, column=1, padx=10, pady=10)

# Кнопка для вычисления
calc_button = tk.Button(root, text="Вычислить", command=calculate, font=("Arial", 14), bg="#4CAF50", fg="white", bd=0, relief="solid", width=20)
calc_button.grid(row=2, column=0, columnspan=4, pady=20)

# Метка для вывода результата
result_label = tk.Label(root, text="Результат: ", font=("Arial", 16), bg="#f0f0f0", fg="#333")
result_label.grid(row=3, column=0, columnspan=4, pady=10)

# Запускаем главный цикл
root.mainloop()