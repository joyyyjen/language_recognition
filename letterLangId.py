#!/usr/local/bin/python3
import sys
import codecs
from string import printable
from collections import Counter
#import nltk

#--- TRAIN FUNCTION ---#
def spliter(text):
    bimap = list()
    unimap = list()
    for i in range(0,len(text)-2):
        if text[i:1] =="\n": break
        unimap.append(text[i:i+1])
        unimap.append(text[i+1:i+2])
        bimap.append(text[i:i+2])
    return bimap,unimap

def frequency(text):
    freq2 = Counter()
    for pair in text:
        freq2[pair] += 1
    return freq2


def trainProc(string):
    list_2, list_1 = spliter(string)
    s = list(set(list_1))
    # ---- CREATE BIGRAM 
    freq_1 = frequency(list_1)
#    print(freq_1)
    for x in s:
        freq_1[x] += 1
#    print(freq_1)
    freq_2 = frequency(list_2)
    s2 = list(set(list_2))
    for x in s2:
        freq_2[x] += 1
     
    return freq_2,freq_1

# ---- TEST FUNCTION----#
#count the possibility that j | ij
def possibilities(j,i,freq_2,freq_1):
     str_1 =  i+j
     if j not in freq_1 or i not in freq_1: return 0.00001
     else:
         try:
             if str_1 in freq_2: poss = float(freq_2[str_1])/float(freq_1[j])
             else: poss = 1/float(freq_1[j])
         except:
#            print("****"+i+" "+j+"****")
#            print("Error")     
             return 1
     #tostr = i+j+str(freq_2[str_1]) +  " " + str(freq_1[j]) + ": "+ str(poss)
     #print(tostr)
     return poss

#count sentence p
def test(sentences,freq_2,freq_1):
    sum = 1
    for i in range(1,len(sentences)):
        possibility = possibilities(sentences[i],sentences[i-1],freq_2,freq_1)
        sum = sum * possibility
    return sum

     
if __name__ =="__main__":

# ---- TRAIN FRENCH
    text = codecs.open("LangId.train.French",'r',encoding='cp1252')
    string = text.read()
#    print("---TRAIN FRENCH---")
    mapF,freq_1F = trainProc(string)
   
# ---- TRAIN ENGLISH
    text = codecs.open("LangId.train.English",'r', encoding='utf-8')
    string = text.read()
#    print("---TRAIN ENGLISH---")
    mapE,freq_1E = trainProc(string)

# ---- TRAIN ITALIAN
    text = codecs.open("LangId.train.Italian",'r', encoding='cp1252')
    string = text.read()
#    print("---TRAIN ITALIAN---")
    mapI,freq_1I = trainProc(string)
   

#---- TEST PROCESS:
    test1 = "Reprise de la session"
    test3 = "Although , as you will have seen , the dreaded - 'millennium bug' - failed to materialise , still the people in a number of countries suffered a series of natural disasters that truly were dreadful ."
# ---- WHAT LANGAUGE AM I?
    """        
    if len(test1) > 100: test1 = test1[0:100]
    print("English:")
    possE = test(test1,mapE,freq_1E)
    print(possE)
    print("French")
    possF = test(test1, mapF,freq_1F)
    print("Italian:")
    possI = test(test1, mapI,freq_1I)
    if possE == 0.0 and  possF == 0.0 and possI == 0.0: print("cannot identified") 
    else: 
        ans = max(possE,possF,possI)
        if ans == possE: print("English")
        elif ans == possF: print("French")
        elif ans == possI: print("Italian-win")
    print(str(possE)+" "+str(possF)+" "+str(possI))
    """   
# ---- PROVIDE TEST
       
    #print("---TEST TEST FILE---")
    sentences = list()
    line_n=0
    text = codecs.open("LangId.test",'r', encoding='cp1252')
    string = text.read().splitlines()
    output = open("letterLangId.out",'w')
    
    for line in string:
        if len(line) > 100: line=line[0:100]
        line_n = line_n + 1
        possE = test(line,mapE,freq_1E)
        possF = test(line, mapF,freq_1F)
        possI = test(line, mapI,freq_1I)
        if possE == 0.0 and  possF == 0.0 and possI == 0.0: output.write(str(line_n)+": cannot identified\n")
        else:
            ans = max(possE,possF,possI)
            if ans == possE: output.write(str(line_n)+" English\n")
            elif ans == possF: output.write(str(line_n)+" French\n")
            elif ans == possI: output.write(str(line_n)+" Italian\n") 
     


