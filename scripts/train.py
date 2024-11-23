import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score



#data loading and preparation

csv_file_path = "../data/mushrooms.csv" 

df = pd.read_csv(csv_file_path, sep=",") 

df.columns = df.columns.str.lower().str.replace('-', '_')

#retain behavior of .replace in future versions
pd.set_option('future.no_silent_downcasting', True)

df['class']= df['class'].replace({'p': 1, 'e': 0})

#splitting data 
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train['class'].values
y_test = df_test['class'].values

del df_full_train['class']
del df_test['class']

# convert to int
y_full_train = y_full_train.astype(int)
y_test = y_test.astype(int)

#one hot encoding
dicts_full_train = df_full_train.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(dicts_full_train)

dicts_test = df_test.to_dict(orient='records')
X_test = dv.transform(dicts_test)


#train final model

print('Training the final model')

final_model = LogisticRegression(C=1.0, random_state=42)
final_model.fit(X_full_train, y_full_train)

y_pred = final_model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred)
acc = accuracy_score(y_test, y_pred >= 0.5)

print(f'Accuracy: {acc}, AUC: {auc}')


#save the model

output_file = f'../models/mushroom_model.bin'
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, final_model), f_out)

print(f'The model is saved to {output_file}')