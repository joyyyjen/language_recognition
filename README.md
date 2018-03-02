# language_recognition

Homework 2 for LING 406 Language Identification

This program reads the test file in the same directory and outputs the language of each sentences
It's a python program. (Idealy python3)

using library sys, codece, collection, pickle, and re
### 1. How to run?
If you are using Mac, open Terminal
If you are consider using letter bigram model, run ./letterLangId.py
If you are consider using word bigram model, run, ./wordLangId.py 
If you are consider using word bigram model (with better smoothing), run, ./wordLangId2.py 

### 2. Double check the python path in your environment
mine is in /usr/local/bin/python3
After executed, if you received this error: "No such file or directory"
try changing the first line #!/usr/local/bin/python3 to #!/usr/bin/python3

### 3. How does it work?
- The default training set include three languages: English, French, Italian. The training file is called "LangId.train.English", "LangId.train.French", and "LangId.train.Italian"
- The program will automatically trians first, and then automatically reads test file. The default test file is LangId.test
run ./letterLangId.py for letter bigram model and ./wordLangId.py for word bigram model
- letterLangId.out is the output file for letter bigram model. wordLangId.out is the output file for word bigram model. wordLangId2.out is the output file for word bigram model with better smoothing.

The output has the format of [line_id] [language]

NOTE:
It takes about 2~10 sec to execute each program
The analysis question and answers is in the Analysis_Answer.txt file.
