import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules


df = pd.read_csv('./data/full.csv').set_index('Partida')

print(df.head(10), end='\n\n')


# Building the model
frq_items = apriori(df, min_support = 0.05, use_colnames = True)
  
# Collecting the inferred rules in a dataframe
rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])

index = np.arange(len(rules.index))
rules['index'] = index
rules.set_index('index', inplace=True)
rules.to_csv("./data/rules.csv")

print(rules.head(100))