import re

Josa = [] # Make Josa List
document = [] # total document spilt by doc_ID

def make_Josa_list() : 
    with open('Josa.txt', 'r', encoding='utf-8') as f :
        lines = f.readlines() # Read File
    for word in lines :
        Josa.append(word.rstrip('\n')) # Remove Carriage Return
    Josa.sort(key=len, reverse=True) # Sort with String Length

def clean_text() :
    special_character_list = '[.,《》()·<>\'\"]'
    repl = ' '
    text = re.sub(special_character_list, repl, document[73])
    return text

def Tokenizer(string) :
    string = string.strip()
    string = re.sub(' +', ' ', string) # Remove multiple space
    str_split = string.split()
    return str_split

def sub_Josa(str_list) :
    sub_josa_list = [] # Return subtract Josa List
    for s in str_list :
        check = 0 # Check that remove Josa
        for j in Josa :
            if s[-len(j):] == j and len(s) != 1 : # If Josa is in Token
                if s[-len(j):] == "로" :
                    if s == "프로" :
                        sub_josa_list.append(s)
                        check = 1
                        break
                if s[-len(j):] == "도" :
                    if len(s[0:-len(j)]) <= 1 :
                        sub_josa_list.append(s)
                        check = 1
                        break
                    else :
                        sub_josa_list.append(s[0:-len(j)])  # Append subtract token in final list
                        check = 1
                        break
                sub_josa_list.append(s[0:-len(j)]) # Append subtract token in final list
                check = 1
                break
        if check == 0 :
            sub_josa_list.append(s) # Append Token without Josa
    return sub_josa_list

def split_document():
    f = open('corpus.txt', 'r', encoding='utf-8')
    document_str = '' # string of one document

    while True:
        line = f.readline()
        if not line : break # end of file

        if '<title>' in line: # new document
            if document_str == '': # first document
                document_str = document_str + line
                continue
            else: # other document
                document.append(document_str) # save to document list

            document_str = '' # new string
            document_str = document_str + line

        else:
            document_str = document_str + line
    f.close

split_document()
make_Josa_list()
print(sub_Josa(Tokenizer(clean_text())))