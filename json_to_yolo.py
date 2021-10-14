# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:31:28 2021

@author: LG
"""
# json load
import json
def load_json(fname):
    with open(fname, encoding = "utf 8") as f:
        json_obj =  json.load(f)
        
    return json_obj

# In[-] 폴더 내 파일읽기
import os
'''
반드시 첫번째로 여기있는 다이렉토리를 수정하면 될듯.
'''
directory = 'C:/Users/LG/Desktop/conference/test_for_json_to_yolo'
filelist = os.listdir(directory)


# In[-]

for i in filelist:
    a = load_json(i)
    value_of_label = list(a[0].values()) # key,value from json
    split_point = value_of_label[10].split(',') # handle point x,y
    list_of_essential = [value_of_label[11],split_point[0],split_point[1],value_of_label[2],value_of_label[3]]
    list_of_essential_final = ' '.join(list_of_essential)  
    save_to_txt = open('%s.txt' % i[:-5],'w')#뒤에서부터 json짜르고 똑같은이름으로 txt파일 저장
    save_to_txt.write(list_of_essential_final)
    save_to_txt.close()

# In[main]

#read label_yolo from txt
''' # 욜로 스타일 라벨링 데이터 읽어와봤음.
with open('A220148XX_04563.txt','r') as file:
    label_yolo = file.readline()
'''


''''여기서부턴 그냥 reference'''
# In[-] arrange to essentiatl information


label_yolo = load_json('A220148XX_04547.json')
value_of_label = list(label_yolo[0].values()) # key,value from json
split_point = value_of_label[10].split(',') # handle point x,y
#transpert to list
list_of_essential = [value_of_label[11],split_point[0],split_point[1],value_of_label[2],value_of_label[3]]



# In[-] write txt, list to str, save.


list_of_essential_final = ' '.join(list_of_essential)
save_to_txt = open('example.txt','w')#can put other folder. note way in front of txt
save_to_txt.write(list_of_essential_final)
save_to_txt.close()
