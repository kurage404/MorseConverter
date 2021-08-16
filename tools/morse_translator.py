# code:Python3/UTF-8/LF
# made by kurage404
#これはモールス信号翻訳機です。
import os

def lang_check(lang):
    sr = os.sep
    lang_list = os.listdir('..'+sr+'lang')
    if(lang in lang_list):
        return True
    else:
        return False


def get_translate_list(lang):
    if(lang_check(lang)):
        sr = os.sep
        with open('..'+sr+'lang'+sr+lang, 'r',encoding="utf-8") as file:
            morse_tra = []
            for line in file:
                morse_tra += [line.split()]
            return morse_tra
    else:
        print("File Does Not Exist")
        return False

def message_check(m,tra_list):
    morse_tra,message_tra = 0,0
    for i in m:
        for li in tra_list:
            if(i in li):
                if(li.index(i) == 1):
                    morse_tra += 1
                else:
                    message_tra += 1
    if(morse_tra > message_tra):
        tra_int = 1
    else:
        tra_int = 0
    return tra_int

def translate_message(m,lang):
    tra_list = get_translate_list(lang)
    tra_int = message_check(m,tra_list)
    tra_mes = ""
    if (tra_int = 0):
        for i in m:
            for li in tra_list:
                if(i in li):
                    tra_mes = tra_mes + li[1] + " "
    else:
        for i in m:
            for li in tra_list:
                if(i in li):
                    tra_mes = tra_mes + li[0]
    print(tra_mes)
