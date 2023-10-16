import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Read data from the first CSV file
df1 = pd.read_csv(r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\eco_drop_regr.csv')

# Read data from the second CSV file
df2 = pd.read_csv(r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_am\data\fin_eco_am.csv')

# Filter data for the first region from both CSV files
region_name = df1['Регион'].iloc[0]
df1_region = df1[df1['Регион'] == region_name]
df2_region = df2[df2['Регион'] == region_name]

# Convert the emissions column to float
df1_region['Выброс загрезнений(тыс.тонн)'] = df1_region['Выброс загрезнений(тыс.тонн)'].astype(float)
df2_region['Выделенный бюджет на защиту экологии'] = df2_region['Выделенный бюджет на защиту экологии'].astype(float)

# Create a figure and axis for the plot
fig, ax = plt.subplots()
plt.xticks(rotation=45)

# Initialize lines for both datasets
line1, = ax.plot([], [], lw=2, label=f'Data 1 - {region_name}')
line2, = ax.plot([], [], lw=2, linestyle='dashed', label=f'Data 2 - {region_name}')

# Function to initialize the plot
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Function to update the plot for each frame
def update(frame):
    years = df1_region['Год'][:frame+1]
    emissions1 = df1_region['Выброс загрезнений(тыс.тонн)'][:frame+1]
    emissions2 = df2_region['Выделенный бюджет на защиту экологии'][:frame+1]
    
    line1.set_data(years, emissions1)
    line2.set_data(years, emissions2)
    
    ax.set_xlim(min(years), max(years))
    ax.set_ylim(0, max(emissions1.max(), emissions2.max()) + 5)
    
    return line1, line2

# Create the animation
ani = FuncAnimation(fig, update, frames=len(df1_region), init_func=init, blit=True)

# Add legend
ax.legend(loc='upper left')

# Save the animation as a GIF or MP4
#ani.save('lineplot_comparison.gif', writer='pillow', fps=10)
# ani.save('lineplot_comparison.mp4', writer='ffmpeg', fps=10)

plt.show()
