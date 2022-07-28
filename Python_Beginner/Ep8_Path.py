#open("name","mode","encoder")
#r = read
#w = write
#a = append

fr = open('Python_Basic\Python_Beginner\/file\demo.txt','r',encoding="UTF-8")
print(fr.read())

import os
script_dir = os.path.dirname(__file__) 
rel_path = "file\demo.txt"
abs_file_path = os.path.join(script_dir, rel_path)
fr2 = open(abs_file_path,'r',encoding="UTF-8")
print(fr2.read())