import pandas as pd
import numpy as np
from one_hot_encoding import one_hot_encoding

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

# taking out spaces, taking out 'ç', making it all upercase
print("FORMATING STRING COLUMN ", end='\n\n')
df['Jogadore(a)s'] = df['Jogadore(a)s'].str.replace(" ", "").str.upper().str.replace('Ç', 'C').str.replace('�', 'C')
print(df.head(10), end='\n\n')

players = ['STEEVE', 'FRANCOIS', 'ALONSO', 'JIMMY', 'RICK', 'YURIKO', 'BARBARA', 'SHELDA']

print("ADDING ONE HOT ENCODING COLUMNS: ")
for i in players:
    df[i] = np.zeros(len(df.index)).astype(int)
print(df.head(10), end='\n\n')

print('ONE HOT ENCODING: ', end='\n\n')
one_hot_encoding(df, 'Jogadore(a)s')
print(df.head(10), end='\n\n')

print("MAKING A WON/LOST COLUMN", end='\n\n')
df['Won'] = np.zeros(len(df.index)).astype(int)
df['Lost'] = np.ones(len(df.index)).astype(int)

itr = 0
while itr < len(df.index):
    itr += 1
    if df['Oponentes'][itr] < df['Amigos'][itr]:
        df['Won'][itr] = 1
        df['Lost'][itr] = 0




print(df.head(10), end='\n\n')

df.to_csv('./data/full_withNames.csv')

df.drop(['Jogadore(a)s', 'Amigos', 'Oponentes'], axis=1, inplace=True)
print("DATA FRAME FINAL: ")
print(df.head(10), end='\n\n')

df.to_csv('./data/full.csv')
