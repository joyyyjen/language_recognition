#!/usr/local/bin/python3

if __name__ == "__main__":
    t = open("letterLangId.out",'r')
    s = open("LangId.sol",'r')
    t2 = open("wordLangId.out",'r')
    string = t2.readlines()
    string2 = s.readlines()
    sum=0
    for i in range(300):
        if string[i] == string2[i]: sum = sum + 1
        else: print(string[i])    
    print(sum/300)
    t.close()
    s.close()
    #for line in string:
    
