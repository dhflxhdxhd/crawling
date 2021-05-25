
file_name = "D:/2021/greentable/crawling_data.txt"
content = ""
target = "●"
new_word = "<span class='name'>"

with open(file_name,"r") as f:
    lines = f.readlines()
    for l in lines:
        if target in l:
            replaced = l.strip().replace(target,new_word) + "</span>"
            content += "\n" + replaced + "\n"
        else:
            original = l
            content += original


f = open(file_name, 'w')
f.write(content)



