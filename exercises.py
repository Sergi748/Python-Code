
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

#page = "https://www.codingame.com/training/easy/chuck-norris"
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
# page = "https://www.codingame.com/training/medium/scrabble"
input = "because first these could which hicquwh"
#input = "some first potsie day could postie from have back this sopitez"
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
