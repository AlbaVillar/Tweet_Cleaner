#!/usr/bin/env python3

with open("Input.txt", 'r', encoding='utf8') as infile:
    content = infile.readlines()

line_clean=[]
line_list=[]
line_split=[]
split_data=('","')
for line in content:
    line = line.strip()
    if any([word in line for word in split_data]):
        line_split = line.split('",')

        if len(line_split)==3:
            line_clean.append(line_split[2])
#Splits metadata and saves tweet text in line_clean 

for line in line_clean:
    line=line[1:-1]
    #removes "" from the beginning and end of sentence
    num = len(line)
    #measures the length of the sentence

    if num >= 50:
        line_list.append(line)
        #saves the sentences that are equal or bigger than 50 characters in line_list

lines_final=[]
forbiden_characters=("@","#","https","…","lmao", "LMAO", "Lmao", "Wtf", "wtf", "WTF","lol","LOL","Lol","bitch","BITCH","Bitch", "Nigga","NIGGA","nigga")
for item in line_list:
    if not any([word in item for word in forbiden_characters]):
        lines_final.append(item)
#Removes sentences that contain URL, hashtags, @profile names, offensive words and abbreviations

with open("Output.txt",'w', encoding='utf8') as outfile:
    for outline in lines_final:
        outstr="{}\n".format(outline)
        outfile.write(outstr)


