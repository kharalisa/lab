import tkinter as tk
from tkinter import ttk, messagebox
from itertools import product

# Функция генерации всех комбинаций из '1' и '7', сумма которых не превышает max_sum
# Возвращает список всех подходящих комбинаций и лучшую из них по сумме

def optimized_method(K, max_sum):
    nums = [(''.join(p), sum(int(d) for d in p)) for p in product('17', repeat=K) if sum(int(d) for d in p) <= max_sum]
    return nums, max(nums, key=lambda x: x[1]) if nums else None

# Обработчик кнопки: извлекает ввод, вызывает генерацию, выводит результат

def generate_numbers():
    output_text.delete('1.0', tk.END)
    try:
        k = int(entry_k.get())
        max_sum = int(entry_max_sum.get())
        if k <= 0 or max_sum < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите положительные целые числа для K и суммы")
        return

    all_combinations, best = optimized_method(k, max_sum)
    if all_combinations:
        output_text.insert(tk.END, f"Найдено подходящих комбинаций: {len(all_combinations)}\n\n")
        for num, s in all_combinations:
            output_text.insert(tk.END, f"Число: {num}, Сумма: {s}\n")
        output_text.insert(tk.END, f"\nОптимальное число: {best[0]} (Сумма: {best[1]})\n")
    else:
        output_text.insert(tk.END, "Нет подходящих чисел\n")

# --- Интерфейс ---

root = tk.Tk()
root.title("Оптимизированный генератор нечётных восьмеричных чисел")

# Применение темы оформления
style = ttk.Style()
style.theme_use('clam')

# Ввод: поле K и max_sum
frame_input = ttk.Frame(root, padding="10 10 10 10")
frame_input.pack(pady=15, padx=20)

label_k = ttk.Label(frame_input, text="Введите значение K (разрядность):", font=("Arial", 12))
label_k.pack(side=tk.LEFT, padx=5)

entry_k = ttk.Entry(frame_input, width=10, font=("Arial", 12))
entry_k.pack(side=tk.LEFT, padx=5)

label_max_sum = ttk.Label(frame_input, text="Максимальная сумма цифр:", font=("Arial", 12))
label_max_sum.pack(side=tk.LEFT, padx=5)

entry_max_sum = ttk.Entry(frame_input, width=10, font=("Arial", 12))
entry_max_sum.pack(side=tk.LEFT, padx=5)

# Кнопка запуска генерации
button_generate = ttk.Button(frame_input, text="Сгенерировать", command=generate_numbers)
button_generate.pack(side=tk.LEFT, padx=5)

# Вывод: текстовое поле с прокруткой
frame_output = ttk.Frame(root, padding="10 10 10 10")
frame_output.pack(pady=15, padx=20)

scrollbar = ttk.Scrollbar(frame_output)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(frame_output, wrap=tk.WORD, height=20, width=80, bg="lightyellow", font=("Courier", 10), yscrollcommand=scrollbar.set)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=output_text.yview)

# Запуск приложения
root.mainloop()

