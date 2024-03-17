import tkinter as tk
from tkinter import ttk, messagebox  # Импорт дополнительных модулей из tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Импорт класса для встраивания графики Matplotlib в Tkinter
import matplotlib.pyplot as plt  # Импорт модуля Matplotlib
import pandas as pd  # Импорт модуля Pandas для работы с данными

# Функция, выполняемая при запуске программы
def main():
    global root  # Объявление переменной root как глобальной
    root = tk.Tk()  # Создание главного окна приложения
    root.title("Анализ уязвимостей")  # Установка заголовка окна
    apply_styles()  # Применение стилей к элементам интерфейса

    global frame  # Объявление переменной frame как глобальной
    frame = tk.Frame(root)  # Создание рамки для размещения элементов интерфейса
    frame.pack(padx=20, pady=20)  # Размещение рамки в главном окне с отступами

    # Создание и размещение метки и поля ввода для ключевого слова
    label_keyword = tk.Label(frame, text="Введите ключевое слово:")  # Создание метки
    label_keyword.grid(row=0, column=0, padx=10, pady=5)  # Размещение метки на сетке
    global entry_keyword  # Объявление переменной entry_keyword как глобальной
    entry_keyword = tk.Entry(frame, width=30)  # Создание поля ввода
    entry_keyword.grid(row=0, column=1, padx=10, pady=5)  # Размещение поля ввода на сетке
    entry_keyword.focus()  # Установка фокуса на поле ввода

    # Создание и размещение кнопки "Найти"
    global Button_find  # Объявление переменной Button_find как глобальной
    Button_find = tk.Button(frame, text='Найти', command=func_add)  # Создание кнопки с привязкой к функции func_add
    Button_find.grid(row=0, column=2, padx=10, pady=5)  # Размещение кнопки на сетке

    # Создание и размещение кнопки "Очистить"
    global Button_clear  # Объявление переменной Button_clear как глобальной
    Button_clear = tk.Button(frame, text='Очистить', command=clear_entry)  # Создание кнопки с привязкой к функции clear_entry
    Button_clear.grid(row=0, column=3, padx=10, pady=5)  # Размещение кнопки на сетке

    # Создание и размещение меток для вывода результатов анализа
    global label_result_K, label_result_K_R, label_result_H, label_result_H_R, label_result_S, label_result_S_R, label_result_L, label_result_L_R
    label_result_K = tk.Label(frame, text="Критический", width=20)  # Создание метки
    label_result_K.grid(row=1, column=0, padx=10, pady=5)  # Размещение метки на сетке
    label_result_K_R = tk.Label(frame, width=20, text='0')  # Создание метки
    label_result_K_R.grid(row=1, column=1, padx=10, pady=5)  # Размещение метки на сетке
    label_result_H = tk.Label(frame, text="Высокий", width=20)  # Создание метки
    label_result_H.grid(row=2, column=0, padx=10, pady=5)  # Размещение метки на сетке
    label_result_H_R = tk.Label(frame, width=20, text='0')  # Создание метки
    label_result_H_R.grid(row=2, column=1, padx=10, pady=5)  # Размещение метки на сетке
    label_result_S = tk.Label(frame, text="Средний", width=20)  # Создание метки
    label_result_S.grid(row=3, column=0, padx=10, pady=5)  # Размещение метки на сетке
    label_result_S_R = tk.Label(frame, width=20, text='0')  # Создание метки
    label_result_S_R.grid(row=3, column=1, padx=10, pady=5)  # Размещение метки на сетке
    label_result_L = tk.Label(frame, text="Низкий", width=20)  # Создание метки
    label_result_L.grid(row=4, column=0, padx=10, pady=5)  # Размещение метки на сетке
    label_result_L_R = tk.Label(frame, width=20, text='0')  # Создание метки
    label_result_L_R.grid(row=4, column=1, padx=10, pady=5)  # Размещение метки на сетке

    # Создание и размещение комбобокса для выбора типа графика
    global chart_type_combo  # Объявление переменной chart_type_combo как глобальной
    chart_type_combo = ttk.Combobox(frame, values=["Круговая", "Столбчатая"], width=20, state="readonly")  # Создание комбобокса
    chart_type_combo.grid(row=0, column=4, padx=10, pady=5)  # Размещение комбобокса на сетке
    chart_type_combo.current(0)  # Установка начального значения

    root.mainloop()  # Запуск главного цикла обработки событий

