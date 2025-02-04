import pandas as pd

HADS = 'HADS_Hospital_Anxiety_Depression_Scale (r‚ponses).xlsx'
df = pd.read_excel(HADS)
'1 create tuple for conversion'
'1.1: anxiété'
'some have repeats but with different scoring - must make one for each question'

'Je me sens tendu ou énervé.'
HADS1 = (
    ('Jamais', 0),
    ('Jamais - 0', 0),
    ('De temps en temps', 1),
    ('De temps en temps - 1', 1),
    ('Souvent', 2),
    ('Souvent - 2', 2),
    ('La plupart du temps', 3),
    ('La plupart du temps - 3', 3)
 )

'''J'ai une sensation de peur comme si quelque chose d'horrible allait m'arriver.'''
HADS2 = (
    ('Pas du tout', 0),
    ('Pas du tout - 0', 0),
    ('''Un peu mais cela ne m'inquiète pas''', 1),
    ('''Un peu mais cela ne m'inquiète pas - 1''', 1),
    ('''Oui, mais ce n'est pas trop grave''', 2),
    ('''Oui, mais ce n'est pas trop grave - 2''', 2),
    ('Oui, très nettement', 3),
    ('Oui, très nettement - 3', 3)
)

'''Je me fais du souci. '''
HADS3 = (
    ('Très occasionnellement', 0),
    ('Très occasionnellement - 0', 0),
    ('Occasionnellement', 1),
    ('Occasionnellement - 1', 1),
    ('Assez souvent', 2),
    ('Assez souvent - 2', 2),
    ('Très souvent', 3),
    ('Très souvent - 3', 3)
)

'''Je peux rester tranquillement assis à ne rien faire et me sentir décontracté. '''
HADS4 = (
    ('''Oui, quoi qu'il arrive''', 0),
    ('''Oui, quoi qu'il arrive - 0''', 0),
    ('''Oui, en général''', 1),
    ('''Oui, en général - 1''', 1),
    ('''Rarement''', 2),
    ('''Rarement - 2''', 2),
    ('Jamais', 3),
    ('Jamais - 3', 3)
)


'''J'éprouve des sensations de peur et j'ai l'estomac noué.'''
HADS5 = (
    ('Jamais', 0),
    ('Jamais - 0', 0),
    ('''Parfois''', 1),
    ('''Parfois - 1''', 1),
    ('''Assez souvent''', 2),
    ('''Assez souvent - 2''', 2),
    ('Très souvent', 3),
    ('Très souvent - 3', 3),
)

'''J'ai la bougeotte et n'arrive pas à tenir en place. '''
HADS6 = (
    ('Pas du tout', 0),
    ('Pas du tout - 0', 0),
    ('Pas tellement', 1),
    ('Pas tellement - 1', 1),
    ('Un peu', 2),
    ('Un peu - 2', 2),
    ('''Oui, c’est tout à fait le cas''', 3),
    ('''Oui, c’est tout à fait le cas - 3''', 3)
)

'''J'éprouve des sensations soudaines de panique. '''
HADS7 = (
    ('Jamais', 0),
    ('Jamais - 0', 0),
    ('''Pas très souvent''', 1),
    ('''Pas très souvent - 1''', 1),
    ('''Assez souvent''', 2),
    ('''Assez souvent - 2''', 2),
    ('Vraiment très souvent', 3),
    ('Vraiment très souvent - 3', 3)
)

'1.2: Dépression'
'some have repeats but with different scoring - must make one for each question'

'''Je prends plaisir aux mêmes choses qu'autrefois.'''
HADS8 = (
    ('Oui, tout autant', 0),
    ('Oui, tout autant - 0', 0),
    ('Pas autant', 1),
    ('Pas autant - 1', 1),
    ('Un peu seulement', 2),
    ('Un peu seulement - 2', 2),
    ('Presque plus', 3),
    ('Presque plus - 3', 3)
)

'''Je ris facilement et vois le bon côté des choses.'''
HADS9 = (
    ('Autant que par le passé', 0),
    ('Autant que par le passé - 0', 0),
    ('''Plus autant qu'avant''', 1),
    ('''Plus autant qu'avant - 1''', 1),
    ('''Vraiment moins qu'avant''', 2),
    ('''Vraiment moins qu'avant - 2''', 2),
    ('Plus du tout', 3),
    ('Plus du tout - 3', 3)
)

