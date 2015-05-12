#describe has the weight of each edge[[[0,0,weight,value,diffrence],[0,1,weight],[1,0,weight]],[[[],[]]]
alpha=0.1
from random import *
import matplotlib.pyplot as plt
from math import *
class ANN(object):
	"""docstring for ANN"""
	def __init__(self,layer,number_input_nodes,number_hidden_nodes,number_output_nodes):
		self.layer=layer
		self.inputlayer_nodes=number_input_nodes
		self.hiddenlayer_nodes=number_hidden_nodes
		self.outputlayer_nodes=number_output_nodes
		self.edge=[]
		# self.inj=0
	def init_edge(self):
		#only three layers for this specific problem
		#the first one which contains the edge from input layer to the hidden layer
		#the second one which contains the edge from hidden layer to the output layer
		edge=[[],[]]
		for e in range(0,self.layer-1):
			if e==0:
				for i in range(0,self.inputlayer_nodes):
					for j in range(0,self.hiddenlayer_nodes):
						edge[e].append([i,j,-1])
			elif e==1:
				for i in range(0,self.hiddenlayer_nodes):
					for j in range(0,self.outputlayer_nodes):
						edge[e].append([i,j,-1])
		self.edge=edge
	def update_weight(self,weight,layer,start,end):
			for i in range(len(self.edge[layer])):
				if self.edge[layer][i][0]==start and self.edge[layer][i][1]==end:
					#replace the oringin weight!
					self.edge[layer][i][2]=weight
		#compute the answer for output layer
	def g_function(self,num):
		return (1/(1+exp(-num)))
	def gprime(self,num):
		return (1 / (2 + (e**(-(num))) + (e**((num)))))
	def get_output(self):
		#compute each hiddennode's value
		inj=0
		for nodes1 in range(len(self.edge[1])):
			summ=0
			for nodes0 in range(len(self.edge[0])):
				if self.edge[0][nodes0][1]==self.edge[1][nodes1][0]:
					summ+=self.edge[0][nodes0][3]*self.edge[0][nodes0][2]
			self.edge[1][nodes1].append(self.g_function(summ))
			#compute the final ouput's value
		for node in range(len(self.edge[1])):
			inj+=self.edge[1][node][3]*self.edge[1][node][2]
		return self.g_function(inj)
	def test(self,qury):
		for j in range(len(self.edge[0])):
			if self.edge[0][j][0]==0:
				self.edge[0][j].append(float(qury[0]))
			elif self.edge[0][j][0]==1:
				self.edge[0][j].append(float(qury[1]))
		inj=0
		for nodes1 in range(len(self.edge[1])):
			summ=0
			for nodes0 in range(len(self.edge[0])):
				if self.edge[0][nodes0][1]==self.edge[1][nodes1][0]:
					summ+=self.edge[0][nodes0][3]*self.edge[0][nodes0][2]
			self.edge[1][nodes1].append(self.g_function(summ))
		for node in range(len(self.edge[1])):
			inj+=self.edge[1][node][3]*self.edge[1][node][2]

		return self.g_function(inj)
def Back_Prop_Learning(examples,network,end):
	start=True
	while start:
		#randomly generate weights
		for layer in range(0,network.layer-1):
			if layer==0:
				for i in range(0,network.inputlayer_nodes):
					for j in range(0,network.hiddenlayer_nodes):
						weight=random()
						network.update_weight(weight,layer,i,j)
			elif layer==1:
				for i in range(0,network.hiddenlayer_nodes):
					for j in range(0,network.outputlayer_nodes):
						# while weight>0.1:
						weight=random()
						network.update_weight(weight,layer,i,j)
						# weight=0.2
		#begin with the first train data
		for ex in range(0,end):
			#get the input
			inj=0
			for j in range(len(network.edge[0])):
				if network.edge[0][j][0]==0:
					network.edge[0][j].append(float(examples[ex][0]))
				elif network.edge[0][j][0]==1:
					network.edge[0][j].append(float(examples[ex][1]))
			#get the out put
			output=network.get_output()
			#compute the difference 3 is value, 2 is weight
			for node in range(len(network.edge[1])):
				inj+=network.edge[1][node][3]*network.edge[1][node][2]
			d=(float(examples[ex][2])-output)*network.gprime(inj)
			for nodes1 in range(len(network.edge[1])):
				summ=0
				for nodes0 in range(len(network.edge[0])):
					if network.edge[0][nodes0][1]==network.edge[1][nodes1][0]:
						summ+=network.edge[0][nodes0][3]*network.edge[0][nodes0][2]
				dd=network.gprime(summ)*d*network.edge[1][nodes1][2]
				network.edge[1][nodes1].append(dd)
			#update all the weight in edge
			for e in range(len(network.edge)):
				if e==0:
					for w in range(len(network.edge[0])):
						for ww in range(len(network.edge[1])):
							if network.edge[0][w][1]==network.edge[1][ww][0]:
								network.edge[0][w][2]+=alpha*network.edge[0][w][3]*network.edge[1][ww][4]				
				elif e==1:
					for z in range(len(network.edge[1])):
						network.edge[1][z][2]+=network.edge[1][z][3]*d
			#delete the previous input
			for c in range(len(network.edge[0])):
				del network.edge[0][c][3]
			for q in range(len(network.edge[1])):
				del network.edge[1][q][3]
				del network.edge[1][q][3]
		if abs(d)<0.13:
			start=False

def Readfile(filepath):
	file=open(filepath,'r')
	quries=[]
	lines=file.readlines()
	for row in range(len(lines)):
		qury=lines[row].strip('\n')
		qury2=qury.split(' ')
		quries.append([qury2[0],qury2[1],qury2[2]])
	return quries
def judge(number):
	if number < 0.5:
		return 0.0 
	else:
		return 1.0
	pass
if __name__=="__main__":
	filepath='/Users/apple/Desktop/homework5.txt'
	quries=Readfile(filepath)
	correct=0.0
	rate=[]
	for i in range(2,11):
		a=ANN(3,2,i,1)
		a.init_edge()
		#train data
		Back_Prop_Learning(quries,a,160)
		#test data
		for i in range(160,len(quries)):
			if float(quries[i][2])==judge(a.test(quries[i])):
				correct+=1
			for e in range(len(a.edge[0])):
				del a.edge[0][e][3]
			for ee in range(len(a.edge[1])):
				del a.edge[1][ee][3]
		print "the number of error:"
		print (40-correct)
		rate.append((40-correct)/(len(quries)-160))
		correct=0.0
	plt.show()
	plt.figure("ANN")
	plt.plot(range(2,2 + len(rate)),rate)
	plt.xlabel("number of hidden neurons")
	plt.ylabel("error rate")
	plt.title("error rate with the number of hidden neurons")
	plt.show()

	# print a.edge