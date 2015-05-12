import math
import copy
import random
import sys 
import time
sys.setrecursionlimit(2000000000)
class assignment:
	sudo=[]
	domain=[]
	constraints=[]
	question_index=[]
	def __init__(self,sudo):
		self.sudo=sudo
	def Init_Constraints(self):
		for x in range(0,len(sudo)):
			for y in range(0,len(sudo)):
				self.Get_Row_Constraints(x,y)
				self.Get_Col_Constraints(x,y)
				self.Get_Block_Constraints(x,y)
	def Get_Row_Constraints(self,row,col):
		for j in range(0,len(self.sudo)):
			if col<>j:
				self.constraints.append([[row,col],[row,j]])
	def Get_Col_Constraints(self,row,col):
		for i in range(0,len(self.sudo)):
			if row<>i:
				self.constraints.append([[row,col],[i,col]])
	def Get_Block_Constraints(self,row,col):
		times=0
		block_num=-1
		find_block=False
		blocks=int(math.sqrt(len(self.sudo)))
		for i in range(len(self.sudo)):
 			if i==0:
 				mark=i
 			if times==len(self.sudo)/blocks:
 				mark=i
 				times=0
 			for x in range(mark,mark+blocks):
 				for y in range(times*blocks,times*blocks+blocks):
 					if row==x and col==y:
 						block_num=i
 						find_block=True
 						break
			times+=1
			if find_block:
				break
		for m in range(int(block_num/blocks)*blocks,int(block_num/blocks)*blocks+blocks):
 				for n in range((block_num%blocks)*blocks,(block_num%blocks)*blocks+blocks):
 					if row<>m and col<>n:
 						self.constraints.append([[row,col],[m,n]])

	def Init_Domain(self):
		var=[]
		for x in range(0,len(self.sudo)):
			for y in range(0,len(self.sudo)):
				var.append([x,y])
		value=[[i for i in range(1,len(self.sudo)+1)] for j in range(len(self.sudo)*len(self.sudo))]
		self.domain=zip(var,value)
		# print domain
		for row in range(0,len(self.sudo)):
			for col in range(0,len(self.sudo)):
				if cmp(sudo[row][col],'?')==-1:
					for x in range(0,len(self.domain)):
						if [row,col] in self.domain[x]:
							del self.domain[x][1][:]
							self.domain[x][1].append(sudo[row][col])
	#you wenti!!!
	def EditDomain(self,row,col,value):
		for x in range(1,len(self.domain)):
			if [row,col] in self.domain[x]:
				del self.domain[x][1][:]
				self.domain[x][1].append(value)
				break
	def Add_value(self,row,col,value):
		self.sudo[row][col]=value
		if value<>'?':
			self.EditDomain(row,col,value)
	def Consistent(self,row,col,Value):
		if self.JudgeRowConlficts(row,Value) and self.JudgeColConflicts(col,Value) and self.JudgeBlockConflicts(row,col,Value):
			return True
		else:
			return False 
	def Print_sudo(self):
		for x in xrange(0,len(sudo)):
			print sudo[x]
			pass
		
	def JudgeColConflicts(self,col,value):
		for row in range(0,len(self.sudo)):
			if self.sudo[row][col]==value:
				return False
		return True
	def JudgeRowConlficts(self,row,value):
		for col in range(0,len(self.sudo)):
			if self.sudo[row][col]==value:
				return False
		return True
	def JudgeBlockConflicts(self,row,col,value):
		times=0
		block_num=-1
		find_block=False
		blocks=int(math.sqrt(len(self.sudo)))
		for i in range(len(self.sudo)):
 			if i==0:
 				mark=i
 			if times==len(self.sudo)/blocks:
 				mark=i
 				times=0
 			for x in range(mark,mark+blocks):
 				for y in range(times*blocks,times*blocks+blocks):
 					if row==x and col==y:
 						block_num=i
 						find_block=True
 						break
			times+=1
			if find_block:
				break
		for m in range(int(block_num/blocks)*blocks,int(block_num/blocks)*blocks+blocks):
 				for n in range((block_num%blocks)*blocks,(block_num%blocks)*blocks+blocks):
 					if self.sudo[m][n]==value:
 						return False
 		return True
	def Scan_Domain(self,row,col,dd):
		for x in range(0,len(dd)):
			if [row,col] in dd[x]:
				return copy.deepcopy((dd[x][1]))
	def Inferences(self,do):
		for x in range(0,len(do)):
			if len(do[x][1])==0:
				return False
		return True
