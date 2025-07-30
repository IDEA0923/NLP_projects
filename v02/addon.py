

def get_sentence_by_file(file_name : str )->list:
    f = open(file_name , "r")
    s =  f.readlines()
    sint = list()
    buff = ""
    buff_list = list()
    for i in s: #каждая строка 
        for symb in i : # читаем символ каждой строки 
            if symb == '\n':
                continue
            if (symb != ' ' ):
                buff =  buff + symb
            else:
                buff_list.append(buff)
                buff = ""
        buff_list.append(buff)
        buff = ""
        sint.append(buff_list)
        buff_list = list()
    return sint

def make_word_list(sentences : list )->list:
    word_list = list()
    for i in sentences:
        for word in i:
            if word not in word_list :
                word_list.append(word)
    return word_list


