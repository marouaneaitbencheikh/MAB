import pandas as pd # type: ignore

# a. Opérations arithmétiques sur les séries
serie1 = pd.Series([2, 4, 6, 8, 10])
serie2 = pd.Series([1, 3, 5, 7, 9])

print("Addition:", serie1 + serie2)
print("Soustraction:", serie1 - serie2)
print("Multiplication:", serie1 * serie2)
print("Division:", serie1 / serie2)

# b. Comparaison d'éléments
print("Éléments égaux:", serie1 == serie2)

# c. Conversion d'un dictionnaire en série
dico = {'a': 10, 'b': 20, 'c': 30}
serie = pd.Series(dico)
print(serie)

# d. Traitement d'un DataFrame
exam_data = {'Nom': ['Aziza', 'Dima', ...], 'score': [12.5, 9, ...]}
index = ['a', 'b', 'c', ...]
df = pd.DataFrame(exam_data, index=index)

# Nombre de lignes et de colonnes
print("Nombre de lignes:", df.shape[0])
print("Nombre de colonnes:", df.shape[1])

# Lignes où le score manque
print(df[df['score'].isnull()])

# Lignes où le score est entre 15 et 20
print(df[(df['score'] >= 15) & (df['score'] <= 20)])

# Somme des tentatives
print(df['attempts'].sum())