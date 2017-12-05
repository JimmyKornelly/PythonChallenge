import os
path = 'C:\\Users\\Konst\\Desktop'
os.chdir(path)
with open('text.txt','r',encoding='utf8') as file:
    text = file.readline().split()  
res = []
for word in text:
    if len(word) > 6:
        res.append(word.capitalize())
    else:
         res.append(word + ' ')
with open('text1.txt','w',encoding='utf8') as file_out:
    file_out.write(str(res))      
print (res)
input ()
