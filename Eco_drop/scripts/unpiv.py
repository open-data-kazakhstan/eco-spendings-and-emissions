import pandas as pd
import numpy as np

# Read the initial 
csv = r"C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\part2.csv"
df = pd.read_csv(csv)
df.columns = df.columns.astype(str)
pd.set_option('display.max_columns', None)

# Unpivot the Excel data for CSV export
df_unpivot = pd.melt(df, id_vars='Unnamed: 0', value_vars=[ '2005.0', '2006.0',
                                                           '2007.0', '2008.0', '2009.0', '2010.0', '2011.0', '2012.0', '2013.0',
                                                           '2014.0', '2015.0', '2016.0', '2017.0', '2018.0', '2019.0', '2020.0',
                                                           '2021.0', '2022.0'])
df_unpivot.rename(columns={"Unnamed: 0": "Регион", "variable": "Год", "value": "Выброс загрязнений(тыс.тонн)"}, inplace=True)
df_unpivot.replace("-", np.nan, inplace=True)
df_unpivot.dropna(axis=0, inplace=True)
df_unpivot = df_unpivot.applymap(lambda x: int(x) if isinstance(x, str) and x.isdigit() else x)


print(df_unpivot)

data_types = df_unpivot.dtypes
print(data_types)

# Export to kazpop.csv
df_unpivot.to_csv(r'C:\Users\USER\Desktop\Eco_project\eco-spendings-and-emissions\Eco_drop\data\unpiv_part2.csv', index=False)