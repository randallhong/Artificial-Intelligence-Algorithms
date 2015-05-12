
import copy
from lea import *
class Variable:
  
    def __init__(self, name, parents, probabilities):
        self.name = name
        self.parents = parents
        self.probabilities = probabilities
        self.cpt=[]
        self.happen=[]
    def Init_cpt(self):
        if len(self.parents) == 0:
            f = [[], ["f"], [self.probabilities[0]]]
            t = [[], ["t"], [self.probabilities[1]]]
            self.cpt.append(f)
            self.cpt.append(t)
        else:
         
            parents = []
            cptt = [[],[],[]]
            cpt=[]

            #cpt1[["cloudy","rain"],["t","f"],[0.5]]
            for x in range(0, len(self.parents)):
                cptt[0].append(self.parents[x].name)
            #cptt[0].append(parents)
            for y in range(0, len(self.probabilities)):
                s='{0:0 b}'
                string=s.replace(' ',str(len(self.parents)))
                p = string.format(y)
                for i in range(0, len(p)):
                    if p[i] == '0':
                        happen = 'f'
                    else:
                        happen = 't'
                    cptt[1].append(happen)
                cptt[2].append(self.probabilities[y])
                cpt.append(copy.deepcopy(cptt))
                del cptt[1][:]
                del cptt[2][:]
            self.cpt = cpt
class BayesianNetwork:
    varialbes=[]
    def __init__(self):
        parents1=[]
        parents2=[]
        pro1=[0.5,0.5]
        v1=Variable("Cloudy","",pro1)
        v1.Init_cpt()
        pro2=[0.5,0.1]
        parents1.append(v1)
        v2=Variable("Sprinkler",parents1,pro2)
        v2.Init_cpt()
        pro3=[0.2,0.8]
        v3=Variable("Rain",parents1,pro3)
        v3.Init_cpt()
        # del parents[:]
        parents2.append(v2)
        parents2.append(v3)
        pro4=[0.01,0.9,0.9,0.99]
        v4=Variable("Wetgrass",parents2,pro4)

        v4.Init_cpt()
        self.varialbes.append(v1)
        self.varialbes.append(v2)
        self.varialbes.append(v3)
        self.varialbes.append(v4)
    def Get_Bayesian(self):
        return copy.deepcopy(self.varialbes)
def PriorSmaple(b):
    event=[]
    v=b.Get_Bayesian()
    for i in range(0,len(v)):
        #print(v[i].cpt)
        #print(len(v[i].parents))
        if len(v[i].parents)==0:

            dis=Lea.fromValFreqs(('f',v[i].cpt[0][2][0]*100),('t',v[i].cpt[1][2][0]*100))
            s=dis.random(1)
            # v[i].happen=s[0]
            v[i].happen.append(s[0])
            # print(v[i].happen)
        else:
            for x in range(0,len(v[i].cpt)):
                if len(v[i].parents)==1:
                    if v[i].parents[0].happen==v[i].cpt[x][1]:
                        diss=Lea.fromValFreqs(('f',100-v[i].cpt[x][2][0]*100),('t',v[i].cpt[x][2][0]*100))
                        ss=diss.random(1)
                        v[i].happen.append(ss[0])
                        break
                else:

                    #eg.v2.happen=t, v3.happen=f
                    if v[i].parents[0].happen[0]==v[i].cpt[x][1][0] and v[i].parents[1].happen[0]==v[i].cpt[x][1][1]:
                        disss=Lea.fromValFreqs(('f',100-v[i].cpt[x][2][0]*100),('t',v[i].cpt[x][2][0]*100))
                        sss=disss.random(1)
                        v[i].happen.append(sss[0])
                        break
    for e in range(0,4):
        event.append(v[e])
    return event
def Rejection(v,e,bn,N):
    T=0
    F=0
    Normalize=[[[],[],[]],[[],[],[]]]
    Accept=0
    for j in range(0,int(N)):
        event=PriorSmaple(bn)
        if len(e)==2:
            if event[e[0][0][0]].happen[0]==e[0][1][0] and event[e[1][0][0]].happen[0]==e[1][1][0]:
                Accept+=1
                if event[v[0]].happen[0]=='t':
                    T+=1
                else:
                    F+=1
        elif len(e)==1:
            if event[e[0][0][0]].happen[0]==e[0][1][0]:
                Accept+=1
                if event[v[0]].happen[0]=='t':
                    T+=1
                else:
                    F+=1
    if Accept!=0:
        Normalize[0][0].append(event[v[0]].name)
        Normalize[1][0].append(event[v[0]].name)
        Normalize[0][1].append("Flase")
        Normalize[1][1].append("True")
        Normalize[0][2].append(F/Accept)
        Normalize[1][2].append(T/Accept)
    else:
        print('\n')
        print("None of samples is accepted! Please try more samples!!!")
        print('\n')
    return Normalize
def ReadFile(filepath):
    file=open(filepath,'r')
    inference=[[],[],[]]
    lines=file.readlines()
    line=lines[0].strip('\n')
    l=line.split(',')
    inference[2].append(lines[1])
    for x in range(0,len(l)):
        if l[x]=='q':
            inference[0].append(x)
        else:
            if l[x]!='-':
                evidence=[[x],[l[x]]]
                inference[1].append(evidence)
    print(inference)
    return inference
if  __name__=="__main__":
    bn=BayesianNetwork()
    filepath='/Users/apple/Desktop/inference3.txt'
    inf=ReadFile(filepath)
    print(inf)
    sum=0
    for i in range(0,10):
        NOR=Rejection(inf[0],inf[1],bn,inf[2][0])
        print(NOR)
        sum+=NOR[1][2][0]
    print(sum/10)



