# Приложение "Анализ уязвимостей"

## Введение

Приложение "Анализ уязвимостей" разработано для анализа данных об уязвимостях программного обеспечения, предоставляемых в виде Excel-файла, с возможностью визуализации результатов в виде круговых или столбчатых диаграмм. Приложение предоставляет пользователю интерфейс для ввода ключевого слова для поиска и анализа данных, а также выбора типа графика.

## Основные функции

### Запуск приложения

При запуске приложения пользователю отображается графический интерфейс, включающий поле ввода ключевого слова, кнопку "Найти" для запуска анализа, кнопку "Очистить" для очистки поля ввода, а также метки и график для отображения результатов анализа.

### Анализ данных

После ввода ключевого слова и нажатия кнопки "Найти" приложение анализирует данные из Excel-файла, ищет совпадения с ключевым словом во всех столбцах и подсчитывает количество уязвимостей различных уровней опасности.

### Отображение результатов

Результаты анализа отображаются в виде численных значений на графическом интерфейсе, а также в виде круговой или столбчатой диаграммы в зависимости от выбора пользователя.

### Выбор типа графика

Пользователь может выбрать тип графика (круговая или столбчатая диаграмма) с помощью выпадающего списка.

### Очистка поля ввода

Пользователь может очистить поле ввода ключевого слова, нажав на кнопку "Очистить".

## Технические детали

### Используемые библиотеки

Приложение использует следующие библиотеки:
- `tkinter` - для создания графического интерфейса;
- `matplotlib` - для создания и отображения графиков;
- `pandas` - для работы с данными из Excel-файла.

### Стилизация

Графический интерфейс приложения стилизован с использованием стандартных настроек для шрифтов, цветов и границ.

### Обработка ошибок

При возникновении ошибок во время выполнения анализа данных или отображения графика, пользователю выводится сообщение об ошибке.


# Использование класса `VulnerabilityAnalyzer`

Для более организованного и модульного кода в приложении был добавлен класс `VulnerabilityAnalyzer`. Этот класс инкапсулирует все функциональности анализа уязвимостей, включая создание графического интерфейса, анализ данных и отображение результатов.

## Атрибуты класса

- `root`: Главное окно приложения tkinter.
- `frame`: Основной фрейм для размещения виджетов.
- `label_keyword`: Метка для отображения текста "Введите ключевое слово:".
- `entry_keyword`: Поле ввода для ввода ключевого слова.
- `Button_find`: Кнопка для запуска анализа данных.
- `Button_clear`: Кнопка для очистки поля ввода.
- `label_result_K`, `label_result_K_R`, `label_result_H`, `label_result_H_R`, `label_result_S`, `label_result_S_R`, `label_result_L`, `label_result_L_R`: Метки для отображения результатов анализа уязвимостей различных уровней опасности.
- `chart_type_combo`: Выпадающий список для выбора типа графика.

## Методы класса

- `__init__(self, master)`: Конструктор класса, инициализирующий основные элементы интерфейса и устанавливающий обработчики событий.
- `apply_styles(self)`: Метод для применения стилей к элементам интерфейса.
- `func_add(self)`: Метод для анализа данных и обновления интерфейса в соответствии с результатами.
- `create_pie_chart(self, threat_count_critical, threat_count_high, threat_count_medium, threat_count_low)`: Метод для создания круговой диаграммы на основе результатов анализа.
- `create_bar_chart(self, threat_count_critical, threat_count_high, threat_count_medium, threat_count_low)`: Метод для создания столбчатой диаграммы на основе результатов анализа.
- `plot_chart(self, fig)`: Метод для отображения графика на интерфейсе.
- `clear_entry(self)`: Метод для очистки поля ввода ключевого слова.

## Использование класса в `main()`

Функция `main()` создает экземпляр класса `VulnerabilityAnalyzer` и запускает главный цикл обработки событий, что позволяет пользователю взаимодействовать с приложением.

Таким образом, в документации теперь также отражены изменения, связанные с использованием класса `VulnerabilityAnalyzer`.


## Переменные

- `root`: Главное окно приложения tkinter.
- `frame`: Основной фрейм для размещения виджетов.
- `label_keyword`: Метка для отображения текста "Введите ключевое слово:".
- `entry_keyword`: Поле ввода для ввода ключевого слова.
- `Button_find`: Кнопка для запуска анализа данных.
- `Button_clear`: Кнопка для очистки поля ввода.
- `label_result_K`, `label_result_K_R`, `label_result_H`, `label_result_H_R`, `label_result_S`, `label_result_S_R`, `label_result_L`, `label_result_L_R`: Метки для отображения результатов анализа уязвимостей различных уровней опасности.
- `chart_type_combo`: Выпадающий список для выбора типа графика.
- `df`: Объект DataFrame из библиотеки pandas, хранящий данные из Excel-файла.

## Функции 

1. **main()**:
   - Эта функция является точкой входа в программу. Она создает главное окно приложения, устанавливает заголовок окна, применяет стили к элементам интерфейса, размещает виджеты на форме (метки, поля ввода, кнопки, комбобокс), и запускает главный цикл обработки событий.

2. **apply_styles()**:
   - Эта функция применяет стили ко всем элементам интерфейса, таким как шрифт, цвет фона, цвет текста, ширина границ и вид границ.

3. **func_add()**:
   - Эта функция выполняет анализ данных и выводит результаты на интерфейс. Она получает ключевое слово из поля ввода, ищет совпадения в данных, обновляет метки с количеством угроз, а также создает и отображает график в зависимости от выбранного типа.

4. **create_pie_chart(threat_count_critical, threat_count_high, threat_count_medium, threat_count_low)**:
   - Эта функция создает круговую диаграмму на основе переданных количеств угроз разных уровней, а затем отображает эту диаграмму на интерфейсе.

5. **create_bar_chart(threat_count_critical, threat_count_high, threat_count_medium, threat_count_low)**:
   - Эта функция создает столбчатую диаграмму на основе переданных количеств угроз разных уровней, а затем отображает эту диаграмму на интерфейсе.

6. **plot_chart(fig)**:
   - Эта функция отображает переданный график на интерфейсе при помощи библиотеки Matplotlib.

7. **clear_entry()**:
   - Эта функция очищает поле ввода ключевого слова.

Эти описания помогут пользователям лучше понять, как работает ваше приложение и какие функции оно предоставляет.


### Методы и атрибуты

#### Методы
`fig, ax = plt.subplots()` - это вызов функции `subplots()` из библиотеки `matplotlib.pyplot`, который создает объекты `Figure` (рисунок) и `Axes` (оси) для построения графика. 

- `fig` представляет собой контейнер для всех элементов рисунка, таких как оси, текст и другие.
- `ax` представляет собой область координат, на которой будут нарисованы данные.

Этот вызов часто используется для создания графиков в Matplotlib. После его выполнения, `fig` и `ax` могут использоваться для настройки внешнего вида графика и добавления данных на график.

- `focus()`: Метод, используемый для установки фокуса на виджет. В данном приложении он используется для установки фокуса на поле ввода `entry_keyword`.
- Методы виджета `Grid`.
- Методы и атрибуты Combobox.

## Заключение

Приложение "Анализ уязвимостей" обеспечивает удобный способ анализа данных об уязвимостях программного обеспечения и предоставляет возможность визуализации результатов для более наглядного представления информации.
