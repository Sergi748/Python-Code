# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:33:15 2018

@author: Sergio Campos
"""
# ---- Librerias ---- #
import numpy as np
import pandas as pd

tablon = np.array([["coche", "moto", "bici", "coche", "moto", "bici", "coche", "moto", "bici"], 
                    [1, 2, 3, 4, 5, 6, 7, 8, 9], 
                    [10, 11, 12, 13, 14, 15, 16, 17, 18], 
                    ["perro", "gato", "caballo", "perro", "gato", "caballo", "perro", "gato", "caballo"]])

tablon = tablon.transpose()
names = [_ for _ in 'abcd']
df2 = pd.DataFrame(tablon, columns = names)
df2['b'] = pd.to_numeric(df2['b'])
df2['c'] = pd.to_numeric(df2['c'])
vars = ['a', 'b']
#vars = False
remove = True

###############################################################################
###################### CREATED OF DUMMIES BASICS ##############################
###############################################################################

def createDummiesBasics(table):
    df = table.copy()
    for i in range(len(df.columns)):    
        if df.iloc[:,i].dtype == 'object':
            for k in set(df.iloc[:,i]):
                name = df.columns.values[i] + "." + str(k)
                df[name] = df[df.columns.values[i]].apply(lambda x: 1 if x == k else 0)

    return df

###############################################################################
###################### CREATED OF DUMMIES BY VARS #############################
###############################################################################

def createDummiesVars(table, vars = None):
    
    df = table.copy()
    for i in range(len(df.columns)):
        if vars != None:
            if df.columns.values[i] in vars:
                for k in set(df.iloc[:,i]):
                    name = df.columns.values[i] + "." + str(k)
                    df[name] = df[df.columns.values[i]].apply(lambda x: 1 if x == k else 0)
        else: 
            if df.iloc[:,i].dtypes == 'object':
                for k in set(df.iloc[:,i]):
                    name = df.columns.values[i] + "." + str(k)
                    df[name] = df[df.columns.values[i]].apply(lambda x: i if x == k else 0)
                
    return df

###############################################################################
################# CREATED OF DUMMIES BY VARS AND REMOVE #######################
###############################################################################
    
def createDummies(table, vars = None, remove = False):

    df = table.copy()
    vars_name = []
    
    for i in range(len(df.columns)):
        for i in range(len(df.columns)):
            if vars != None:
                if df.columns.values[i] in vars:
                    for k in set(df.iloc[:,i]):
                        name = df.columns.values[i] + "." + str(k)
                        df[name] = df[df.columns.values[i]].apply(lambda x: 1 if x == k else 0)
            else: 
                if df.iloc[:,i].dtypes == 'object':
                    vars_name.append(df.columns.values[i])
                    for k in set(df.iloc[:,i]):
                        name = df.columns.values[i] + "." + str(k)
                        df[name] = df[df.columns.values[i]].apply(lambda x: i if x == k else 0)
    
    if remove == True and vars != None:
        df.drop(vars, axis=1, inplace=True)
    elif remove == True and vars == None:
        df.drop(vars_name, axis=1, inplace=True)
    
    return df
        

a = createDummiesBasics(df2)
b = createDummiesVars(df2, vars)
c = createDummies(df2, vars, remove = True)
