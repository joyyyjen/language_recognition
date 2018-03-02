#!/usr/local/bin/python3

if __name__ == "__main__":
    t = open("letterLangId.out",'r')
    s = open("LangId.sol",'r')
    t2 = open("wordLangId.out",'r')
    string = t.readlines()
    string2 = s.readlines()
    sum=0
    for i in range(300):
        if string[i] == string2[i]: sum = sum + 1
        else: print(string[i])    
    print(sum/300)
#    print(len(string))
#    print(string[1])
#    for i in range(len(string)):
#        if string[i] == "French\n": sum = sum +1
#    print(sum/len(string)) 
    t.close()
    s.close()
    #for line in string:
    