# General Arc consistency
	def New_Constraints(self,Var,domai,constraints):
		domain_x=[]
		NTDA=[]
		for v in Var:
			index_of_x=[v[0],v[1]]
			doma=copy.deepcopy(self.Scan_Domain(index_of_x[0],index_of_x[1],domai))
			domain_x.append((index_of_x,doma))
		TDA=constraints
		while(len(TDA)==0):
			x=random.randint(0,len(TDA)-1)
			NTDA.append(TDA[x])
			x_row_index=TDA[x][0][0]
			x_col_index=TDA[x][0][1]
			y_row_index=TDA[x][1][0]
			y_col_index=TDA[x][1][1]
			del TDA[x]
			original_domain_of_x=copy.deepcopy(self.Scan_Domain(x_row_index,x_col_index,domain_x))
			domain_first=copy.deepcopy(self.Scan_Domain(x_row_index,x_col_index,domain_x))
			domain_second=copy.deepcopy(self.Scan_Domain(y_row_index,y_col_index,domain_x))		
			if not domain_second:
				continue
			remain=len(domain_first)
			for i in range(0,len(domain_first)):
				if i==remain:
					break		
				satisfy=False
				for j in range(0,len(domain_second)):
					if domain_first[i]<>domain_second[j]:
						satisfy=True
						break
				if not satisfy:
					remain=remain-1
					del domain_first[i]
			if set(domain_first)<>set(original_domain_of_x):
				for s in range(0,len(domain_x)):
					if [x_row_index,x_col_index] in domain_x[s]:
						del domain_x[s][1][:]
						for m in range(0,len(domain_first)):
							domain_x[s][1].append(domain_first[m])
				re=len(NTDA)
				for x in range(0,len(NTDA)):
					if x==re:
						break
					if [x_row_index,x_col_index] in NTDA[x][1]:
						TDA.append(NTDA[x])
						del NTDA[x]
						re=re-1
			if not TDA:
				print 'TDA EMPTY'
		return domain_x
	def Find_TDA_Constraints_of_x(self,constraints,row,col):
		xtda_constraints=[]
		for x in range(0,len(constraints)):
			if [row,col] == constraints[x][1]:
				xtda_constraints.append(constraints[x])
		return copy.deepcopy(xtda_constraints)

	def Find_NTDA_Constraints_of_x(self,constraints,row,col):
		xntda_constraints=copy.deepcopy(constraints)
		remain=len(xntda_constraints)
		for x in range(0,len(xntda_constraints)):
			if x==remain:
				break
			if [row,col]==xntda_constraints[x][1]:
				del xntda_constraints[x]
				remain=remain-1
		return copy.deepcopy(xntda_constraints)

	def Get_var(self,row,col):
		related_neighbor_x=[]
		for c in range(0,len(self.sudo)):
			if [row,c] not in related_neighbor_x :
				related_neighbor_x.append([row,c])
		for b in range(0,len(self.sudo)):
			if [b,col] not in related_neighbor_x:
				related_neighbor_x.append([b,col])
		times=0
		block_num=-1
		blocks=int(math.sqrt(len(self.sudo)))
		for i in range(len(self.sudo)):
 			if i==0:
 				mark=i
 			if times==len(self.sudo)/blocks:
 				mark=i
 				times=0
 			for x in range(mark,mark+blocks):
 				for y in range(times*blocks,times*blocks+blocks):
 					if row==x and col==y:
 						block_num=i
			times+=1
		for ii in range(int(block_num/blocks)*blocks,int(block_num/blocks)*blocks+blocks):
 			for jj in range((block_num%blocks)*blocks,(block_num%blocks)*blocks+blocks):
 				if [ii,jj] not in related_neighbor_x:
 					related_neighbor_x.append([ii,jj])
		return related_neighbor_x

def JudgeRow(su):
	row_conflicts=0
	row_count=[]
	for row in range(len(su)):
		del row_count[:]
		for x in range(len(su)):
			row_count.append(0)
		for col in range(len(su)):
			if cmp(su[row][col],'?')==-1:
				row_count[su[row][col]-1]+=1
		for x in range(len(su)):
			if row_count[x]>1:
				row_conflicts+=1
	return row_conflicts
def JudgeCol(su):
	col_coflicts=0
	col_count=[]
	for col in range(len(su)):
		del col_count[:]
		for x in range(len(su)):
			col_count.append(0)
		for row in range(len(su)):
			if cmp(su[row][col],'?')==-1:
				col_count[sudo[row][col]-1]+=1
		for x in range(len(su)):
			if col_count[x]>1:
				col_coflicts+=1
	return col_coflicts
def JudgeBlock(su):
	times=0
	block_conflicts=0
	blocks_count=[]
	blocks=int(math.sqrt(len(su)))
	for i in range(len(su)):
 		if i==0:
 			mark=i
 		if times==len(su)/blocks:
 			mark=i
 			times=0
		del blocks_count[:]
		for x in range(len(su)):
			blocks_count.append(0)
 		for row in range(mark,mark+blocks):
 			for col in range(times*blocks,times*blocks+blocks):
 				if cmp(su[row][col],'?')==-1:
		    			blocks_count[su[row][col]-1]+=1
		for b in range(len(su)):
				if blocks_count[b]>1:
					block_conflicts+=1
		times+=1
	return block_conflicts

