import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Load your two datasets into Pandas DataFrames with UTF-8 encoding
file1 = r"C:\Users\USER\Desktop\Eco_project\Eco_am\data\eco_rank.csv"
file2 = r'C:\Users\USER\Desktop\Eco_project\Eco_drop\data\eco_drop_rank.csv'
df1 = pd.read_csv(file1, encoding='utf-8')
df2 = pd.read_csv(file2, encoding='utf-8')

# Ensure the columns have appropriate data types (convert to float)
df1['Выделенный бюджет на защиту экологии'] = pd.to_numeric(df1['Выделенный бюджет на защиту экологии'], errors='coerce')
df2['Выброс загрезнений(тыс.тонн)'] = pd.to_numeric(df2['Выброс загрезнений(тыс.тонн)'], errors='coerce')

# Drop rows with NaN values
df1 = df1.dropna(subset=['Выделенный бюджет на защиту экологии'])
df2 = df2.dropna(subset=['Выброс загрезнений(тыс.тонн)'])

# Use the "ggplot" style
plt.style.use("ggplot")

fig, ax = plt.subplots(figsize=(9, 6))

ax.set_xlim(df1['Год'].min(), df1['Год'].max())
ax.set_ylim(df1['Выделенный бюджет на защиту экологии'].min(), df1['Выделенный бюджет на защиту экологии'].max())

x_values = []
y1_values = []
y2_values = []

def animate(i):
    x = df1['Год'].iloc[i]
    x_values.append(x)
    
    y1 = df1['Выделенный бюджет на защиту экологии'].iloc[i]
    y1_values.append(y1)

    y2 = df2['Выброс загрезнений(тыс.тонн)'].iloc[i]
    y2_values.append(y2)

    ax.clear()
    ax.plot(x_values, y1_values, label='Выделенный бюджет на экологию')
    ax.plot(x_values, y2_values, label='Выброс загрезнений(тыс.тонн)')

    ax.legend(loc='upper left')
    ax.set_xlabel('Год')
    ax.set_ylabel('Значение')
    ax.set_title(f'Сравнение данных по экологии за {x} год', size=17, weight='bold')

animation = FuncAnimation(fig, animate, frames=min(len(df1), len(df2)), interval=200)

plt.show()