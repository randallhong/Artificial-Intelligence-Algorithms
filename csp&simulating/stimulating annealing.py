import string
import math
import random
##Implementation: Sudoku 1
# from random import random,shuffle,randint,sample
import copy
import time
total_questionmark_indices=[]
def Readfile(filepath):
	file = open(filepath,'r')
	lines=file.readlines()
	sudo= [[0 for x in range(len(lines))] for x in range(len(lines))] 
	for row in range(len(lines)):
			del sudo[row][:]
			line=lines[row].split(',')
			for col in range(len(lines)):
				ll=line[col].strip('\n')	
				if cmp(line[col],'?')==-1:
					ll=int(ll)
				sudo[row].append(ll)
	file.close()
	return sudo
	


# ##Implementation: Sudoku 2
# ##Valid the initial state of the Sudoku
# ##Judge the row, count the conflicts
# #Judge the col, count the conflicts
# #Judge teh block, count the conflicts 
# #1st judge the row, return the num of conflicts
# ##remeber the index of row_count begin with "0" not "1"

def JudgeRowConflicts(sudo):
			row_conflicts=0
			row_count=[]
			for row in range(len(sudo)):
				del row_count[:]
				for x in range(len(sudo)):
					row_count.append(0)
				for col in range(len(sudo)):
					if sudo[row][col]<>'?':
		    				row_count[sudo[row][col]-1]+=1
				for x in range(len(sudo)):
					if row_count[x]>1:
						row_conflicts+=1
			return row_conflicts

# #2nd Judge the col, return the num of conflicts
def JudgeColConflicts(sudo):
			col_coflicts=0
			col_count=[]
			for col in range(len(sudo)):
				del col_count[:]
				for x in range(len(sudo)):
					col_count.append(0)
				for row in range(len(sudo)):
					if sudo[row][col]<>'?':
		    				col_count[sudo[row][col]-1]+=1
				for x in range(len(sudo)):
					if col_count[x]>1:
						col_coflicts+=1
			return col_coflicts

#Judge the blocks, retrun the num of conflicts
def JudgeBlockConflicts(sudo):
	times=0
	block_conflicts=0
	blocks_count=[]
	blocks=int(math.sqrt(len(sudo)))
	for i in range(len(sudo)):
 		if i==0:
 			mark=i
 		if times==len(sudo)/blocks:
 			mark=i
 			times=0
		del blocks_count[:]
		for x in range(len(sudo)):
			blocks_count.append(0)
 		for row in range(mark,mark+blocks):
 			for col in range(times*blocks,times*blocks+blocks):
 				if cmp(sudo[row][col],'?')==-1:
		    			blocks_count[sudo[row][col]-1]+=1
		for b in range(len(sudo)):
				if blocks_count[b]>1:
					block_conflicts+=1
		times+=1
	return block_conflicts


def Score(sudo):
	score=JudgeRowConflicts(sudo)+JudgeColConflicts(sudo)
	return score


def Randomize_on_questionmarks(sudo):
	times=0
	blocks=int(math.sqrt(len(sudo)))
	for i in range(len(sudo)):
		questionmark_indices=[]
		del questionmark_indices[:]
		block=[]
		del block[:]
 		if i==0:
 			mark=i
 		if times==len(sudo)/blocks:
 			mark=i
 			times=0
 		for row in range(mark,mark+blocks):
 			for col in range(times*blocks,times*blocks+blocks):
 				if cmp(sudo[row][col],'?')<>-1:
 					questionmark_indices.append([row,col])
 					total_questionmark_indices.append([row,col])
 				else:
 					block.append(sudo[row][col])
		fill = [i for i in range(1,len(sudo)+1) if i not in block]
		random.shuffle(fill)
		for index, value in zip(questionmark_indices, fill):
			sudo[index[0]][index[1]] = value      
		times+=1
	return sudo

#swap two value in a block

def GetTheNeighbor(sudo):
	#random get a block
	new_neighbor=copy.deepcopy(sudo)
	block =random.randint(0,len(new_neighbor)-1)
	blocks=int(math.sqrt(len(new_neighbor)))
	#then random choose two indeices in this block
	block_indices=[]
	#print int(block/blocks)
	for i in range(int(block/blocks)*blocks,int(block/blocks)*blocks+blocks):
 			for j in range((block%blocks)*blocks,(block%blocks)*blocks+blocks):
 					if [i,j] in total_questionmark_indices:
 						block_indices.append([i,j])
 	if len(block_indices)>=2:				
		random_squares = random.sample(range(len(block_indices)),2)
		new_neighbor[block_indices[random_squares[1]][0]][block_indices[random_squares[1]][1]], new_neighbor[block_indices[random_squares[0]][0]][block_indices[random_squares[0]][1]] = new_neighbor[block_indices[random_squares[0]][0]][block_indices[random_squares[0]][1]] , new_neighbor[block_indices[random_squares[1]][0]][block_indices[random_squares[1]][1]]
	return new_neighbor
def Schedule(tt):
	tnew=tt*0.99999
	return tnew

def Solver(sudo):
 	Randomize_on_questionmarks(sudo)
 	current_score=Score(sudo)
 	T=0.8
 	best_score = current_score
 	for i in range(1,10000000):
 		print "~~~~~~processing~~~~~~~"
 		print "Current T is "
 		print T
 		print "the less conflicts is"
 		print best_score
 		T=Schedule(T)
 		if T==float(0):
 			return sudo
 		neighbor = GetTheNeighbor(sudo)
 		neighbor_score = Score(neighbor)
 		delta_E=float(current_score-neighbor_score)
 		if delta_E>0 :
 			sudo=neighbor
 			current_score=neighbor_score
 		if delta_E<0:
 			if ((math.exp((delta_E/T))-random.random())>=0):
 				sudo=neighbor
 				current_score=neighbor_score	
 		if(current_score<best_score):
 			best_neightbor=copy.deepcopy(sudo)
 			best_score=Score(best_neightbor)
 		if (neighbor_score==0):
 			sudo=neighbor
 			break
 	if best_score==0:
 		print "the less conflicts is"
 		print best_score
 		print("Sudoku solved!")
 	return sudo
    





if __name__ == "__main__":
	filepath='/Users/apple/Desktop/sudo/4*4.txt'
	sudo=Readfile(filepath)
	print JudgeRowConflicts(sudo)+JudgeColConflicts(sudo)+JudgeBlockConflicts(sudo)
	timestart=time.time()
	su=Solver(sudo)
	timeend=time.time()
	print "the time cost is"
	print timeend-timestart
	print su
	