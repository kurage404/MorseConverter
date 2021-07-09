# code:Python3/UTF-8
# made by kurage404
import os

def lang_check(lang):
    sr = os.sep
    lang_list = os.listdir('..'+sr+'lang')
    if(lang in lang_list):
        return True
    else:
        return False


def get_transelate_list(lang):
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
