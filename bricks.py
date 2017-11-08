#==============================================================================================#
# Name        : bricks.py                                                                      #
# Description : The brick class definition for the tetris game.                                #
# Author      : Nguyen Hoang Nam                                                               #
# Date        : 07.11.2017                                                                     #
#==============================================================================================#


from random import randrange
from colors import *
class brick:
	position = [0,0]
	type = 0
	bricksShape = [
	[[]],

	[[1,1],
	 [1,1]],

	[[0,1,0],
	 [1,1,1]],

	[[1,1,0],
	 [0,1,1]],

	[[0,1,1],
	 [1,1,0]],

	[[1,0,0],
	 [1,1,1]],

	[[0,0,1],
	 [1,1,1]],

 	[[1,1,1,1],
	 [0,0,0,0]]

	]
	shape=[[]]
	def __init__(self,Width):
		self.type = randrange(1,8)
		self.shape=self.bricksShape[self.type]
		self.position=[0,Width//2-1]

	def rotate(self):
		self.shape=list(zip(*self.shape[::-1]))

	def fall(self):
		self.position[0]+=1

	def moveLeft(self):
		self.position[1]-=1

	def moveRight(self):
		self.position[1]+=1

	def __eq__(self,other):
		self.type=other.type
		self.shape=other.shape[:]
		self.position=other.position[:]