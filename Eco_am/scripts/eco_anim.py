import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

file = r'C:\Users\USER\Desktop\Eco_project\Eco_am\data\eco_rank.csv'
df = pd.read_csv(file)
print(df)

# Convert 'Ожидаемый возраст населения при рождении' column to float
df['Выделенный бюджет на защиту экологии'] = df['Выделенный бюджет на защиту экологии'].fillna(0).astype(int)
df['Год'] = df['Год'].fillna(0).astype(int)
print(df.dtypes)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(9, 16))

# Create a list of unique ranks from the 'ranks' column
ranks = df['ranks'].unique()

def animate(rank):
    ax.clear()
    filtered = df[df['ranks'] == rank]
    filt_areas = filtered[filtered['Регион'] != 'Республика Казахстан '].sort_values('Выделенный бюджет на защиту экологии')
    filt_areas.drop(filt_areas[filt_areas['Выделенный бюджет на защиту экологии'] == 0].index, inplace=True)
    plot = plt.barh(y=filt_areas['Регион'], width=filt_areas['Выделенный бюджет на защиту экологии'], color='#E6825D')

    ax.set_xlim(0, max(df['Выделенный бюджет на защиту экологии']))  # Adjust the limit based on your data range
    ax.bar_label(plot, padding=3, labels=[f'{value:.2f}' for value in filt_areas['Выделенный бюджет на защиту экологии']])

    for edge in ['top', 'right', 'bottom', 'left']:
        ax.spines[edge].set_visible(False)

    ax.tick_params(left=False)
    ax.get_xaxis().set_visible(False)
    
    year = filtered['Год'].iloc[0]
    ax.set_title(f'Выделенный бюджет на защиту экологии по Регионам на {year} год c прогнозом  ', size=18, weight='bold')

plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

# Define the range of ranks you want to animate
ranks_to_animate = range(df['ranks'].min(), df['ranks'].max() + 1)
animation = FuncAnimation(fig, animate, frames=ranks_to_animate, interval=25)

# Uncomment the next line if you want to save the animation as a GIF
# animation.save('population_animate.gif', dpi=100, writer=PillowWriter(fps=100))

plt.show()
