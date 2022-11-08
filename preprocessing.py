import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

print("DATA PREPROCESSING", end='\n\n')

print("DATA FRAME 1: ", end='\n\n')
df1 = pd.read_csv('./data/_ASSOC_BGFriends_01.csv')
print(df1.head(10), end='\n\n')

print("DATA FRAME 2: ", end='\n\n')
df2 = pd.read_csv('./data/_ASSOC_BGFriends_02.csv')
print(df2.head(10), end='\n\n')

print("CONCATENATING THE DATAFRAMES: ", end='\n\n')
df = pd.concat([df1, df2])
print("FULL DATAFRAME: ", end='\n\n')
print(df.head(10), end='\n')
print('\t\t\t[...]')
print(df.tail(10), end='\n\n')

print("REINDEXING", end='\n\n')
df.set_index('Partida', inplace=True)
print(df.head(10), end='\n\n')

print("TAKING SPACES OUT: ", end='\n\n')
df['Jogadore(a)s'] = df['Jogadore(a)s'].str.replace(" ", "")
print(df.head(10), end='\n\n')

encoder = OneHotEncoder()
df_ = OneHotEncoder.fit_transform(df['Jogadore(a)s'])

#df.to_csv('./data/full.csv')
