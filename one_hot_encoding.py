import pandas as pd
import numpy as np


def one_hot_encoding(df=pd.DataFrame([]), column_to_be_encoded=''):

    if df.empty or column_to_be_encoded == '':
        return -1
    
    itr = 0
    for i in df[column_to_be_encoded]:
        itr += 1
        for j in df.columns:
            if(j in i):
                df[j][itr] = 1
