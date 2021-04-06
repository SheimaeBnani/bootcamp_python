def text_analyzer(text):
        Other,Space,Lower,Upper=0,0,0,0
        Lines = text.readlines()
        for l in Lines:
                for i in l:
                        if i.isspace():
                                Space +=1
                        elif i.islower():
                                Lower += 1
                        elif i.isupper():
                                Upper += 1
                        else:
                                Other +=1
        return[Space,Lower,Upper,Other]

text=open("module00_ex02.py", "r")
print(text_analyzer(text))

