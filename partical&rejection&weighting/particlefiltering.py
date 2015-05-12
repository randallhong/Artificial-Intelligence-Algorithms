import copy
import lea
from random import *
class DynamicBaysianNetwork:
    
    def __init__(self,prior,transition,sensor):
        self.prior=[]
        self.prior.append(prior)
        self.trasition=transition
        self.sensor=sensor
        self.dbn=[]
    #dbn=[[0,7],[['t','f'],[0.7,0.3]],[['t','f'],[0.9,0.2]]
    def construct_dbn(self):
    
        self.dbn.append(self.prior)
        self.dbn.append(copy.deepcopy(self.trasition))
        self.dbn.append(copy.deepcopy(self.sensor))
        return copy.deepcopy(self.dbn)
def Sample(pro):
    dis=lea.Lea.fromValFreqs(('f',100-pro*100),('t',100*pro))
    return dis
def Weight_sapmle(s,dbn,e):
    
    weight=1
    sample_with_weight=[]
    for x in range(0,len(dbn[2][0])):
        if dbn[2][0][x]==s[0]:
            if e[0]=='t':
                weight*=dbn[2][1][x]
            else:
                weight*=(1-dbn[2][1][x])
            break
    sample_with_weight.append(s[0])
    sample_with_weight.append(weight)
    #saple['t',0.5]
    return sample_with_weight
def ParticleFiltering(e,N,dbn):
    #in there, just generate lots of sample depending on the prior probobility
    samples=[]
    sample_new=[]
    resample=[]
    T=0
    F=0
    dis=Sample(dbn[0][len(dbn[0])-1])
    s=dis.random(int(N))
    for h in range(0,len(s)):
        samples.append(s[h])
    #use the transition model to generate the new samples
    for x in range(0,int(N)):
        
        for i in range(0,len(dbn[1][0])):
            if dbn[1][0][i]==samples[x]:
                # print(dbn[1][1][i])
                d=Sample(dbn[1][1][i])
                ss=d.random(1) 
                sample_new.append(Weight_sapmle(ss[0],dbn,e))
                break
    for y in range(0,len(sample_new)):
        i=randint(0,len(sample_new)-1)
        randompro=randint(0,1000)/1000
        if randompro<sample_new[i][1]:
            resample.append(sample_new[i][0])
    #normalize the new samples' probability
    for x in range(0,len(resample)):
        if resample[x]=='t':
            T+=1
        else:
            F+=1
    dbn[0].append(T/(T+F))
    return T/(T+F)
def ReadFile(filepath):
    #t,t,t,t,t
    #100
    evidence=[[],[]]
    file=open(filepath,'r')
    lines=file.readlines()
    line=lines[0].strip('\n')
    l=line.split(',')
    for x in range(0,len(l)):
            evidence[0].append(l[x])
    evidence[1].append(lines[1])
    return evidence
if  __name__=="__main__":
    filepath='/Users/apple/Desktop/umbrellas3.txt'
    evidence=ReadFile(filepath)
    print('The data read from file is ',evidence)
    transition=[['t','f'],[0.7,0.3]]
    sensor=[['t','f'],[0.9,0.2]]
    d=DynamicBaysianNetwork(0.7,transition,sensor)
    dbn=d.construct_dbn()
    print('The DynamicBaysianNetwork is',dbn)
    # print(evidence)
    sum=0
    for time in range(0,30):
        for y in range(0,len(evidence[0])):
            p=ParticleFiltering(evidence[0][y],evidence[1][0],dbn)
        print('The',time+1,'times','Probability is ',p)
        sum+=p
    av=sum/30
    print("The average is")
    print(av)