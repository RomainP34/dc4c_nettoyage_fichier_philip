import pandas as pd

df = pd.read_csv('C:/Users/bruno/Desktop/Python/test.csv')

df = df.drop(columns=['Series_reference'])

df = df.drop(columns=['Suppressed'])

df = df.drop(columns=['STATUS'])

df = df.drop(columns=['UNITS'])

df = df.drop(columns=['Magnitude'])

df = df.drop(columns=['Subject'])

df = df.drop(columns=['Group'])

df = df.drop(columns=['Series_title_1'])

df = df.drop(columns=['Series_title_3'])

df = df.drop(columns=['Series_title_4'])

df = df.drop(columns=['Series_title_5'])

df.dropna(inplace=True)

df.insert(0, 'id', range(1, 1 + len(df)))

df = df[df.Series_title_2.isin(['Credit', 'Debit', 'Services'])]

df.to_csv('result.csv', index=False)




