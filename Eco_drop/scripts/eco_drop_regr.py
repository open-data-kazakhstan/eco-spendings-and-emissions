import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


data = pd.read_csv(r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\unpiv_part2.csv')


grouped_data = data.groupby('Регион')


models = {}
predictions = {}


for area, area_data in grouped_data:
    X = area_data['Год'].values.reshape(-1, 1)
    y = area_data['Выброс загрязнений(тыс.тонн)'].values

    
    model = LinearRegression()

    
    model.fit(X, y)

    
    models[area] = model

    
    future_years = np.arange(2023, 2051).reshape(-1, 1)

    
    predicted_populations = model.predict(future_years)

    
    predictions[area] = predicted_populations


predictions_df = pd.DataFrame()


predictions_df['Год'] = np.arange(2023, 2051)


for area, area_data in grouped_data:
    area_predictions = predictions[area]
    predictions_df[area] = area_predictions


predictions_df = predictions_df.melt(id_vars='Год', var_name='Регион', value_name='Выброс загрязнений(тыс.тонн)')
combined_df = pd.concat([data, predictions_df], ignore_index=True)

df_sorted = combined_df.sort_values(by=['Год'])


df_sorted.to_csv(r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\eco_drop_regr.csv')