'''Je suis de bonne humeur.'''
HADS10 = (
    ('La plupart du temps', 0),
    ('La plupart du temps - 0', 0),
    ('Assez souvent', 1),
    ('Assez souvent - 1', 1),
    ('Rarement', 2),
    ('Rarement - 2', 2),
    ('Jamais', 3),
    ('Jamais - 3', 3)
)

'''J'ai l'impression de fonctionner au ralenti.'''
HADS11 = (
    ('''Jamais''', 0),
    ('''Jamais - 0''', 0),
    ('''Parfois''', 1),
    ('''Parfois - 1''', 1),
    ('''Très souvent''', 2),
    ('''Très souvent - 2''', 2),
    ('Presque toujours', 3),
    ('Presque toujours - 3', 3)
)

'''Je ne m'intéresse plus à mon apparence.'''
HADS12 = (
    ('''J'y prête autant d'attention que par le passé''', 0),
    ('''J'y prête autant d'attention que par le passé - 0''', 0),
    ('''Il se peut que je n'y fasse plus autant attention''', 1),
    ('''Il se peut que je n'y fasse plus autant attention - 1''', 1),
    ('''Je n'y accorde pas autant d'attention que je devrais''', 2),
    ('''Je n'y accorde pas autant d'attention que je devrais - 2''', 2),
    ('''Oui, c’est tout à fait le cas''', 3),
    ('''Oui, c’est tout à fait le cas - 3''', 3)
)

'''Je me réjouis d'avance à l'idée de faire certaines choses.'''
HADS13 = (
    ('''Autant qu'avant''', 0),
    ('''Autant qu'avant - 0''', 0),
    ('''Un peu moins qu'avant''', 1),
    ('''Un peu moins qu'avant - 1''', 1),
    ('''Bien moins qu'avant''', 2),
    ('''Bien moins qu'avant - 2''', 2),
    ('''Presque jamais''', 3),
    ('''Presque jamais - 3''', 3)
)

'''Je peux prendre plaisir à un bon livre ou à une bonne émission radio ou télévision'''
HADS14 = (
    ('Souvent', 0),
    ('Souvent - 0', 0),
    ('''Parfois''', 1),
    ('''Parfois - 1''', 1),
    ('''Rarement''', 2),
    ('''Rarement - 2''', 2),
    ('Très rarement', 3),
    ('Très rarement - 3', 3)
)

'2: convert tuples to dictionaries'
dHADS1 = dict(HADS1)
dHADS2 = dict(HADS2)
dHADS3 = dict(HADS3)
dHADS4 = dict(HADS4)
dHADS5 = dict(HADS5)
dHADS6 = dict(HADS6)
dHADS7 = dict(HADS7)
dHADS8 = dict(HADS8)
dHADS9 = dict(HADS9)
dHADS10 = dict(HADS10)
dHADS11 = dict(HADS11)
dHADS12 = dict(HADS12)
dHADS13 = dict(HADS13)
dHADS14 = dict(HADS14)

dHADS_list = [dHADS1, dHADS2, dHADS3, dHADS4, dHADS5, dHADS5, dHADS6, dHADS7,
              dHADS8, dHADS8, dHADS9, dHADS10, dHADS11, dHADS12, dHADS13, dHADS14]
'3: replace values'
print('begin replacement')
n = 1
i = 3
while i <= 16:
    df.iloc[:, i].replace(dHADS_list[n], inplace=True)
    '''when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' 
    or df[col] = df[col].method(value) instead
    
    FutureWarning: Downcasting behavior in `replace` is deprecated and will be removed in a future version. To retain the old behavior, explicitly call `result.infer_objects(copy=False)`. To opt-in to the future behavior, set `pd.set_option('future.no_silent_downcasting', True)`
  df.iloc[:, i].replace(dHADS_list[n], inplace=True)'''
    print(df.iloc[:,i])
    print(dHADS_list[n])
    i += 1
    n += 1
'''DataFrame indexing should be done using .iloc for specific row and column indices.'''
print(df.head())

'4: HADS score - sum of all values'
df['HADS score'] = df.sum(axis=1, numeric_only=True)
'''add new column into the df which adds all the values in the row - 
 numeric only not necessary as sum just takes existing values'''

'5 create a new excel file with the replaced values'
output = 'HADS modified.xlsx'
df.to_excel(output, index=False)
print('output complete')