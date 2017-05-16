file = open("data.txt", "r")
file_data = file.readlines()
file.close()
data = file_data[0]
q="dinchak"
flag = 0
for i in data:
    if i[0] == q:
        print i[1]
        flag = 1
if(flag == 0):
    file1 = open("data.txt", "w+")
    file1.write(','.join((q,"???")))
print data
