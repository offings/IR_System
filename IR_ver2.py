import re
import math

Josa = [] # Make Josa List
document = [] # total document spilt by doc_ID
dictionary = [] # [term, [docID, weight] [docID, weight], ... ]
q_list = []
q_tfidf = []

def make_Josa_list() :
    with open('Josa.txt', 'r', encoding='utf-8') as f :
        lines = f.readlines() # Read File
    for word in lines :
        Josa.append(word.rstrip('\n')) # Remove Carriage Return
    Josa.sort(key=len, reverse=True) # Sort with String Length

def clean_text(document) :
    special_character_list = '[.,《》()·<>\'\"~‘’“”「」]'
    repl = ' '
    text = re.sub(special_character_list, repl, document)
    return text

def Tokenizer(string) :
    string = string.strip()
    string = re.sub(' +', ' ', string) # remove multiple space
    str_split = string.split()
    return str_split

def sub_Josa(str_list) :
    sub_josa_list = [] # Return subtract Josa List
    for s in str_list :
        check = 0 # Check that remove Josa
        for j in Josa : # Include Josa
            if s[-len(j):] == j and len(s) != 1 : # detect Josa and str_list != one_character
                if len(s[0:-len(j)]) <= 0 :
                    check = 1
                    break

                if s[-len(j):] == "는" :
                    if s == "또는" :
                        sub_josa_list.append(s)
                        check = 1
                        break

                if s[-len(j):] == "로" :
                    if s == "프로" or s == '니콜로' or s == '쳄발로' :
                        sub_josa_list.append(s)
                        check = 1
                        break

                if s[-len(j):] == "이":
                    if s == "트로이" or s == '노르웨이' or s == '톨스토이' or s == '하노이' or s == '깊이':
                        sub_josa_list.append(s)
                        check = 1
                        break

                if(s[-len(j):] == '가'):
                    if s == '미술작가' or s == '작곡가' or s == '평가' or s == '연주가' or s == '작가' or s == '운동가' or s == '카뮈가' or s == '화가' or s == '정치가' or s == '웅변가' or s == '문학가' or s == '수필가' or s == '만화가' or s == '판화가':
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
        if check == 0 : # Not include Josa
            sub_josa_list.append(s) # Append Token without Josa
    return sub_josa_list

def split_document():
    f = open('corpus.txt', 'r', encoding='utf-8')
    document_str = '' # string of one document

    while True:
        line = f.readline()
        if not line : # end of file
            document.append(document_str)  # save to document list
            break
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

def indexing(string_list) :
    docID = int(string_list[1])
    word_index = string_list.index("/title") # word index behind title
    final_word = string_list[word_index + 1:len(string_list)] # word list behind title
    find_list = [] # list that compare string is exist or not exist
    for i in range(word_index + 1, len(string_list)) :
        if string_list[i] in final_word :
            find_list.clear()
            for j in range(len(dictionary)) :
                find_list.append(dictionary[j][0]) # make list that compare string is exist or not exist
            if string_list[i] not in find_list : # if string is not exist in find_list
                dictionary.append([string_list[i], [docID, final_word.count(string_list[i])]])
            elif string_list[i] in find_list :
                # docID가 기존것이랑 일치하면 아무것도 안 하고,
                index = find_list.index(string_list[i])
                if dictionary[index][1][0] == docID :
                    continue
                # docID가 기존것이랑 다르면 dictionary에 append를 해준다
                else :
                    dictionary[index].append([docID, final_word.count(string_list[i])])

def bigram(string_list) :
    docID = int(string_list[1])
    bigram_list = []
    biword = []
    word_index = string_list.index("/title")  # word index behind title
    final_word = string_list[word_index + 1:len(string_list)]  # word list behind title
    for i in range(word_index + 1, len(string_list) - 1) :
        biword.clear()
        biword.append(string_list[i])
        biword.append(string_list[i+1])
        bigram_list.append(" ".join(biword)) # Join two words that is continuous
    return docID, bigram_list

def bigram_indexing(docID, string_list) :
    find_list = []  # list that compare string is exist or not exist
    for i in range(0, len(string_list)):
        find_list.clear()
        for j in range(len(dictionary)):
            find_list.append(dictionary[j][0])  # make list that compare string is exist or not exist
        if string_list[i] not in find_list:  # if string is not exist in find_list
            dictionary.append([string_list[i], [docID, string_list.count(string_list[i])]])

