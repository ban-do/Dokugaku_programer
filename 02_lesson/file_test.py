with open ("./st.txt","r",encoding = "utf-8")as f:
    print(f.read())

type = input("what do you like food?")
with open("./answer.txt","w",encoding = "utf-8")as f:
    f.write(type)

import csv

list = [["TopGun","RiskyBusiness","MinorityReport"],["Titanic","TheRevenant","Inception"],["TrainingDay","ManonFire","Flight"]]
with open ("./movie.csv","w",encoding = "utf-8")as f:
    w = csv.writer(f,delimiter = ",")
    for r in list:
        w.writerow(r)
