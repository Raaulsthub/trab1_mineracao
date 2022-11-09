import pandas as pd
import numpy as np
from one_hot_encoding import one_hot_encoding


# importing
df1 = pd.read_csv('./data/_ASSOC_BGFriends_01.csv')
df2 = pd.read_csv('./data/_ASSOC_BGFriends_02.csv')

# concatenating
print("DATA FRAMES: ", end='\n\n')
df = pd.concat([df1, df2])
print(df.head(10), end='\n\n')

# fixing index problem
df.set_index('Partida', inplace=True)

# taking out spaces, taking out 'ç', making it all upercase
df['Jogadore(a)s'] = df['Jogadore(a)s'].str.replace(" ", "").str.upper().str.replace('Ç', 'C').str.replace('�', 'C')

# list of players for one hot encoding
players = ['STEEVE', 'FRANCOIS', 'ALONSO', 'JIMMY', 'RICK', 'YURIKO', 'BARBARA', 'SHELDA']

# making all one hot encoding columns equal to zero
for i in players:
    df[i] = np.zeros(len(df.index)).astype(int)

# aplying the one hot encoding function
one_hot_encoding(df, 'Jogadore(a)s')

df['Won'] = np.zeros(len(df.index)).astype(int)

itr = 0
while itr < len(df.index):
    itr += 1
    if df['Oponentes'][itr] < df['Amigos'][itr]:
        df['Won'][itr] = 1


df.to_csv('./data/full_withNames.csv')

df.drop(['Jogadore(a)s', 'Amigos', 'Oponentes'], axis=1, inplace=True)
print("DATA FRAME FINAL: ")
print(df.head(10), end='\n\n')

df.to_csv('./data/full.csv')

