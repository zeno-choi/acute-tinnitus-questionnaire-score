import pandas as pd

Khal = 'HQ_Khalfa.xlsx'
df = pd.read_excel(Khal, header=0)

'1: convert scoring'
'1.1: dictionary for the corresponding results'
Khal_scoring = {
    'Non': 0,
    'Oui, un peu': 1,
    'Oui, modérément': 2,
    'Oui, beaucoup': 3
}

'1.2: convert the results in the df'
df.replace(Khal_scoring, inplace=True)
print(df.head())

'2: add the Khal score'
df['score'] = df.sum(axis=1, numeric_only=True)
print(df.head())

'3: classify based on categories'
# 3.1 Attentional
'[Vous arrive-t-il d’utiliser des bouchons, boules quiès ou casque, pour limiter votre perception du bruit?]'
'[Avez-vous des difficultés à ne plus faire attention aux sons qui vous entourent dans la vie quotidienne?]'
'[Êtes-vous incommodé(e) pour lire dans un environnement bruyant?]'
'[Êtes-vous incommodé(e) pour vous concentrer dans un milieu bruyant?]'
try:
    att_cols = [4, 5, 6, 7]
    df['attentionnel'] = df.iloc[:, att_cols].sum(axis=1, numeric_only=True)
except Exception as e:
    print(f'Error in attentional: {e}')
'''e = assigns the exception instance to the variable

KeyError: Raised when a dictionary key is not found.
ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
TypeError: Raised when an operation or function is applied to an object of an inappropriate type.
AttributeError: Raised when an attribute reference or assignment fails.
IOError: Raised when an input/output operation fails, such as reading or writing to a file.

Error in attentional: "None of [Index(['[Vous arrive-t-il d’utiliser des bouchons, boules quiès ou casque, pour limiter votre perception du bruit?]',
'[Avez-vous des difficultés à ne plus faire attention aux sons qui vous entourent dans la vie quotidienne?]',
'[Êtes-vous incommodé(e) pour lire dans un environnement bruyant?]',
'[Êtes-vous incommodé(e) pour vous concentrer dans un milieu bruyant?]'],dtype='object')] are in the [columns]"'''

# 3.2 Social
'[Éprouvez-vous des difficultés pour entendre une conversation au milieu d’un environnement bruyant?]'
'[Certaines personnes de votre entourage vous ont-elles déjà fait remarquer que vous supportiez mal le bruit ou certains sons?]'
'[Êtes-vous particulièrement sensible, voire incommodé(e) par le bruit de la rue?]'
'[Le bruit dans certaines situations sociales (ex : boîtes de nuit, bars, concerts, cocktails,…) vous est-il pénible?]'
'[Si l’on vous propose une activité (sortie, cinéma, concert,…), pensez-vous tout de suite au bruit que vous aurez à supporter?]'
'[Vous arrive-t-il de refuser des invitations ou des sorties par crainte du bruit que vous aurez à affronter?]'
try:
    soc_cols = [8, 9, 10, 11, 12, 13]
    df['social'] = df.iloc[:, soc_cols].sum(axis=1, numeric_only=True)
except Exception as e:
    print(f'Error in social: {e}')

# 3.3 Emotional
'[Est-ce qu’un bruit ou un son précis vous dérange plus dans une atmosphère silencieuse que dans une pièce légèrement bruyante?]'
'[Votre capacité de concentration dans le bruit est-elle diminuée par le stress et la fatigue?]'
'[Votre capacité de concentration dans le bruit est-elle diminuée en fin de journée?]'
'[Est-ce que le bruit ou certains sons vous stressent ou vous énervent?]'
try:
    emo_cols = [14, 15, 16, 17]
    df['emotionnel'] = df.iloc[:, emo_cols].sum(axis=1, numeric_only=True)
except Exception as e:
    print(f'Error in emotional: {e}')


# 4. Create a new excel file with the replaced values
output = 'Khalifa_modified.xlsx'
df.to_excel(output, index=False)
print('Output complete')