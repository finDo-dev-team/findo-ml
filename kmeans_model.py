# Importation des biblithèques nécessaires
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn import metrics
import json

# Importer les donnees fakeUsers depuis l'api laravel
'''
url =
data = pd.DataFrame(url)
'''
data = pd.read_table("fakeUsers(1).csv", sep=",")
dataWithEncoder = data.drop(['id','prenom','nom'], axis=1)

'''
#print(dataWithEncoder)
'''

#Labellisation des champ textes avec Encoder1
Encoder =preprocessing.LabelEncoder()
dataWithEncoder["ville"]=Encoder.fit_transform(dataWithEncoder["ville"])
'''
#dataWithEncoder["prenom"]=Encoder.fit_transform(dataWithEncoder["prenom"])
#dataWithEncoder["nom"]=Encoder.fit_transform(dataWithEncoder["nom"])
'''


#création d'un clusetr Kmeans avec nombre de clusters 4
kmeans = KMeans(n_clusters = 4 )
#Apprentissage fonction fit)
kmeans.fit(dataWithEncoder)
#Prédiction et enregistrement des labels 
labels = kmeans.predict(dataWithEncoder)
#Affichage des labels
'''
print('labels:')
print(labels)
'''
#enregistrement des centres des clusters
centres = kmeans.cluster_centers_
'''
print('centres:')
print(centres)
'''
#Calculer le score du modèle
kmean_score= metrics.silhouette_score(dataWithEncoder,labels)

print('score : %f' %kmean_score)


# Créer un dataframe pour stocker les labels des clusters et les noms des utilisateurs
df = pd.DataFrame({'labels':labels,'users':data['nom']}).sort_values(by=['labels'],axis = 0)
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