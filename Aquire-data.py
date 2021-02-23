import pandas as pd
import numpy as np
kek = pd.read_csv("botresponses.csv", na_values='thisisnotadrill')
print(kek)
stimulus = []
response = []
whatsaid = ""
num = 0
usertoclone = 'Fakeuser#1234'
#get responses
for i in range(1, int(kek.shape[0])):                     
    if kek.loc[i,'Author'] == usertoclone: 
       if type(kek.loc[i-1,'Content']) is float:
           whatsaid += (str(kek.loc[i-1,'Attachments']))
       else:          
        whatsaid += (str(kek.loc[i-1,'Content']))
    if whatsaid != "":
        stimulus.append(str(whatsaid))
    whatsaid = ""
#get answer
for i in range(0, kek.shape[0]):                     
    if kek.loc[i,'Author'] == usertoclone: 
        if type(kek.loc[i,'Content']) is float:
           whatsaid += (str(kek.loc[i,'Attachments']))
        else:          
            whatsaid += (str(kek.loc[i,'Content']))
        if i < int(kek.shape[0]-1):
            if kek.loc[i+1,'Author'] == usertoclone: 
               if type(kek.loc[i+1,'Content']) is float:
                   whatsaid += (str(kek.loc[i+1,'Attachments']))
               else:          
                whatsaid += (str(kek.loc[[i+1],'Content']))
    if whatsaid != "":
        response.append(str(whatsaid))
    whatsaid = ""

#print(response)
f = open('training-data.txt', 'a')
h = open('training-stimuli.txt', 'a')
j = open('training-responses.txt', 'a')
if len(stimulus) > len(response): 
    for i in range(len(response)):
        print(stimulus[i], file= f)
        print(response[i], file= f)
        print(stimulus[i], file= h)
        print(response[i], file= j)
else: 
    for i in range(len(stimulus)):
        print(stimulus[i], file = f)
        print(response[i], file = f)
        print(stimulus[i], file = h)
        print(response[i], file = j)
#       if kek.loc[i-1,'Author'] == usertoclone:

    