# Функция для применения стилей к элементам интерфейса
def apply_styles():
    root.option_add('*Font', 'Helvetica 12')  # Установка шрифта для всех элементов интерфейса
    root.option_add('*Background', 'white')  # Установка цвета фона
    root.option_add('*Foreground', '#333')  # Установка цвета текста
    root.option_add('*BorderWidth', 2)  # Установка ширины границ
    root.option_add('*Relief', 'groove')  # Установка вида границ

# Функция для выполнения анализа и вывода результатов
def func_add():
    try:
        keyword = entry_keyword.get().strip()  # Получение ключевого слова из поля ввода
        if not keyword:  # Если ключевое слово не введено
            messagebox.showwarning("Пустое ключевое слово", "Пожалуйста, введите ключевое слово для поиска.")
            return

        threat_count_low = 0  # Инициализация счетчиков угроз
        threat_count_medium = 0
        threat_count_high = 0
        threat_count_critical = 0

        df = pd.read_excel('vullist.xlsx', header=2)  # Загрузка данных из файла Excel

        # Поиск ключевого слова во всех столбцах DataFrame
        for index, row in df.iterrows():  # Перебор строк
            for column in df.columns:  # Перебор столбцов
                if keyword.lower() in str(row[column]).lower() and pd.notna(row['Уровень опасности уязвимости']):
                    if "Низкий" in row['Уровень опасности уязвимости']:
                        threat_count_low += 1
                    elif "Средний" in row['Уровень опасности уязвимости']:
                        threat_count_medium += 1
                    elif "Высокий" in row['Уровень опасности уязвимости']:
                        threat_count_high += 1
                    elif "Критический" in row['Уровень опасности уязвимости']:
                        threat_count_critical += 1
                    break  # Найдено совпадение, переходим к следующей строке

        # Обновление меток с количеством угроз
        label_result_K_R.config(text=str(threat_count_critical))
        label_result_H_R.config(text=str(threat_count_high))
        label_result_S_R.config(text=str(threat_count_medium))
        label_result_L_R.config(text=str(threat_count_low))

        # Создание и отображение графика в зависимости от выбранного типа
        if chart_type_combo.get() == "Круговая":
            create_pie_chart(threat_count_critical, threat_count_high, threat_count_medium, threat_count_low)
        elif chart_type_combo.get() == "Столбчатая":
            create_bar_chart(threat_count_critical, threat_count_high, threat_count_medium, threat_count_low)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Функция для создания кругового графика
def create_pie_chart(threat_count_critical, threat_count_high, threat_count_medium, threat_count_low):
    try:
        labels = ['Критический', 'Высокий', 'Средний', 'Низкий']
        counts = [threat_count_critical, threat_count_high, threat_count_medium, threat_count_low]
        fig, ax = plt.subplots()
        ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        plot_chart(fig)  # Отображение графика на интерфейсе
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Функция для создания столбчатого графика
def create_bar_chart(threat_count_critical, threat_count_high, threat_count_medium, threat_count_low):
    try:
        labels = ['Критический', 'Высокий', 'Средний', 'Низкий']
        counts = [threat_count_critical, threat_count_high, threat_count_medium, threat_count_low]
        fig, ax = plt.subplots()
        ax.bar(labels, counts, color=['red', 'orange', 'yellow', 'green'])
        plot_chart(fig)  # Отображение графика на интерфейсе
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Функция для отображения графика на интерфейсе
def plot_chart(fig):
    try:
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=2, rowspan=5, padx=10, pady=10)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Функция для очистки поля ввода
def clear_entry():
    entry_keyword.delete(0, tk.END)

# Запуск программы при запуске данного файла
if __name__ == "__main__":
    main()