def term_frequency():
    # tf : total term index
    # tf[i] : one term index
    # tf[i][0] : term
    # tf[i][1] : [docID, frequency]
    # tf[i][1][0] : docID
    # tf[i][1][1] : frequency
    # len(tf[i] - 1) :
    for i in range(len(dictionary)) :
        for j in range(len(dictionary[i]) - 2):
            dictionary[i][j+2][1] = 1 + math.log10(dictionary[i][j+2][1])

def document_frequency():
    for i in range(len(dictionary)) :
        df = len(dictionary[i]) - 1
        idf = len(document) / df
        log_idf = math.log10(idf)
        dictionary[i].insert(1, log_idf)

# 제곱해서 더하고, 루트(각 document 당 1번만 구하면 됨)
def square_document() :
    square = [0]*len(document)
    for word in range(len(dictionary)) :
        for i in range(1, len(document) + 1) : #docID비교
            for j in range(2, len(dictionary[word])) :
                if i == dictionary[word][j][0] :
                    square[i-1] = square[i-1] + math.pow(dictionary[word][j][1], 2)
    for i in range(len(document)) :
        square[i] = math.sqrt(square[i])
    return square

def length_normalization(square) :
    for word in range(len(dictionary)):
        for i in range(1, len(document) + 1):  # docID비교
            for j in range(2, len(dictionary[word])):
                if i == dictionary[word][j][0]:
                    dictionary[word][j][1] = dictionary[word][j][1] / square[i-1]

def query(string) :
    docID = len(document) + 1
    find_list = []
    biword = []
    josa = sub_Josa(Tokenizer(clean_text(string)))
    for word in josa :
        q_list.append(word)
    for i in range(len(q_list) - 1):
        biword.clear()
        biword.append(q_list[i])
        biword.append(q_list[i + 1])
        q_list.append(" ".join(biword))
    find_list = []  # list that compare string is exist or not exist
    for i in range(len(q_list)):
        find_list.clear()
        for j in range(len(dictionary)):
            find_list.append(dictionary[j][0])  # make list that compare string is exist or not exist
        if q_list[i] not in find_list:  # if string is not exist in find_list
            dictionary.append([q_list[i], [docID, q_list.count(q_list[i])]])
        elif q_list[i] in find_list:
            # docID가 기존것이랑 일치하면 아무것도 안 하고,
            index = find_list.index(q_list[i])
            if docID != dictionary[index][len(dictionary[index]) - 1][0] :
                dictionary[index].append([docID, q_list.count(q_list[i])])

def query_tfidf():
    query_index = 101
    # calculate query wt
    for i in range(len(dictionary)):
        for j in range(len(q_list)):
            if dictionary[i][0] == q_list[j]:
                for k in range(2, len(dictionary[i])):
                    if dictionary[i][k][0] == query_index:
                        dictionary[i][k][1] = dictionary[i][1] * dictionary[i][k][1]
                        q_tfidf.append([q_list[j], dictionary[i][k][1]])
    # calculate query length
    q_square = 0
    for i in range(len(q_tfidf)):
        q_square = q_square + math.pow(q_tfidf[i][1], 2)
    q_square = math.sqrt(q_square)

    # query length normalization
    for i in range(len(q_tfidf)):
        q_tfidf[i][1] = q_tfidf[i][1] / q_square

    # query list sorting
    q_tfidf.sort()

def calc_score() :
    score = [0]*100
    for i in range(len(dictionary)) :
        for j in range(len(q_tfidf)) :
            if q_tfidf[j][0] == dictionary[i][0] :
                for k in range(2, len(dictionary[i])-1):
                    score[dictionary[i][k][0] - 1] = score[dictionary[i][k][0] - 1] + (q_tfidf[j][1] * dictionary[i][k][1])
    return score

def IR_system() :
    for i in range(len(document)) :
        indexing(sub_Josa(Tokenizer(clean_text(document[i]))))
        docID, bigram_list = bigram(sub_Josa(Tokenizer(clean_text(document[i]))))
        bigram_indexing(docID, bigram_list)
    dictionary.sort()
    document_frequency()
    input_string = input("query : ")
    query(input_string)
    term_frequency()
    dictionary.sort()
    query_tfidf()
    square = square_document()
    length_normalization(square)

def ranking(score) :
    rank = []
    for i in range(len(document)) :
        rank.append([i+1, score[i]])
    rank.sort(key=lambda rank: rank[1], reverse=True)
    print("<Ranking>")
    for i in range(5) :
        print(i+1, ". document", rank[i][0] , ":", rank[i][1])

split_document()
make_Josa_list()
IR_system()
ranking(calc_score())