with open("demo.txt",'r+') as file:
    file.truncate(0)
with open("demo1.txt",'r+') as file:
    file.truncate(0)


f = open("pred.csv", "w")
f.truncate()
f.close()

f = open("grp_by1.csv", "w")
f.truncate()
f.close()

f = open("results.csv", "w")
f.truncate()
f.close()