#!/usr/bin/env python3

'''
extractPDF.py: 处理PDF文件中的换行符问题，并自动消除引用数字
需要同文件夹内words_for_transformation.txt作为输入源

__author__ = "Whale Song"
__email__  = "whalesong@pku.edu.cn"
__version__ = '1.0'
'''


btype = list('1234567890') + [',', '–']

with open('words_for_transformation.txt', 'r') as file:
    word_list = file.readlines()
    
def removen(wlst):
    if type(wlst) != list:
        raise Exception('object not a list', type(wlst))
    else:
        for i in range(len(wlst)):
            wlst[i] = wlst[i].replace('\n', '')
        return ' '.join(wlst)

def removeRef(lstr, p=False, i=0, s=0):
    if i == 12 and p == False:
        return removeRef(lstr, True)
    elif i < 12:
        posi = lstr.find(btype[i], s)
        if posi == -1 and i <= 9:
            return removeRef(lstr, p,  i+1)
        elif posi != -1 and i <= 9:
            if 64 < ord(lstr[posi-1]) < 123:
                return removeRef(lstr[:posi]+lstr[posi+1:], p, i)
            else:
                return removeRef(lstr, p, i, posi+1)
        elif 9 < i <= 11:
            if posi != -1:
                if 47 < ord(lstr[posi+1]) < 59:
                    return removeRef(lstr[:posi]+lstr[posi+2:], p, i)
                else:
                    return removeRef(lstr, p, i, posi+1)
            else:
                return removeRef(lstr, p, i+1)
    elif i == 12 and p == True:
        return lstr

def write(object):
    with open('result.txt', 'w') as file:
        file.write(object)

def main():
    words = removen(word_list)
    words = removeRef(words)
    write(words)

if __name__ == '__main__':
    main()