from copy import *
import heapq
def Readfile(filepath):
	file=open(filepath,'r')
	lines=file.readlines()
	origin_maze=[]
	for row in range(len(lines)):
		origin_maze.append(lines[row].strip('\n'))
	return deepcopy(origin_maze)
# def Astar():

def Formalize_maze(origin_maze):
	maze=[]
	for row in range(len(origin_maze)):
		maze.append(origin_maze[row].split(' '))
	return maze
def Update_value(path,parent):
	if parent.x==path.x:
		if parent.y<path.y:
			path.value="<"
		else:
			path.value=">"
	if parent.y==path.y:
		if parent.x>path.x:
			path.value="v"
		else:
			path.value="^"
class Block(object):
	def __init__(self,x,y,value,Iswall):
		self.value=value
		self.Iswall=Iswall
		self.processed=False
		self.x=x
		self.y=y
		self.parent=None
		self.f=0
		self.g=0
		self.h=0
class Astar(object):
	def __init__(self):
		self.openlist=[]
		heapq.heapify(self.openlist)
		self.closelist=[]
		self.blocks=[]
		self.start=None
		self.goal=None
		self.width=0
	def init_maze(self,maze):
		self.width=len(maze)
		for row in range(len(maze)):
			for col in range(len(maze[row])):
				if maze[row][col]=='1':
					self.blocks.append(Block(row,col,'#',True))
				elif maze[row][col]=='S':
					self.start=Block(row,col,'S',False)
					self.blocks.append(self.start)
				elif maze[row][col]=='G':
					self.goal=Block(row,col,'G',False)
					self.blocks.append(self.goal)
				else:
					self.blocks.append(Block(row,col,' ',False))
	def get_block(self,x,y):
		for b in range(len(self.blocks)):
			if self.blocks[b].x==x and self.blocks[b].y==y:
				return self.blocks[b]
	def get_adjacent(self,block):

		#return the adjacnet block
		adjacent_blocks=[]
		if block.x>0:
		 	b1=self.get_block(block.x-1,block.y)
		 	# if b1.value<>self.goal.value and b1.value<>self.start.value:
		 		# b1.value='|'
		 	adjacent_blocks.append(b1)
		if block.x<self.width-1:
		 	b2=self.get_block(block.x+1,block.y)
		 	# if b2.value<>self.goal.value and b2.value<>self.start.value:
		 		# b2.value='|'
		 	adjacent_blocks.append(b2)
		if block.y>0:
		 	b3=self.get_block(block.x,block.y-1)
		 	# if b3.value<>self.goal.value and b3.value<>self.start.value:
		 		# b3.value='--'
		 	adjacent_blocks.append(b3)
		if block.y<self.width-1:
		 	b4=self.get_block(block.x,block.y+1)
		 	# if b4.value<>self.goal.value and b4.value<>self.start.value:
		 		# b4.value='--'
		 	adjacent_blocks.append(b4)
		return adjacent_blocks
		 #want to get all of the blocks near the block(4-connected)
		 #4 directions, but need to think the boundry
	def Is_theBlock_In_Openlist(self,block):
		for element in self.openlist:
			# print element[1].x
			if element[1].x==block.x and element[1].y==block.y:
				return True
		return False
		# for b in range(len(self.openlist)):
		# 	print len(self.openlist[b])
		# 	
	def display(self):
		block=self.goal
		blocks=[]
		while block.parent is not self.start:
			block=block.parent
			blocks.append(block)
			# print block.value
		return blocks
	def recalculate(self,adj,block):
		adj.g=block.g+10;
		adj.h=self.get_heuristic(adj)
		adj.parent=block
		adj.f=adj.g+adj.h
	def get_heuristic(self,block):
		#regardless of the wall and calculate the shortest path from current block to the goal
		return 10*(abs(block.x-self.goal.x)+abs(block.y-self.goal.y))
	def Search(self):
		#add the startblocks into the min_queue and process it.
		heapq.heappush(self.openlist,(self.start.f, self.start))
		while len(self.openlist):
			# pop cell from heap queue
			f,block=heapq.heappop(self.openlist)
			# add cell to closed list so we don't process it twice
			self.closelist.append(block)
			block.processed=True
			# if ending cell, display found path
			if block.value==self.goal.value:
				# print self.goal.value
				# print block.value
				bs=self.display()
				return bs
			# get adjacent cells for cell
			adjancents=self.get_adjacent(block)
			for a_block in adjancents:
				if a_block.Iswall==False and a_block.processed==False:

					if self.Is_theBlock_In_Openlist(a_block):
						# print "yes"
						# print a_block.g
						# print block.g+10
						if a_block.g>block.g+10:

							#recaculate the f for ad_b
							self.recalculate(a_block,block)
					else:
						self.recalculate(a_block,block)
						heapq.heappush(self.openlist,(a_block.f,a_block))
		





if __name__=="__main__":
	filepath='/Users/apple/Desktop/maze.txt'
	output=''
	print "The maze is:"
	o_maze=Readfile(filepath)
	for row in range(len(o_maze)):
		print o_maze[row]
	maze=Formalize_maze(o_maze)
	a=Astar()

	a.init_maze(maze)
	# for row in range(len(a.blocks)):
	# 	 output.append(a.blocks[row].value)
	# 	 if (row+1)%10==0:
	# 	 	print output
	# 	 	del output[:]
	bs=a.Search()
	if bs is None:
		print "\nCouldn't find any path!\n"
	else:
		parent=a.goal
		for b in range(len(bs)):
			Update_value(bs[b],parent)
			parent=bs[b]

	# a.init_maze(maze)
		print "\nThe shortest path is:"
		for row in range(len(a.blocks)):
		# for c in range(len(bs)):
			# if a.blocks[row].x==bs[c].x and a.blocks[row].y==bs[c].y:
			# 	a.blocks[row].value=bs[c].value
			output+=" "+a.blocks[row].value
			if (row+1)%10==0:
		 		print output
		 		output=''