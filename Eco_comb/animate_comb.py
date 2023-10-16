import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

df_input = pd.read_csv(r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_comb\csv_comb.csv')

df = df_input[['Год', 'Выброс загрязнений(тыс.тонн)', 'Выделенный бюджет на защиту экологии']]
df = df.iloc[:51, :]
df['Год'] = df['Год'].astype(int)  # Convert the 'Год' column to integer
df['Выделенный бюджет на защиту экологии'] = df['Выделенный бюджет на защиту экологии'] * 1000
df['Выброс загрязнений(тыс.тонн)'] = df['Выброс загрязнений(тыс.тонн)'] * 1000

fig, ax1 = plt.subplots(2, 1, figsize=(10, 8))

# First subplot for 'Выброс загрязнений'
ax1[0].set_xlabel('Год')
ax1[0].set_ylabel('Выброс загрязнений (тонн)')
ax1[0].set_title('Выброс загрязнений по годам')
ax1[0].grid(True)

# Second subplot for 'Выделенный бюджет на защиту экологии'
ax1[1].set_xlabel('Год')
ax1[1].set_ylabel('Выделенный бюджет на защиту экологии (тенге)')
ax1[1].set_title('Выделенный бюджет на защиту экологии по годам')
ax1[1].grid(True)

x_data = df['Год']
y1_data = df['Выброс загрязнений(тыс.тонн)']
y2_data = df['Выделенный бюджет на защиту экологии']

# Interpolate more data points for smoother animation
x_interp = np.linspace(min(x_data), max(x_data), 100)
y1_interp = np.interp(x_interp, x_data, y1_data)
y2_interp = np.interp(x_interp, x_data, y2_data)

line1, = ax1[0].plot(x_interp, y1_interp, label='Выброс загрязнений')
line2, = ax1[1].plot(x_interp, y2_interp, label='Выделенный бюджет на защиту экологии')

# Format y-axis tick labels
ax1[0].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
ax1[1].get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

def update(frame):
    if frame < len(x_interp):
        line1.set_data(x_interp[:frame], y1_interp[:frame])
        line2.set_data(x_interp[:frame], y2_interp[:frame])
    return line1, line2

ani = FuncAnimation(fig, update, frames=len(x_interp), blit=True)
plt.tight_layout()
plt.show()