import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = r'C:\Users\USER\Desktop\Eco_project\Eco_drop\data\unpiv_part2.csv'
df_1 = pd.read_csv(file)

file2 = r'C:\Users\USER\Desktop\Eco_project\Eco_drop\data\eco_drop_regr.csv'
df_2 = pd.read_csv(file2)
df_2 = df_2.loc[df_2['Год'] > 2022]

df = pd.concat([df_1,df_2])

df['Выброс загрезнений(тыс.тонн)'] = df['Выброс загрезнений(тыс.тонн)'].fillna(0).astype('int')
df = df.replace(to_replace='Северо-Казахстанская', value='СКО')
df = df.replace(to_replace='Западно-Казахстанская', value='ЗКО')
df = df.replace(to_replace='Восточно-Казахстанская', value='ВКО')
df = df.replace(to_replace='г. Астана', value='Астана')
df = df.replace(to_replace='г. Алматы', value='Алматы')
df = df.replace(to_replace='г. Шымкент', value='Шымкент')
df = df.replace(to_replace='Туркестанская 1', value='Туркестанская')
df = df.replace(to_replace='СевероКазахстанская', value='СКО')
df = df.replace(to_replace='ЗападноКазахстанская', value='ЗКО')
df = df.replace(to_replace='ВосточноКазахстанская', value='ВКО')

def ml_new_regions(region_to_test, region_predict):
    df_vko = df.loc[df['Регион'] == region_to_test]
    df_vko = df_vko.loc[df_vko['Год'] < 2021]
    values = df_vko['Выброс загрезнений(тыс.тонн)'].values.tolist()
    k = 0
    c = 0
    for i in range(1, len(values)-1):
        x_avg_1 = 0
        y_avg_1 = 0
        for k in range(0,i+1):
            x_avg_1 = (x_avg_1 + values[k])/i+1
            y_avg_1 = (y_avg_1 + values[k+1])/i+1
        k = (values[i]-x_avg_1)*(values[i+1]-y_avg_1)/((values[i]-x_avg_1))**2 + k
        c = y_avg_1 - ((values[i]-x_avg_1)*(values[i+1]-y_avg_1)/((values[i]-x_avg_1))**2)*x_avg_1 + c
    k_final = k/(len(values)-1)
    c_final = c/(len(values)-1)
    list_res = []
    list_yrs = []
    filtered_df = df.loc[(df['Регион'] == region_predict) & (df['Год'] == 2021), 'Выброс загрезнений(тыс.тонн)']
    x = filtered_df.iloc[0] if not filtered_df.empty else 0

    for i in range (2023, 2051):
        y = x*k_final + c_final
        list_res.append(y)
        x = y
        list_yrs.append(i)
    kval = 0
    for i in list_yrs:
        df['Выброс загрезнений(тыс.тонн)'] = np.where((df['Регион'] == region_predict) & (df['Год'] == i), list_res[kval], df['Выброс загрезнений(тыс.тонн)'])
        kval = kval +1

df_final = df[0:0]
regions = []
for i in df['Регион']:
    if i not in regions:
        regions.append(i)
for i in regions:
    df_1 = df.loc[df['Регион'] == i]
    df_1 = df_1.reset_index()
    df_1.index = df_1.index*10
    last_idx = df_1.index[-1] + 1
    df_expanded = df_1.reindex(range(last_idx))
    df_expanded['Год'] = df_expanded['Год'].fillna(method='ffill')
    df_expanded['Регион'] = df_expanded['Регион'].fillna(method='ffill')
    df_expanded = df_expanded.interpolate()
    df_final = pd.concat([df_final, df_expanded])

df1 = df_final
li = []
ranks = []
df1 = df1.sort_values(by=['Год', 'Регион', 'Выброс загрезнений(тыс.тонн)'], ascending=[True, True, True])
for i in df1['Регион']:
    if i not in li:
        ranks.append(1)
        li.append(i)
    else:
        x = 1
        for k in li:
            if k == i:
                x = x +1
        ranks.append(x)
        li.append(i)
df1['ranks'] = ranks

df1['Выброс загрезнений(тыс.тонн)'] = df1['Выброс загрезнений(тыс.тонн)'].fillna(0).astype('int')
df1['Год'] = df1['Год'].fillna(0).astype('int')
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15,8))
df1.to_csv(r'C:\Users\USER\Desktop\Eco_project\Eco_drop\data\eco_drop_rank.csv') 