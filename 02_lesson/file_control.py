import os

#path = os.path.join("Users","bob","st.txt")
#print(path)

st = open("./st.txt","w",encoding = "utf-8")
st.write("書き込んだよー")
st.close()

with open("./st.txt","r",encoding = "utf-8")as f:
    print(f.read())

my_list = []
with open("./st.txt","r",encoding = "utf-8")as s:
    my_list.append(s.read())

print(my_list)

import csv

with open("./test.csv","w",newline='') as f:
    w = csv.writer(f,delimiter = ",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])
    w.writerow(["seven","eight","nine"])

with open("./test.csv","r",) as f:
    r = csv.reader(f,delimiter = ",")
    for row in r:
        print(",".join(row))
