
"""
Created on Fri Sep 14 12:36:13 2018

@author: Sergio Campos
"""
# Libraries
import pandas as pd
from sklearn import model_selection
from sklearn import linear_model 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

# Paths
path = ""
pathData = path + "/" + "Data"
pathOutput = path + "/" + "Resultados"

# Development
tablon = pd.read_csv(pathData + "/" + "tablon_completo.csv")
varsTablon = list(tablon)

# Count target
tablon['Survived'].value_counts()
varsNumeric = []
varsCharacter = []

# Check NA´s by column
for i in list(tablon):
    if tablon.loc[:,i].isnull().sum() > 0 and tablon.loc[:,i].dtypes in ["float64", "int64"]:
        print("Column name numeric -- > " + tablon.loc[:,i].name)
        varsNumeric.append(tablon.loc[:,i].name)
    elif tablon.loc[:,i].isnull().sum() > 0 and tablon.loc[:,i].dtypes == "object":
        print("Column name character -- > " + tablon.loc[:,i].name)
        varsCharacter.append(tablon.loc[:,i].name)
        
# We create a dictionary to inpute the NA´s of variables by mean or mode
meanNumeric = {}
modeCharacter = {}
for i in list(tablon):
    if i in varsNumeric:
        meanNumeric[tablon.loc[:,i].name] = round(tablon.loc[:,i].mean(), 2)
    elif i in varsCharacter:
        modeCharacter[tablon.loc[:,i].name] = tablon.loc[:,i].mode()[0]

tablon.isnull().sum().sum()

# Impute NA´s
for i in list(tablon):
    if i in meanNumeric.keys():
        varName = tablon.loc[:,i].name
        tablon[varName] = tablon[varName].fillna(meanNumeric.get(varName))
    elif i in modeCharacter.keys():
        varName = tablon.loc[:,i].name
        tablon[varName] = tablon[varName].fillna(modeCharacter.get(varName))

# Check number of NA´s in dataframe
tablon.isnull().sum().sum() == 0
# Remove columns that we will not use
tablon.drop(['Name', 'Ticket','Cabin'], inplace=True, axis=1)

# Create dummies of character variables
varsDummy = []
for i in list(tablon):
    if tablon.loc[:,i].dtypes == "object":
        varsDummy.append(tablon.loc[:,i].name)
        for k in list(set(tablon.loc[:,i])):
            name = tablon.loc[:,i].name + "." + k
            tablon[name] = tablon.loc[:,i].apply(lambda x: 1 if x == k else 0)

tablon.drop(varsDummy, inplace = True, axis = 1)
# Order column to put target in last position
orderVars = ['PassengerId','Pclass','Age','SibSp','Parch','Fare','Sex.male','Sex.female','Embarked.C','Embarked.Q','Embarked.S','Survived']
tablon = tablon[orderVars]

# Save dataframe in csv
tablon.to_csv(pathOutput + "/" + "trainTest.csv", index = False)

# Split-out validation dataset
array = tablon.values
X = array[:,0:11]
Y = array[:,11]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# evaluate each model in turn
model = linear_model.LogisticRegression()
model.fit(X_train, Y_train)
model.score(X_train, Y_train)

# Equation coefficient and Intercept
print("Coefficient: \n", model.coef_)
print("Intercept: \n", model.intercept_)

# Make predictions on validation dataset with LR
predictions_lr = model.predict(X_validation)
print(model.score(Y_validation, predictions_lr))
print(confusion_matrix(Y_validation, predictions_lr))
print(classification_report(Y_validation, predictions_lr))

# Meditions of model
auc = roc_auc_score(predictions_lr, Y_validation)
gini = (2*auc) - 1
