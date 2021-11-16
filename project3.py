import re
file = input("please input file as .txt: ")
import os.path 
if os.path.exists(file):
    with open(file) as file_doc:
        file_content = file_doc.read()
else:
     file = input("please name file that exists: ")


file_content1 = re.sub(r"(ll)", "l", file_content, flags=re.M)
file_content2 = re.sub(r"(ed)", "t", file_content1, flags=re.M)
file_content3 = re.sub(r"(ize)", "ise", file_content2, flags=re.M)

with open("output.txt", "a+") as f:
    for item in file_content3:
        f.write(item)


