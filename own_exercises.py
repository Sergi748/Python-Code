# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:08:48 2018

@author: NB23625
"""

pagina = "http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-1.html"

###############################################################################
# Ejercicio 1: Definir una función max() que tome como argumento dos números y 
# devuelva el mayor de ellos. (Es cierto que python tiene una función max() 
# incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
###############################################################################

def max(num_1, num_2):
    
    if num_1 > num_2:
        print(num_1)
    else:
        print(num_2)

a=max(9,7)


###############################################################################
# Ejercicio 2: Definir una función max_de_tres(), que tome tres números como 
# argumentos y devuelva el mayor de ellos. 
###############################################################################

lista_num = [5,34,3,56,23,2,67,8,98,9898]

def max_list(data):
    lista = data.copy()
    vector = 0
    for i in range(len(lista)):

        if lista[i] > vector:
          vector = lista[i]
        else:
          vector = vector
                
    return vector 

max_list(lista_num)

###############################################################################
# Ejercicio 3: Definir una función que calcule la longitud de una lista o una 
# cadena dada.(Es cierto que python tiene la función len() incorporada, 
# pero escribirla por nosotros mismos resulta un muy buen ejercicio.
###############################################################################

lista_num = [5,34,3,56,23,2,67,8,98,9898,989]

def longitud(lista):
    data = lista.copy()

    x = sum(1 for x in data)
    
    return x

longitud(lista_num)
                
###############################################################################
# Ejercicio 4: Escribir una función que tome un carácter y devuelva True 
# si es una vocal, de lo contrario devuelve False.
###############################################################################

lista_character = ["f", "R", "a", "E", "h", "S", "i"]

def vocal(lista):
    data = lista.copy()
    # Vocales del vocabulario
    vocales = ["a", "e", "i", "o", "u"]
    
    # Convertimos todas los string dados a minusculas
    data = [x.lower() for x in data]
    
    string = []
    indice = []
    for i in range(len(data)):
        if data[i] in vocales:
            string.append(data[i])
            indice.append(i)
        
    return string, indice
    
a, b = vocal(lista_character)
vocal(lista_character)         
        
###############################################################################
# Ejercicio 5: Escribir una funcion sum() y una función multip() que sumen y 
# multipliquen respectivamente todos los números de una lista. 
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) 
# debería devolver 24.
###############################################################################

date = [1,2,3,4]

class calculate:

    def suma(data):
        vector = 0
        for i in range(len(data)):
            vector = vector + data[i]
        
        return vector
    
    def multiplicacion(data):
        vector = 1
        for i in range(len(data)):
            vector = vector * data[i]
        
        return vector
            
calculate.suma(date)
calculate.multiplicacion(date)        
        
###############################################################################
# Ejercicio 6: Definir una función inversa() que calcule la inversión de una 
# cadena. Por ejemplo la cadena "estoy probando" debería devolver 
# la cadena "odnaborp yotse"
###############################################################################

cadena = "Holi how are you?"

def inverse(data):
    partes = data.split()
    result = []
    
    for i in reversed(range(len(partes))):
        string = partes[i]
        vacio = []
        
        for k in range(len(string)):
            letra = string[k]
            vacio.append(letra)
            str = ''.join(vacio[::-1]) # inverso de un string    
        
        result.append(str)
        
    return result 

inverse(cadena)

###############################################################################
# Ejercicio 7: Definir una función es_palindromo() que reconoce palíndromos
# (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo ("radar") tendría que devolver True.
###############################################################################
      
palabras = ["adios","oso", "radar", "sedes", "hola", "Sedes"]

def palindromo(cadena):
    cadena = [x.lower() for x in cadena]
    result = []
    
    for i in range(len(cadena)):
        palabra = cadena[i]
        new = []
        
        for k in range(len(palabra)):
            letra = palabra[k]
            new.append(letra)
            str = ''.join(new[::-1])
                        
        out = True if palabra == str else False
        result.append(out)
    
    return result

a = palindromo(palabras)

###############################################################################
# Ejercicio 8: Definir una función superposicion() que tome dos listas y 
# devuelva True si tienen al menos 1 miembro en común o devuelva False de 
# lo contrario. Escribir la función usando el bucle for anidado. 
###############################################################################

aa = ["adios","oso", "rAdar", "sedes"]
#lista1 = aa
bb = ["hola","oso", "raDar", "sedes", "adios", "coche"]
#lista2 = bb
cc = ["bebe","rico"]

def superposicion(lista1, lista2):
    lista1 = [x.lower() for x in lista1]
    lista2 = [x.lower() for x in lista2]
    
    lista = [lista1, lista2]
    result = []
    booleano = []
    
    for i in range(len(lista)):
        result_lista = []
        booleano_lista = []
        
        for k in range(len(lista[i])):
            if i != len(lista)-1:
                out = True if lista[i][k] in lista[i+1] else False
                name = lista[i][k]
                booleano_lista.append(out)
                result_lista.append(name)
            else:
                out = True if lista[i][k] in lista[i-1] else False
                name = lista[i][k]
                booleano_lista.append(out)
                result_lista.append(name)
    
        result.append(result_lista)    
        booleano.append(booleano_lista)
   
    return result, booleano


a, b = superposicion(aa, bb)
superposicion(aa, bb)

###############################################################################

aa = ["adios","oso", "rAdar", "sedes"]
#lista1 = aa
bb = ["hola","oso", "raDar", "sedes", "adios", "coche"]
#lista2 = bb
cc = ["bebe","rico"]
#lista_inicial = [aa,bb,cc]
dd = ["bebe","rico", "Coche", "nadar"]

def superposicion_new(*lista_inicial):
    lista = []    
    for l in range(len(lista_inicial)):
        a = [x.lower() for x in lista_inicial[l]]
        lista.append(a)

    result = []
    booleano = []

    for i in range(len(lista)):
        result_lista = []
        booleano_lista = []
        lista_def = lista.copy()
        del lista_def[i] #Eliminamos la lista en la que iniciamos el bucle
        
        for j in range(len(lista_def)):
            foo = []
            foh = []
            for k in range(len(lista[i])):
                out = True if lista[i][k] in lista_def[j] else False
                foo.append(out)
                foh.append(lista[i][k])
                
            booleano_lista.append(foo)
            result_lista.append(foh)
            
        booleano.append(booleano_lista)
        result.append(result_lista)
        
    return result, booleano

a, b = superposicion_new(aa, bb, cc, dd)
superposicion_new(aa, bb, cc, dd)
   
###############################################################################
# Ejercicio 9: Hacer unlist:
###############################################################################

lista = [[2, True, 9.7, [False, "foo", 3, 4], 'a'], 1, "foh", [5, ['b', True], 6, [7, [8, 9, 10]]], False]

def unlist(data):
    foh = []

    for i in range(len(data)):
        if type(data[i]) != list:
            foh.append(data[i])
        else:
            foh.extend(unlist(data[i]))

    return foh
    
unlist(lista)            
bb = unlist(lista)
aa = unlist(bb)


###############################################################################
# Ejercicio 10: Escribir una clase en python que convierta un número 
# romano a número entero
###############################################################################
def roman_number(x):
    
    number = x
    dicc = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"} 
    a = []
    for i in range(len(number)):
        for k in range(len(list(dicc.values()))):
            if number[i] == list(dicc.values())[k]:
                a.append(list(dicc.keys())[k])
    
    tipo_5 = ["5", "50", "500"]
    
    b = []
    vars_no = []
    if len(a) > 1:
        for k in range(len(a)):
            if a[k] != a[-1]:
                if a[k] < a[k+1]:
                    if a[k] not in tipo_5:
                        b.append(a[k+1]-a[k])
                        vars_no.append(a[k+1])
                    else:
                        if a[k] * 10 == a[k+1]:
                            b.append(a[k+1]-a[k])
                else:                
                    b.append(a[k])
            else:
                b.append(a[k])
                    
    result = sum(b)-sum(vars_no)
        
    return result

number = "MCMXXIX"
roman_number(number)

###############################################################################
# Escribe una función que lea las palabras de un archivo de texto (texto.txt) 
# y construya una lista donde cada palabra es un elemento de la lista.
###############################################################################

path = "C:\\Users\\NB23625\\Documents\\PRUEBAS PERSONALES\\8. Ejercicios python"
name = "prueba"

def readtxt(path, name):
    path = path
    name = name
    
    f = open(path + "\\" + str(name) + ".txt", "r")
    text = f.read()
    partes = text.split()
    
    return partes

readtxt(path, name)

###############################################################################
# Sacar el valor el mas alto posible de un input dado
###############################################################################

n = 8
#input = "4 9 8 . 8 5 2 -"
input = "0 0 0 1 0 0 0 ."
input = input.split()
input = sorted(input)

result = []
if "-" in input:
    result.append("-")
    input.remove("-")
    if "." in input:
        newlist = input.copy()
        newlist.remove(".")
        for i in range(len(newlist)):
            result.append(newlist[i])
        result.insert(2, ".")
        result = ''.join(result)
        if len(set(input[1:])) == 1 and list(set(input[2:]))[0] == '0':
            result = 0
        print(result)
    else:
        for i in range(len(input)):
            result.append(input[i])
        result = ''.join(result)
        print(result)
else:
    if "." in input:
        newlist = input.copy()
        newlist.remove(".")
        for i in range(len(newlist)):
            result.append(newlist[::-1][i])
        result.insert(len(result) -1 , ".")
        result = ''.join(result)    
        if len(set(input[len(result) -1:])) == 1 and '0' in list(set(input[len(result) -2:])):
            result = result[0:len(result) -2]
        print(result)    
    else:
        for i in range(len(input)):
            result.append(input[::-1][i])
        result = ''.join(result)
        print(result)
        
        
###############################################################################
#Binary with 0 and 1 is good, but binary with only 0, or almost, is even better! 
#Originally, this is a concept designed by Chuck Norris to send so called unary messages.
#
#Write a program that takes an incoming message as input and displays as output 
#the message encoded using Chuck Norris’ method.
#
# 	Rules
#Here is the encoding principle:
#
#The input message consists of ASCII characters (7-bit)
#The encoded output message consists of blocks of 0
#A block is separated from another block by a space
#Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
#- First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
#- Second block: the number of 0 in this block is the number of bits in the series
# 	Example
#Let’s take a simple example with a message which consists of only one character: 
#Capital C. C in binary is represented as 1000011, so with Chuck Norris’ technique this gives:
#
#0 0 (the first series consists of only a single 1)
#00 0000 (the second series consists of four 0)
#0 00 (the third consists of two 1)
#So C is coded as: 0 0 00 0000 0 00
###############################################################################

character = 'C'
result = []
output = ""
for l in range(len(character)):
    a = ord(character[l]) # 1000011
    
    for i in reversed(range(0, 7)):
        if a & (2 ** i) != 0:
            result.append("0")
        else:
            result.append("00")
    
    for k in range(len(result)):
        if k == 0:
            output = "0 0" if result[k] == "0" else "00 0"
        else:
            output = output + '0' if result[k] == result[k-1] else output + str(' ') + str(result[k]) + str(' 0') 
                    
print(output)


###############################################################################
# Your program must read the data from the standard input and write the 
# result on the standard output.
###############################################################################
input = "42 -5 12 21 5 24"

input = input.split()
result = ""

for i in range(len(input)):
    if i == 0:
        result = int(input[i])
    else:
        if abs(int(input[i])) <= abs(result):
            if result int(input[i]):result = int(input[i])
            
print(result)        

###############################################################################
# Your objective is to find the word that scores the most 
# points using the available letters (1 to 7 letters).
###############################################################################
#input = "because first these could which hicquwh"
input = "some first potsie day could postie from have back this sopitez"
#input = "qzyoq azejuy kqjsdh aeiou qsjkdh qzaeiou"
#input = "after repots user powers these time know from could people tsropwe"
input = input.split()

dicc = {"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":5,"l":1,"m":3,
        "n":1,"o":1,"p":3,"q":10,"r":1,"s":1,"t":1,"u":1,"v":4,"w":4,"y":4,"z":10}

elementkey = input[len(input) - 1]
dicckey = {}
for x in elementkey: dicckey.setdefault(x, elementkey.count(x))

count = []
word = []

for i in range(len(input)-1):
    element = input[i]
    dicc2 = {}
    a = 0
    for x in element: dicc2.setdefault(x, element.count(x))
    prueba = []
    for key in range(len(list(dicc2.keys()))):
        if list(dicc2.keys())[key] in list(dicckey.keys()) and list(dicc2.values())[key] <= dicckey.get(list(dicc2.keys())[key]):
           prueba.append("TRUE")
        else:
           prueba.append("FALSE")
    
    if "TRUE" in set(prueba) and len(set(prueba)) == 1:
        for k in range(len(list(set(element)))):
            if input[i][k] in input[len(input)-1]:
                for l in range(len(list(dicc.keys()))):
                    if input[i][k] == list(dicc.keys())[l]:
                        a = a + list(dicc.values())[l]
        word.append(input[i])
        count.append(a)

count_final = 0
result = []
for n in range(len(count)):
    if n == 0:
        count_final = count[n]
        result = word[n]
    else:
        if count[n] > count_final:
            count_final = count[n]
            result = word[n]
            
print(result)
