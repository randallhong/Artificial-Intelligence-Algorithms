from math import *
import matplotlib.pyplot as plt
import heapq
class TrainData(object):
 	def __init__(self,x,y,label):
			self.x=x
			self.y=y
			self.label=label
class Knn(object):
	def __init__(self,k):
		self.k=k
		self.traindata=[]
	def init_traindata(self,data):
		for num in range(len(data)):
			self.traindata.append(TrainData(data[num][0],data[num][1],data[num][2]))
	def getdistance(self,qury,traindata):
		return sqrt((float(qury[0])-float(traindata.x))*(float(qury[0])-float(traindata.x))+(float(qury[1])-float(traindata.y))*(float(qury[1])-float(traindata.y)))
	def getnearestlabel(self,qury,end):
		nears=[]
		lb0=0
		lb1=0
		for num in range(0,end):
			distance=self.getdistance(qury,self.traindata[num])
			heapq.heappush(nears,(distance,self.traindata[num]))

		# print nears
		for i in range(0,self.k):
			# print i
			di,data=heapq.heappop(nears)
			# print round(float(data.label))
			if round(float(data.label))==0.0:
				lb0+=1
			elif round(float(data.label))==1.0:
				lb1+=1
		#if the label of "0" you get is more than the label of "1"
		if lb0>lb1:
			return 0.0
		else:
			return 1.0
	# def Process(self):

#compute the ditance from every traninig data to the quiry point
#strore every distance in a min-heap
#if k=1, then extract 1 traning data from the heap
#and then use the lable that this trainning data has to label the quiry point
#if k=n, then recursively etract n trainning data from the heap
#and then count which label(0 or 1) has the most more one, pick that one to
#lable the qury
def Readfile(filepath):
	file=open(filepath,'r')
	quries=[]
	lines=file.readlines()
	for row in range(len(lines)):
		qury=lines[row].strip('\n')
		qury2=qury.split(' ')
		quries.append([qury2[0],qury2[1],qury2[2]])
	return quries
if __name__=="__main__":
	filepath='/Users/apple/Desktop/homework5.txt'
	quries=Readfile(filepath)
	t=0.0
	f=0.0
	rate=[]
	for i in range(1,11):
		k=i
		knn=Knn(k)
		knn.init_traindata(quries)
		start=(int)(len(quries)*0.8)
	# print start
		for num in range(start,len(quries)):
		#use quries[num] to compute its neartest element and get the label
			label=knn.getnearestlabel(quries[num],start)
			if label<>round(float(quries[num][2])):
				
				f+=1
			elif label==round(float(quries[num][2])):
				t+=1
		print "the number of error:"
		print f
		rate.append(f/(t+f))
		f=0.0
		t=0.0
	plt.show()
	plt.figure("KNN")
	plt.plot(range(1,1+len(rate)),rate)
	plt.xlabel("number of k")
	plt.ylabel("error rate")
	plt.title("error rate change with the number of k")
	plt.show()
	# print "The error rate is = %f" % (f/(t+f))


