# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:50:25 2018

@author: Sergi
"""
def distance_to_line(x0, y0, x1, y1, x2, y2):
    """
    Calculates the distance from (x0,y0) to the 
    line defined by (x1,y1) and (x2,y2)
    """
    dx = x2 - x1
    dy = y2 - y1
    return abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / \
           math.sqrt(dx * dx + dy * dy)
           
# Libraries
import pandas as pd
import numpy as np
import datetime as datetime
from sklearn import model_selection
from sklearn.ensemble import ExtraTreesClassifier
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import pylab as pl
import cmath as math

# Read dataset
df = pd.read_csv('file.csv', sep = ";")
df.columns = map(str.upper, df.columns)
df['TARGET_V3'] = np.where(df['VL_SCORE_VOICE_LANDLINE']<=3, 1, 0)
print(df.DE_TIPO_PRODUCTO.value_counts())
df = df[df['DE_TIPO_PRODUCTO'] == "ADSL"]
df = df.reset_index()
del df['index']
date_format = "%Y-%m-%d"
df['DAYS_SINCE_LAST_RESET'] = df['DT_LAST_RESET'].map(lambda x: (datetime.datetime.strptime('2018-05-05', date_format)-datetime.datetime.strptime(x, date_format)).days, na_action = 'ignore')

# Remove variables
del df['DT_LAST_RESET']
del df['DE_TIPO_PRODUCTO']
del df['PORT_ADDRESS']
del df['VL_SCORE_VOICE_LANDLINE']
del df['VL_SCORE_INTERNET_LANDLINE']
del df['ID_LANDLINE_NUMBER']

# Input NA´s
print("Sum of NA´s before input "+ str(df.isnull().sum().sum()))
varsCharacter = []
for i in list(df):
    if df[i].dtype == "object":
        varsCharacter.append(i)
        df[i] = df[i].fillna(value="desconocido")
    else:
        df[i] = df[i].fillna(value=99999)
print("Sum of NA´s after input "+ str(df.isnull().sum().sum()))

# Created dummies
for i in list(df):
    if i in varsCharacter:
        for k in list(set(df[i])):
            varName = i + "_" + k
            df[varName] = df[i].apply(lambda x: 1 if x == k else 0)

df.drop(varsCharacter, inplace=True, axis=1)

# Development model
Vars = list(df)
Vars.remove("TARGET_V3")

X = df[Vars]
Y = df['TARGET_V3']
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# evaluate each model in turn
model = ExtraTreesClassifier()
model.fit(X_train, Y_train)
weightFeature = model.feature_importances_
varsModel = pd.DataFrame(Vars, columns=['Vars name'])
varsModel = pd.concat([varsModel, pd.DataFrame(weightFeature, columns=['weightFeature'])], axis=1)
varsModel = varsModel.sort_values('weightFeature', ascending = False)

# Clear environment
del X_train, X_validation, X, Y, Y_train, Y_validation, Vars, date_format, 

# Select best variables
numVars = 30
variablesFinal = list(varsModel.iloc[0:numVars, 0])

varsSelect  = []
dfResumen = pd.DataFrame()

for i in variablesFinal:
    print(i)
    varsSelect.append(i)
    numVarsSelect = len(varsSelect)

    # Normalizer 
    scaler = StandardScaler()
    dfScaler = df[varsSelect]
    X = scaler.fit_transform(dfScaler)

    # k means determine k
    distortions = []
    K = range(1,10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k).fit(X)
        kmeanModel.fit(X)
        distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    
    # Plot the elbow
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()
    
    # Determinate best k
    num = 0
    distanceSelect = 0
    for j in range(1, 8):
        distance = distance_to_line(K[j], distortions[j], K[0], distortions[0], K[8], distortions[8])
        if distanceSelect == 0:
            distanceSelect = distance
            num = K[j]
        else:
            if distanceSelect <= distance:
                distanceSelect = distance
                num = K[j]
            
    # Kmeans
    print("Number of cluster --> " + str(num))
    kmeans = KMeans(n_clusters=num, random_state=22).fit(X)
    centorids = kmeans.cluster_centers_
    
    # Predicting the clusters
    labels = pd.DataFrame(kmeans.predict(X), columns = ['Cluster'])
    dfTarget = pd.DataFrame(df.loc[:,'TARGET_V3'], columns = ['TARGET_V3'])
    dfTarget = pd.concat([dfTarget, labels], axis=1)
    numCluster = sorted(list(labels.Cluster.unique()), reverse=False)
    print(numCluster)
    
    for k in numCluster:
        data = dfTarget[dfTarget['Cluster'] == k]
        num0 = data.TARGET_V3.count() - data.TARGET_V3.sum()
        num1 = data.TARGET_V3.sum()
        prior = round(data.TARGET_V3.sum()/len(data.TARGET_V3) * 100, 2)
        variance = data.TARGET_V3.var()
        desvTipica = data.TARGET_V3.std()
        dfFinal = pd.DataFrame([[k, numVarsSelect, list(dfScaler), num0, num1, prior, variance, desvTipica]], 
                               columns=['Cluster', 'Num Vars', 'Variables selected', 'Num0', 'Num1', 'Prior', 'Variance', 'DesvTipica'])
        dfResumen = dfResumen.append(dfFinal, ignore_index=True)
