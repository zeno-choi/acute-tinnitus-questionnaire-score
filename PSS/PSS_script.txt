import pandas as pd

PSS = 'PSS_Perceived_Stress_Scale (réponses).xlsx'
df = pd.read_excel(PSS)

'''cotation
(0 = Jamais, 1 =Presque jamais, 2 =Parfois, 3 =Assez souvent, 4 = Très souvent). 
Inversions : ítems 4, 5, 6, 7, 9, 10, 13 (0=4, 1=3, 2=2, 3=1 y 4=0) et somme des 14 items.
'''

'questions for conversion'
df_convert = df.iloc[:, [3, 4, 5, 10, 13, 14, 16]].copy()

conversion = (
    ('Jamais', 0), ('Presque jamais', 1), ('Parfois', 2), ('Assez souvent', 3), ('Très souvent', 4))
conversion_dict = dict(conversion)

df_convert.replace(conversion_dict, inplace=True)

'questions for inversion'
df_invert = df.iloc[:, [6, 7, 8, 9, 11, 12, 15]].copy()
'''SettingWithCopyWarning, is due to the replace function being applied to a slice of the DataFrame (df_convert). 
Use the copy method to explicitly create a copy of the DataFrame.'''

inversion = (
    ('Jamais', 4), ('Presque jamais', 3), ('Parfois', 2), ('Assez souvent', 1), ('Très souvent', 0))
inversion_dict = dict(inversion)

df_invert.replace(inversion_dict, inplace=True)

'replace values in df with conversion and inversion'

for column in df_convert.columns:
    df[column] = df_convert[column]

for column in df_invert.columns:
    df[column] = df_invert[column]
'''DeprecationWarning: In a future version, `df.iloc[:, i] = newvals` will attempt to set the values 
inplace instead of always setting a new array. To retain the old behavior, use either `df[df.columns[i]] = newvals` 
or, if columns are non-unique, `df.isetitem(i, newvals)` df.loc[:, df_invert.columns] = df_invert'''
print(df.head())

'PSS score'
df['PSS SCORE'] = df.sum(axis=1, numeric_only=True)

'output in excel'
output = 'PSS modified.xlsx'
df.to_excel(output, index=False)
print('output complete')



