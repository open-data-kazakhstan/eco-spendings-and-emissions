import pandas as pd

# Загрузите оба CSV файла
file1 = r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\eco_drop_regr.csv'
file2 = r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_am\data\fin_eco_am.csv'

# Прочитайте данные из обоих файлов в два отдельных DataFrame
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Фильтруйте данные по региону "Республика Казахстан"
df1_filtered = df1[df1['Регион'] == 'Республика Казахстан']
df2_filtered = df2[df2['Регион'] == 'Республика Казахстан']

# Выберите последний столбец из df2_filtered
last_column = df2_filtered.iloc[:, -1]

# Объедините df1_filtered и последний столбец из df2_filtered
result = pd.concat([df1_filtered, last_column], axis=1)

# Сохраните объединенный DataFrame в новый CSV файл
result.to_csv(r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\csv_comb.csv', index=False)