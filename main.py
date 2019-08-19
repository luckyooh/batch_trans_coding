# -*- coding: utf-8 -*-
import  os
import chardet

path = "/Users/jiangfubang/Documents/project/ai/"

files = os.listdir(path)

for file in files:
    with open(path+file, "rb") as f:
        data = f.read()
        ch = chardet.detect(data)["encoding"]
    print(ch,file)
    with open(path+file, "r", encoding=ch) as f:
        text = f.read()
    print(text)