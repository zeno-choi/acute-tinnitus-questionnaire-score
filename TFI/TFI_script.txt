import pandas as pd

TFI_data = 'TFI_Tinnitus_Functional_Index (réponses).xlsx'
df = pd.read_excel(TFI_data)
print(df.head())

'A: call items 1 + 3 and convert the values'
'1: identify the columns'
Q1 = pd.Series(df['1. Pendant quel pourcentage de votre temps d’éveil avez-vous été CONSCIENT(E) DE vos acouphènes?'])
Q3 = pd.Series(df['3. Pendant quel pourcentage de votre temps d’éveil avez-vous été DÉRANGÉ(E) par vos acouphènes?'])
'right now, these are lists, must change to df using pd.Series()'

Percent_data = pd.concat([Q1, Q3], axis=1)
'''if we use =[Q1 + Q3] we would be making a list and NOT a df; therefore head wouldnt work. concat would be used
instead to keep it as a df, axis=1 means to concatenate along the columns; axis=0 would stack them one up another'''
print(Percent_data.head())

'2: create function to convert values in column'
'some data points have text; must remove the text '
'2.1: create tuple'
to_replace = (
    ('100% (Tout le temps)', 1.0),
    ('0% (À aucun moment)', 0)
)
'2.2: convert tuple to dictionary'
dict_replace = dict(to_replace)
'2.3: replace values'
Percent_data.replace(dict_replace, inplace=True)
'now change by multiplying by 10'
Percent_data = Percent_data.apply(lambda row: row*10, axis=1)
'''lambda will make it so that .apply will iterate over all the rows and since the values
that we want to modify are the only ones in this df, we can just multiply all rows by 10'''
print(Percent_data)

'3: replace values in df to new ones: assign columns of TFI with those from Percent_data'
df[['1. Pendant quel pourcentage de votre temps d’éveil avez-vous été CONSCIENT(E) DE vos acouphènes?',
    '3. Pendant quel pourcentage de votre temps d’éveil avez-vous été DÉRANGÉ(E) par vos acouphènes?']] = Percent_data

print(df.head())

'B:calculation of overall TFI scores'
'1: somes values contain qualitative measures to convert'
conversion = (
    ('0 (Absolument)', 0), ('10 (Pas du tout)', 10), ('0 (Très facile)', 0),
    ('10 (Impossible)', 10), ('0 (Pas du tout)', 0), ('10 (Totalement)', 10),
    ('0 (Jamais)', 0), ('10 (Toujours)', 10), ('0 (À aucun moment)', 0),
    ('10 (Tout le temps)', 10), ('0 (Pas du tout)', 0), ('10 (Totalement)', 10),
    ('10 (Extrêmement)', 10))
'2: convert tuple to dictionary'
dict_conversion = dict(conversion)
'3: replace values'
df.replace(dict_conversion, inplace=True)
print (df)

'4: overall score'
'4.1: sum of all questions'
df['TFI score'] = df.sum(axis=1, numeric_only=True)
print(df.head())
'4.2: divide by number of questions with valid answers = 25?'
'df = df[TFI score].apply(lambda row: [TFI score]/25, axis=1) - not good we already have the column named'
df['TFI score'] /= 25

'4.3: mulitply by 10'
'df = df[TFI score].apply(lambda row: [TFI score]*10, axis=1) - we already have it named'
df['TFI score'] *= 10
print (df.head())

'C: creation of subscales'
'C.1: creation of subscale scores'
'INTRUSIVE'
Q2 = pd.Series(df['2. Quel était le NIVEAU D’INTENSITÉ de vos acouphènes?'])
I = Percent_data.copy()
I.insert(1, '2. Quel était le NIVEAU D’INTENSITÉ de vos acouphènes?', Q2, True)
print(I.head())
'''DataFrame.insert(loc, column, value, allow_duplicates=_NoDefault.no_default);
when using insert, it operates in th eplace and doesn't return anything: it doesn't create
a new variable. Therfore assigning the operation as I will not create anything and leave none.
so I must copy the df and assign it to allow the .insert operation in another df.'''

try:
    'create list of rest of subscales: sense of control, cognitive, sleep disturbance, auditory, interference with relaxation'
    subscales=['Sc', 'C', 'Sl', 'A', 'R']
    'create dictionary to assign each value to a new dataframe'
    subscales_dict={}
    n = 7
    j = 0
    for j, subscale in enumerate(subscales):
        try:
            subscales_dict[subscale] = df.iloc[:, n:n + 3]
        except KeyError:
            print(f'Unable to create DataFrame for subscale {subscale}')
        n+=3
    print('subscales classed')
except:
    print('error')

# show the dataframes
for subscale, df_subscale in subscales_dict.items():
    print(f'\nDataFrame for subscale {subscale}:')
    print(df_subscale.head())
'''items in the subscales_dict dictionary. Subscale=name of the subscale + value (df_subscale)=associated dataframe
2nd line:will indicate name of the subscale; \n = creates new line under; f-string = embed value of subscale into string.'''

'quality of life reduced'
try:
    QOL = df[['19. Votre capacité à apprécier les ACTIVITÉS SOCIALES?',
        '20. Votre capacité à PROFITER DE LA VIE?',
        '21. Vos RELATIONS avec votre famille, vos amis et les autres personnes?',
        '''22. À quelle fréquence vos acouphènes vous ont-ils donné de la difficulté à faire votre TRAVAIL OU D'AUTRES TÂCHES (entretien de la maison, devoirs scolaires, soin des enfants ou autres)?''']]
    subscales_dict['QOL'] = QOL
except:
    print('no work')

'emotional stress'
try:
    E = df[['23. Dans quelle mesure vos acouphènes vous ont-ils rendu(e) ANXIEUX(SE) ou INQUIÈT(E)?',
        '24. Dans quelle mesure vous êtes-vous senti(e) INCOMMODÉ(E) ou CONTRARIÉ(E) à cause de vos acouphènes?',
        '25. Dans quelle mesure avez-vous été DÉPRIMÉ(E) à cause de vos acouphènes?']]
    subscales_dict['E'] = E
except:
    print('no work')

'C.2: CALCULATIONS OF SUBSCALES'
'add I to dictionary'
subscales_dict['I'] = I
mean_df = pd.DataFrame()

for subscale, df_subscale in subscales_dict.items():
    mean_df[subscale + '_Score'] = df_subscale.mean(axis=1) * 10
print(mean_df.head())

for column in mean_df.columns:
    df[column] = mean_df[column]
'''loop through each column and add each column to df'''

'D: create a new excel file with the replaced values'
output = 'TFI modified.xlsx'
df.to_excel(output, index=False)
print('output complete')
