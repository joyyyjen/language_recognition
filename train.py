#!/usr/local/bin/python3
import sys
import codecs
from collections import Counter
import nltk

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
     
if __name__ =="__main__":

# ---- TRAIN FRENCH
    text = codecs.open("LangId.train.French",'r',encoding='cp1252')
    string = text.read()
    print("---TRAIN FRENCH---")
    mapF,freq_1F = trainProc(string)
    s = set(freq_1F.elements())
    print(len(s))
    trainFrench_l = open("trainfre_l",'wb')
    trainFrench_m = open("trainfre_m",'wb')
    pickle.dump(freq_1F,trainFrench_l)
    trainFrench_l.close()
    pickle.dump(mapF,trainFrench_m)
    trainFrench_m.close()
   
    #print("here:"); print(map["A"]["p"])
# ---- TRAIN ENGLISH
    text = codecs.open("LangId.train.English",'r', encoding='utf-8')
    string = text.read()
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
    string = text.read()
    print("---TRAIN ITALIAN---")
    mapI,freq_1I = trainProc(string)
    trainItalian_l = open("trainita_l",'wb')
    trainItalian_m = open("trainita_m",'wb')
    pickle.dump(freq_1I,trainItalian_l)
    trainItalian_l.close()
    pickle.dump(mapI,trainItalian_m)
    trainItalian_m.close()


