# Competitive Programming Parser

from bs4 import BeautifulSoup
import urllib.request,time,os
import re,sys

olusern="-11111111111111111111111111"
pagescount=1

f = open("rank.csv", "w")
f.truncate()
f.close()
# contest_id=int(input("Contest Id : \n"))
contest_id = sys.argv[1]
start_time = time.time()

while(pagescount>=0):
    url = "https://codeforces.com/contest/+"+str(contest_id)+"/standings/page/"+str(pagescount)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    regex1 = re.compile('contestant-cell')
    content_lis = soup.find_all('td', attrs={'class': regex1})

    ranks = soup.find_all('tr')
    # rnk_lis = soup.find_all('tr', attrs={'participantId': regex2})

    sd=[]
    for datal in content_lis:
        cur=""
        for chr in datal:
            cur+=str(chr)+" "
        sd.append(cur)

    se=[]
    for ch in sd:
        s=""
        for j in range(len(ch)):
            if(ch[j:j+4]=="href"):
                while(ch[j+16]!=' '):
                    s+=(ch[j+15])
                    j+=1
        se.append(s)

    # rank=1
    # for j in se:
    #     print(str(rank)+". "+j)
    #     rank+=1

    for j in se:
        checkusern = j
        break
    
    if(checkusern == olusern):
        pagescount=-502
        break

    olusern = checkusern

    sy=""
    for i in ranks:
        sy+=str(i)+" "

    rnk_list = []
    for i in range(len(sy)):
        if(sy[i:i+14]=="participantid="):
            while(sy[i-3:i-1]!="td"):
                i+=1
            j=i
            while(sy[i+3:i+5]!="td"):
                i+=1
            rnk_list.append(sy[j:i-1])

    for j in range(len(rnk_list)):
        ab = ""
        deh=0
        for a in str(rnk_list[j]):
            if(a!='\r'):
                if('0' <= a and a <= '9' ):
                    ab+=a
                    deh=1
                elif(deh==1):
                    break
        rnk_list[j]=int(ab)

    # print(rnk_list)

    fi=open('rank.csv',"a")
    i=0
    for j in se:
        fi.write(str(rnk_list[i])+","+j+"\n")
        i+=1

    fi.close()

    pagescount+=1  

t2=time.time();print("Time Elapsed -> "+str(int(t2-start_time))+"sec")

os.system("python3 find_ranks.py")