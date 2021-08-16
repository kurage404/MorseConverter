# code:Python3/UTF-8
# made by kurage404
#これはモールス信号置換機です。

def defult_str():
    return("・","ー","0","1")

def convert(from1, from2, to1, to2, m):
    m = m.replace(from1, to1)
    m = m.replace(from2, to2)
    print(m)

def state():
    print("\'"+from1+"\' => \'"+to1+"\'")
    print("\'"+from2+"\' => \'"+to2+"\'")
from1, from2, to1, to2 = defult_str()
state()
m=input()
convert(from1, from2, to1, to2, m)
