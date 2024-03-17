import tkinter as tk
import pandas as pd

root = tk.Tk()

label_result_K = tk.Label(root, bg='green', fg='white', text="Критический", width=20)
label_result_K_R = tk.Label(root, bg='black', fg='white', width=20, text='0')
label_result_H = tk.Label(root, bg='green', fg='white', width=20, text='Высокий')
label_result_H_R = tk.Label(root, bg='black', fg='white', width=20, text='0')
label_result_S = tk.Label(root, bg='green', fg='white', text="Средний", width=20)
label_result_S_R = tk.Label(root, bg='black', fg='white', width=20, text='0')
label_result_L = tk.Label(root, bg='green', fg='white', text="Низкий", width=20)
label_result_L_R = tk.Label(root, bg='black', fg='white', width=20, text='0')

def func_add():
    # try:
        keyword = "Windows"  # Ключевое слово для поиска
        threat_count_low = 0
        threat_count_medium = 0
        threat_count_high = 0
        threat_count_critical = 0

        # Читаем данные из файла Excel в DataFrame
        df = pd.read_excel('vullist.xlsx', header=2)  # Начинаем чтение с третьей строки (индекс 2)

        # Подсчитываем количество уязвимостей каждого уровня опасности
        for index, row in df.iterrows():
            print(df.columns.tolist())
            software_name = str(row['Название ПO']).split()[0]  # Берем первое слово из названия ПО
            print(software_name)
            if keyword in software_name and pd.notna(row['Уровень опасности уязвимости']):
                if "Низкий" in row['Уровень опасности уязвимости']:
                    threat_count_low += 1
                elif "Средний" in row['Уровень опасности уязвимости']:
                    threat_count_medium += 1
                elif "Высокий" in row['Уровень опасности уязвимости']:
                    threat_count_high += 1
                elif "Критический" in row['Уровень опасности уязвимости']:
                    threat_count_critical += 1

        # Обновляем текст меток с количеством угроз
        label_result_K_R['text'] = str(threat_count_critical)
        label_result_H_R['text'] = str(threat_count_high)
        label_result_S_R['text'] = str(threat_count_medium)
        label_result_L_R['text'] = str(threat_count_low)

   # except Exception as e:
       # print(f"Ошибка: {e}")

# Привязываем функцию к событию нажатия кнопки
Button_add = tk.Button(root, text='Найти', command=func_add)

label_result_K.pack()
label_result_K_R.pack()
label_result_H.pack()
label_result_H_R.pack()
label_result_S.pack()
label_result_S_R.pack()
label_result_L.pack()
label_result_L_R.pack()
Button_add.pack()

root.mainloop()
