# Importation des biblithèques nécessaires
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn import metrics
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

#création d'un clusetr Kmean avec nombre de clusters 4
kmeans = KMeans(n_clusters = 5,max_iter = 100)
#Apprentissage (segmetation) (fonction fit)
kmeans.fit(data)
#Prédiction et enregistrement des labels 
labels = kmeans.predict(data)
#Affichage des labels
'''
print('score : %f' %labels)
'''
#enregistrement des centres des clusters
centres = kmeans.cluster_centers_
'''
print('centres : %f' %centres)
'''
#Calculer le score du modèle
kmean_score= metrics.silhouette_score(data,labels)
'''
print('score : %f' %kmean_score)
'''

# Créer un dataframe pour stocker les labels des clusters et les noms des utilisateurs
df = pd.DataFrame({'labels':labels,'users':data1['nom']}).sort_values(by=['labels'],axis = 0)
'''
print(df)
'''
# Convertir le dataframe en json 
donneesjson = df.to_json(orient="index")
parsed = json.loads(donneesjson)
json.dumps(parsed,indent=4)

'''
print(donneesjson)
users = json.loads(donneesjson)
for key in users:
    print(key, ":", users[key])
'''