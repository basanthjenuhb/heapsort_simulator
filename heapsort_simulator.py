import pygame,sys
from pygame.locals import *
from random import randint
import time

y=1
x_square=10
y_square=80
duration=1.5
WHITE=(255,255,255)
YELLOW=(255,255,0)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
sorted_array=[]

def add_squares():
	for square in Square.all_squares:
		square.draw_square()

def display_tree(i,j):
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(WHITE)
	add_squares()
	add_nodes()
	draw_all_lines()
	draw_all_nodes(i,j)
	pygame.display.update()
	time.sleep(duration)

def heapify(i):
	k=i*2+1
	display_tree(i,-1)
	if k>len(array)-1:
		return
	if k+1<len(array) and array[k+1]>array[k]:
		k+=1
	if array[i]<array[k]:
		display_tree(i,k)
		temp=array[i]
		array[i]=array[k]
		array[k]=temp
		display_tree(i,-1)
		heapify(k)

def construct():
	i=len(array)/2-1
	while i>=0:
		heapify(i)
		screen.fill(WHITE)
		add_nodes()
		draw_all_lines()
		draw_all_nodes(i,-1)
		pygame.display.update()
		time.sleep(duration)
		i-=1


def text(screen,text,x,y,size=20,color=(255,255,255),fonttype="Monospace"):
    text=str(text)
    font=pygame.font.SysFont(fonttype,size)
    text=font.render(text,True,color)
    screen.blit(text,(x,y))

def draw_all_lines():
	i=0
	while i<len(source):
		pygame.draw.line(screen,BLACK,source[i],destination[i],2)
		i+=1

class Square:
	all_squares=[]
	def __init__(self,x,y,color,radius,num):
		self.x=x
		self.y=y
		self.num=num
		self.color=color
		self.radius=radius
		Square.all_squares.insert(0,self)

	def draw_square(self):
		pygame.draw.rect(screen,self.color,(self.x,self.y,self.radius-13,self.radius+10))
		text(screen,str(self.num),self.x+10,self.y+10,20,BLACK)

class Node:
	all_nodes=[]
	def __init__(self,x,y,color,radius,num):
		self.x=x
		self.y=y
		self.num=num
		self.color=color
		self.radius=radius
		Node.all_nodes.append(self)

	def draw_node(self):
		pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
		text(screen,str(self.num),self.x-10,self.y-10,20,BLACK)

def draw_all_nodes(k,j):
	i=0
	while i<len(Node.all_nodes):
		Node.all_nodes[i].draw_node()
		if i==k:
			pygame.draw.circle(screen, RED, (Node.all_nodes[i].x, Node.all_nodes[i].y), 30, 5)
		if i==j:
			pygame.draw.circle(screen, BLUE, (Node.all_nodes[j].x, Node.all_nodes[j].y), 30, 5)
		i+=1

def add_nodes():
	Node.all_nodes=[]
	j=0
	y=100
	l=0
	while pow(2,j)<=len(array):
			i=0
			k=scr_width/(pow(2,j)+1)
			y+=100
			x=0
			while i<pow(2,j):
				x+=k
				if l<len(array):
					Node(x,y,YELLOW,30,array[l])
					l+=1
				i+=1
			j+=1


array=[]
n=input("Enter no of elements: ")
while len(array)<n:
	array.append(randint(0,100))
print array
pygame.init()
y,x,l=0,0,0
scr_width,scr_height=1330,1020
screen=pygame.display.set_mode((scr_width,scr_height),RESIZABLE)
i,j=0,0

add_nodes()
pygame.display.set_caption('SE Project - Graphical Simulation of Heapsort')
i,j,k=0,0,0
source=[]
destination=[]
while i<len(Node.all_nodes)/2:
	k=2*i
	if k+1<len(Node.all_nodes):
		dummy1=[]
		dummy1.append(Node.all_nodes[i].x)
		dummy1.append(Node.all_nodes[i].y)
		source.append(dummy1)
		dummy2=[]
		dummy2.append(Node.all_nodes[k+1].x)
		dummy2.append(Node.all_nodes[k+1].y)
		destination.append(dummy2)
	if k+2<len(Node.all_nodes):
		dummy1=[]
		dummy1.append(Node.all_nodes[i].x)
		dummy1.append(Node.all_nodes[i].y)
		source.append(dummy1)
		dummy2=[]
		dummy2.append(Node.all_nodes[k+2].x)
		dummy2.append(Node.all_nodes[k+2].y)
		destination.append(dummy2)
	i+=1
screen.fill(WHITE)
draw_all_lines()
draw_all_nodes(0,-1)
pygame.display.update()
construct()
i=0
while i<len(array)-1:
	display_tree(0,len(array)-1)
	temp=array[0]
	array[0]=array[len(array)-1]
	array[len(array)-1]=temp
	display_tree(0,len(array)-1)
	sorted_array.insert(0,array[-1])
	Square(x_square,y_square,YELLOW,50,array[-1])
	x_square+=35

	del array[-1]
	del source[-1]
	del destination[-1]
	time.sleep(2)
	display_tree(0,-1)
	heapify(0)
sorted_array.insert(0,array[-1])
Square(x_square,y_square,YELLOW,50,array[-1])
display_tree(-1,-1)
del array[-1]
print sorted_array
while 1:
	screen.fill(WHITE)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	display_tree(-1,-1)