# Importation des biblithèques nécessaires
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn import metrics
import pickle
import json

# Importer les donnees fakeUsers depuis l'api laravel
'''
url =
'''
data1 = pd.read_table("FakeUsers.csv", sep=",")
data = data1.drop(['age', 'ville'], axis=1)

'''
print(data)
print(data.dtypes)
'''

#Labellisation des champ textes avec Encoder1
Encoder =preprocessing.LabelEncoder()
data["prenom"]=Encoder.fit_transform(data["prenom"])
data["nom"]=Encoder.fit_transform(data["nom"])

'''
data["ville"]=Encoder.fit_transform(data["ville"])
'''