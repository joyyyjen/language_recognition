#!/usr/local/bin/python3
#Author: Joy Jen, netid: yjen2
import sys
import codecs
from collections import Counter
from nltk import word_tokenize
import re

def spliter(text,unimap,bimap):
    for i in range(0,len(text)-2): 
        if text[i:1] =="\n": break
        unimap.append(text[i:i+1])
        bimap.append(text[i:i+2])
    return bimap,unimap
def frequency(text):
    freq = Counter()
    for i in text:
        freq[i] += 1
    return freq

def trainProc(string):
    list_1 = list()
    list_2 = list()
    for line in string:
        line = line.strip()
        line = "$"+line+"$"
        words = word_tokenize(line)
        list_2,list_1 = spliter(words,list_1,list_2)
    #print(list_2)  
    list_uni = list()
    list_bi = list()
    for i in list_1: 
        j = str(i)
        j = j[2:len(j)-2]
        list_uni.append(j)
    for j in list_2:
        k = str(j)
        k = k[2:len(k)-2]
        k = re.sub("',\s'"," ",k)
        list_bi.append(k)
   # print(list_bi)
    s = list(set(list_uni))
    s2 = list(set(list_bi))

    freq_1 = frequency(list_uni)
    for x in s: freq_1[x] += 1
    freq_2 = frequency(list_bi)
    for x in s2: freq_2[x] += 1 
    return freq_2,freq_1

def possibilities(j,i,freq_2,freq_1):
     str_1 = i+j
     if j not in freq_1 or i not in freq_1: 
          #print("not in freq_1:"+j)
         return 0.00001 
     else:
         try:
             if str_1 in freq_2: poss = float(freq_2[str_1])/float(freq_1[j])
             else: poss = 1/float(freq_1[j])
         except:
             #print("****"+i+" "+j+"****")
             #print("Error")     
             return 1
     #print(map[i][j])
     #print(freq_1[j])
     if str_1 in freq_2: tostr = i+j+str(freq_2[str_1]) +  " " + str(freq_1[j]) + ": "+ str(poss)
     else: tostr = i+j+ "1 " + str(freq_1[j]) + ": "+ str(poss)
#     print(tostr)
     return poss

#count sentence p
def test(sentences,freq_2,freq_1):
    sum = 1
    #min =100
    words = word_tokenize(sentences)
    for i in range(1,len(words)):
    #    print(words[i],words[i-1])
        possibility = possibilities(words[i],words[i-1],freq_2,freq_1)
        #if possibility < min and possibility != 0.0: min=possibility
        sum = sum * possibility
    #print("min:"+str(min))
    return sum


if __name__ =="__main__":

    
    text = codecs.open("LangId.train.French",'r',encoding='cp1252')
    string = text.read().splitlines()
#    print("---TRAIN FRENCH---")
    mapF,freq_1F = trainProc(string)
    
    #print("here:"); print(map["A"]["p"])
# ---- TRAIN ENGLISH
    text = codecs.open("LangId.train.English",'r', encoding='utf-8')
    string = text.read().splitlines()
#    print("---TRAIN ENGLISH---")
    mapE,freq_1E = trainProc(string)


# ---- TRAIN ITALIAN
   
    text = codecs.open("LangId.train.Italian",'r', encoding='cp1252')
    string = text.read().splitlines()
#    print("---TRAIN ITALIAN---")
    mapI,freq_1I = trainProc(string)
 
#---- TEST PROCESS:
    #tiest1 = "Pourquoi est - ce arrivé - ? "
    test3 = "Although , as you will have seen , the dreaded - 'millennium bug' - failed to materialise , still the people in a number of countries suffered a series of natural disasters that truly were dreadful ."
    testP = ["Pourquoi est - ce arrivé - ? ","Pourquoi - ?"]
#    testP = ["Resumption of the session","Perché non esistono istruzioni da seguire in caso di incendio ?","If the House agrees , I shall do as Mr Evans has suggested .","Des décisions existent qui s ' opposent à une telle taxe ."]
# ---- WHAT LANGAUGE AM I?
    """
    for line in testP:    
        if len(line) > 100: line = line[0:100]
        print("English:")
        possE = test(line,mapE,freq_1E)
        print("French")
        possF = test(line, mapF,freq_1F)
        print("Italian:")
        possI = test(line, mapI,freq_1I)
        if possE == 0.0 and  possF == 0.0 and possI == 0.0: print("cannot identified") 
        else: 
            ans = max(possE,possF,possI)
            if ans == possE: print("***English")
            elif ans == possF: print("***French")
            elif ans == possI: print("***Italian")
        print(str(possE)+" "+str(possF)+" "+str(possI))
     """

# ---- PROVIDE TEST
           
    #print("---TEST TEST FILE---")
    sentences = list()
    line_n=0
    text = codecs.open("LangId.test",'r', encoding='cp1252')
    string = text.read().splitlines()
    output = open("wordLangId.out",'w')
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
    
