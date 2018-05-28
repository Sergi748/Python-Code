# Library
import pandas as pd

# Path
path = "C:\\Users\\NB23625\\Documents\\PRUEBAS PERSONALES\\1. Titanic"
path_output = path + "\\" + "Resultados"

# Load data
tablon = pd.read_csv(path + "\\" + "train titanic.csv", sep = ";")

# Desarrollo
# Create variable with NA´s by row
tablon['Sum_NA'] = tablon.isnull().sum(axis=1)
# Input NA´s
vars_na = tablon.columns[tablon.isnull().any()].tolist()
for i in tablon.columns:
    if i in vars_na:
        if tablon[i].dtype != 'object':
            tablon[i].fillna(round(tablon[i].dropna().mean()), inplace=True)
        else:
            tablon[i].fillna(tablon[i].dropna().mode()[len(tablon[i].dropna().mode())-1], inplace=True)
            
del vars_na, i

# Add different variables in a table
tablon['Family'] = tablon['Parch'].apply(lambda x: 1 if x != 0 else 0)
tablon['Children'] = tablon['Age'].apply(lambda x: 1 if x < 12 else 0)

# Create dummies for variable
vars_dummy = ['Sex', 'Embarked']
for i in range(len(tablon.columns)):    
    if tablon.columns.values[i] in vars_dummy:
        for k in set(tablon.iloc[:,i]):
            name = tablon.columns.values[i] + "." + str(k)
            tablon[name] = tablon[tablon.columns.values[i]].apply(lambda x: 1 if x == k else 0)

vars_dummy.append('Name')
vars_dummy.append('Ticket')
tablon.drop(vars_dummy, axis=1, inplace=True)
del name, i, k, vars_dummy

# Grouped dummies of variable Cabin
tipos = tablon['Cabin'].apply(lambda x: x[0]).unique()
for i in tipos:
    tablon['Cabin'+'.'+i] = tablon['Cabin'].apply(lambda x: 1 if x[0] == i else 0)

del tipos, i
tablon.drop('Cabin', axis=1, inplace=True)

# Change '.' of Fare variable for nothing and created variable
tablon['Fare'] = pd.to_numeric(tablon['Fare'].apply(lambda x: str(x).replace('.', '')))
tablon['Fare_low'] = tablon['Fare'].apply(lambda x: 1 if x >= 0 and x <= 250000 else 0)
tablon['Fare_medium'] = tablon['Fare'].apply(lambda x: 1 if x > 250000 and x <= 1000000 else 0)
tablon['Fare_high'] = tablon['Fare'].apply(lambda x: 1 if x > 1000000 else 0)
tablon.drop('Fare', axis=1, inplace=True)

# Save table complete
tablon.to_csv(path_output + "\\" + "tablon_completo.csv")

