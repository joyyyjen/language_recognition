#!/usr/local/bin/python3
#Author: Joy Jen, NetID: yjen2

import sys
import codecs
from collections import Counter
import nltk
import pickle
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

def bigram(s,freq):
    map = {}
    for i in range(len(s)):
        map[s[i]]= {}
        for j in range(len(s)):
            strr = s[i]+" "+s[j]
            if strr in freq:
                map[s[i]][s[j]] = freq[strr]
            else: map[s[i]][s[j]] = 1
#    print(map)
    return map 

def trainProc(string):
    list_1 = list()
    list_2 = list()
    for line in string:
        line = line.strip()
        line = "$"+line+"$"
        words = nltk.word_tokenize(line)
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
    # ---- CREATE BIGRAM ----
#    print(list_uni)
    freq_1 = frequency(list_uni)
    for x in s: freq_1[x] += 1
    freq_2 = frequency(list_bi)
    for x in s2: freq_2[x] += 1 
    #print(freq_2)
    #print(len(s))
    #print("---START BUILDING MAP---")
    #map = bigram(s,freq_2)
    return freq_2,freq_1

if __name__ =="__main__":
# ---- TRAIN FRENCH
    
    text = codecs.open("LangId.train.French",'r',encoding='cp1252')
    string = text.read().splitlines()
    print("---TRAIN FRENCH---")
    mapF,freq_1F = trainProc(string)
    trainFrench_l = open("trainfre_l",'wb')
    trainFrench_m = open("trainfre_m",'wb')
    pickle.dump(freq_1F,trainFrench_l)
    trainFrench_l.close()
    pickle.dump(mapF,trainFrench_m)
    trainFrench_m.close()
    
# ---- TRAIN ENGLISH
    text = codecs.open("LangId.train.English",'r', encoding='utf-8')
    string = text.read().splitlines()
    print("---TRAIN ENGLISH---")
    mapE,freq_1E = trainProc(string)
    trainEnglish_l = open("traineng_l2",'wb')
    trainEnglish_m = open("traineng_m2",'wb')    
    pickle.dump(freq_1E,trainEnglish_l)
    trainEnglish_l.close()
    pickle.dump(mapE,trainEnglish_m)
    trainEnglish_m.close()

# ---- TRAIN ITALIAN
   
    text = codecs.open("LangId.train.Italian",'r', encoding='cp1252')
    string = text.read().splitlines()
    print("---TRAIN ITALIAN---")
    mapI,freq_1I = trainProc(string)
    trainItalian_l = open("trainita_l",'wb')
    trainItalian_m = open("trainita_m",'wb')
    pickle.dump(freq_1I,trainItalian_l)
    trainItalian_l.close()
    pickle.dump(mapI,trainItalian_m)
    trainItalian_m.close()
