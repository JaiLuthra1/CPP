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
    if(str(line)[-1]!='\n'):
        name.append(str(line))
    else:
        name.append((str(line))[:-1])

d.close()

# Assign a negative rank for non-participant
ranks=[-5]*len(name)

for i in range(len(na)):
    for h in range(len(name)):
        if(na[i]==name[h]):ranks[h]=int(r[i])

final_rnk=[]

for i in range(len(name)):
    if(ranks[i]>0):
        final_rnk.append([ranks[i],name[i]])

final_rnk.sort()

final=open('final.csv',"w")

for i in range(len(final_rnk)):
    final.write(str(str(final_rnk[i][0])+","+str(final_rnk[i][1])+"\n"))

final.close()
for i in range(len(final_rnk)):
    print((len(str(final_rnk[-1][0]))-len(str(final_rnk[i][0])))*" " +str(final_rnk[i][0]) + ". " + str(final_rnk[i][1]))
