import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Чтение данных из первого CSV-файла
df1 = pd.read_csv(r'C:/Users/USER/Desktop/Eco_project/eco-spendings-and-emissions/Eco_drop/data/eco_drop_regr.csv')

# Чтение данных из второго CSV-файла
df2 = pd.read_csv(r'C:/Users/USER/Desktop/Eco_project/eco-spendings-and-emissions/Eco_am/data/fin_eco_am.csv')

# Фильтрация данных для первого региона ("Республика Казахстан")
df1_kazakhstan = df1[(df1['Регион'] == 'Республика Казахстан')]

# Преобразование столбца с данными в числовой формат
df1_kazakhstan['Выброс загрезнений(тыс.тонн)'] = df1_kazakhstan['Выброс загрезнений(тыс.тонн)'].astype(float)

# Фильтрация данных для второго региона ("Республика Казахстан")
df2_kazakhstan = df2[(df2['Регион'] == 'Республика Казахстан')]

# Преобразование столбца с данными в числовой формат
df2_kazakhstan['Выделенный бюджет на защиту экологии'] = df2_kazakhstan['Выделенный бюджет на защиту экологии'].astype(float)

# Создание графика
fig, ax = plt.subplots(figsize=(9, 6))
ax.set_ylim(0, max(df1_kazakhstan['Выброс загрезнений(тыс.тонн)'].max(), df2_kazakhstan['Выделенный бюджет на защиту экологии'].max()) + 5)
ax.set_xlim(min(df1_kazakhstan['Год']), max(df1_kazakhstan['Год']))

x_1, y_1 = [], []
y2 = []

def animate(i):
    current_year = df1_kazakhstan['Год'].values[i]
    
    x_1.append(current_year)
    y_1.append(df1_kazakhstan[df1_kazakhstan['Год'] == current_year]['Выброс загрезнений(тыс.тонн)'].values[0])
    y2.append(df2_kazakhstan[df2_kazakhstan['Год'] == current_year]['Выделенный бюджет на защиту экологии'].values[0])

    ax.clear()
    ax.plot(x_1, y_1, 'bo-', label='Выброс загрезнений(тыс.тонн)')
    ax.plot(x_1, y2, 'ro--', label='Выделенный бюджет на защиту экологии')
    ax.set_ylim(0, max(max(y_1), max(y2)) + 5)
    ax.set_xlim(min(x_1), max(x_1))
    ax.legend(loc='upper left')
    ax.set_title(f'Сравнение для {current_year} (Республика Казахстан)', fontsize=16)
    ax.set_xlabel('Год', fontsize=12)
    ax.set_ylabel('Значение', fontsize=12)

animation = FuncAnimation(fig, animate, frames=len(df1_kazakhstan), interval=200)

# Раскомментируйте следующую строку для сохранения анимации в GIF-файл
# animation.save('lineplot_comparison.gif', writer=PillowWriter(fps=10))

plt.show()