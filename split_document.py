def split_document():
    f = open('corpus.txt', 'r', encoding='utf-8')
    document_str = '' # string of one document
    document = [] # total document spilt by doc_ID

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