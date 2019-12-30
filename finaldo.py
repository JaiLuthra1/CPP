d = open("rank.csv", "r")

r = []
na = []

for line in d:
    r.append(line.split(",")[0])
    na.append(line.split(",")[1][:-1])

d.close()

d=open("names.csv","r")

name=[]
for line in d:
    if(str(line)[-1]!='\n'):name.append(str(line))
    else:name.append((str(line))[:-1])
d.close()

ranks=[-5]*len(name)
for i in range(len(na)):
    for h in range(len(name)):
        if(na[i]==name[h]):ranks[h]=int(r[i])

fank=[]
for i in range(len(name)):
    if(ranks[i]>0):fank.append([ranks[i],name[i]])

fank.sort()

files=open('final.csv',"w")

for i in range(len(fank)):
    files.write(str(str(fank[i][0])+","+str(fank[i][1])+"\n"))

files.close()
for i in range(len(fank)):
    print((len(str(fank[-1][0]))-len(str(fank[i][0])))*" " +str(fank[i][0]) + ". " + str(fank[i][1]))