def Readfile(filepath):
	file = open(filepath,'r')
	lines=file.readlines()
	su= [[0 for x in range(len(lines))] for x in range(len(lines))] 
	for row in range(len(lines)):
			del su[row][:]
			line=lines[row].split(',')
			for col in range(len(lines)):
				ll=line[col].strip('\n')	
				if cmp(line[col],'?')==-1:
					ll=int(ll)
				su[row].append(ll)
	file.close()
	return su

#  Minmum remaining values
def Select_Variable(assignment):
		variable_index=[]
		questionmark_index=[]
		for i in range(0,len(assignment.sudo)):
			for j in range(0,len(assignment.sudo)):
				if cmp(assignment.sudo[i][j],'?')<>-1:
					questionmark_index.append([i,j])
		if len(questionmark_index)<>0:
			minium=len(assignment.Scan_Domain(questionmark_index[0][0],questionmark_index[0][1],assignment.domain))
			variable_index.append(questionmark_index[0][0])
			variable_index.append(questionmark_index[0][1])
			for x in range(0,len(questionmark_index)):
				if len(assignment.Scan_Domain(questionmark_index[x][0],questionmark_index[x][1],assignment.domain))<minium:
					# if len(assignment.Scan_Domain(questionmark_index[x][0],questionmark_index[x][1],assignment.domain))<>1:
					minium=len(assignment.Scan_Domain(questionmark_index[x][0],questionmark_index[x][1],assignment.domain))
					del variable_index[:]
					variable_index.append(questionmark_index[x][0])
					variable_index.append(questionmark_index[x][1])
		return variable_index

def Select_domain_of_var(assignment,V):
	for x in range(0,len(assignment.domain)):
		if len(V)<>0:
			if [V[0],V[1]] in assignment.domain[x]:
				return copy.deepcopy(assignment.domain[x][1])
			
def Rivise_domain(assignment,new_domain):
	ne=copy.deepcopy(new_domain)
	for i in range(0,len(ne)):
		for j in range(0,len(assignment.domain)):
			if ne[i][0] in assignment.domain[j]:
				del assignment.domain[j][1][:]
				for m in range(0,len(ne[i][1])):
						assignment.domain[j][1].append(ne[i][1][m])

def Iscomplete(assignment):
	domain_compelete=True
	sudo_comple=True
	for x in range(0,len(assignment.domain)):
		if len(assignment.domain[x][1])<>1:
			domain_compelete=False
	for i in range(0,len(assignment.sudo)):
		for j in range(0,len(assignment.sudo)):
			if cmp(assignment.sudo[i][j],'?')<>-1:
				sudo_comple=False
	return domain_compelete and sudo_comple

def Backtracking(assignment):
	if JudgeRow(assignment.sudo)+JudgeBlock(assignment.sudo)+JudgeCol(assignment.sudo)==0 and Iscomplete(assignment):
	  	return assignment.sudo
	result=False
	var=copy.deepcopy(Select_Variable(assignment))
	doma=copy.deepcopy(Select_domain_of_var(assignment,var))
	for value in doma:
		if assignment.Consistent(var[0],var[1],value):
			All_Constraints=[]
			original_domain_of_x=copy.deepcopy(assignment.Scan_Domain(var[0],var[1],assignment.domain))	
			if len(original_domain_of_x)==0:
				continue
			assignment.Add_value(var[0],var[1],value)
			Variable_Related_to_X=copy.deepcopy(assignment.Get_var(var[0],var[1]))
			for x in range(0,len(Variable_Related_to_X)):
				for y in range(0,len(assignment.constraints)):
					if Variable_Related_to_X[x]==assignment.constraints[y][0]:
						All_Constraints.append(assignment.constraints[y])
			new_domain_for_variable=assignment.New_Constraints(Variable_Related_to_X,assignment.domain,All_Constraints)
			if assignment.Inferences(new_domain_for_variable):
				Rivise_domain(assignment,new_domain_for_variable)
				result=Backtracking(assignment)
			if result:
				return result
			
			for i in range(0,len(assignment.domain)):
				if [var[0],var[1]] in assignment.domain[i]:
					del assignment.domain[i][1][:]
					for x in range(0,len(original_domain_of_x)):
						assignment.domain[i][1].append(original_domain_of_x[x])
		assignment.sudo[var[0]][var[1]]='?'
		print "~~~~~~~~processing~~~~~~~~"
	return False


if __name__ == "__main__":
	filepath='/Users/apple/Desktop/sudo/4*4.txt'
	sudo=Readfile(filepath)
	su=assignment(sudo)
	su.Init_Domain()
	su.Init_Constraints()
	timestart=time.time()
	result=Backtracking(su)
	if not result:
		timeend=time.time()
		print "the time cost is"
		print  timeend-timestart
		print 'Sudoku not solved!'
	else:
		timeend=time.time()
		print timeend-timestart
		print su.Print_sudo()