import re

Josa = [] # 조사 리스트 제작

def make_Josa_list() : 
    with open('Josa.txt', 'r', encoding='utf-8') as f :
        lines = f.readlines()
    for word in lines :
        Josa.append(word.rstrip('\n'))

def clean_text():
    text = '<title>1. 지미 카터</title> 지미 카터는 민주당 출신 미국 39번째 대통령이다. 지미 카터는 조지아 주  한 마을에서 태어났다. 조지아 공과대학교를 졸업하였다. 그 후 해군에 들어가 전함·원자력·잠수함의 승무원으로 일하였다. '
    special_character_list = '[.,《》()·<>\'\"]'
    repl = ' '
    text = re.sub(special_character_list, repl, text)
    print(text)

clean_text()
