import pandas as pd

df = pd.read_csv('production.csv')

нові_рядки = pd.DataFrame([[None]*df.shape[1]]*3, columns=df.columns)
df = pd.concat([df, нові_рядки], ignore_index=True)

df.to_csv('all.csv', index=False)
