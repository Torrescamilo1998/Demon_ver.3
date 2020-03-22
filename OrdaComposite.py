import pygame,sys,random
import threading
from time import sleep 

pygame.init()
screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
pygame.display.get_caption()
Rect1 = pygame.Rect(200,200,10,10)
Rect2 = pygame.Rect(0,0,100,100)
estado=False
class Mouse:
	def __init__(self):
		self.estado = False
		self.Rectangulo= (0,0,0,0)
		self.a=(0,0)
	
	def seleccion(self,screen):
		
		
		if pygame.mouse.get_pressed()[0]==1 and self.estado ==False :
				self.a = pygame.mouse.get_pos()
				print (self.a)
				self.estado=True
		if pygame.mouse.get_pressed()[0]==0 and self.estado==True:
					b=pygame.mouse.get_pos()
					print (b)
					self.estado = False
					if (self.a[0]<b[0] and self.a[1]<b[1]):
						self.Rectangulo = pygame.Rect(self.a[0],self.a[1],(b[0]-self.a[0]),(b[1]-self.a[1]))
						
					if 	(self.a[0]>b[0] and self.a[1]<b[1]):
						self.Rectangulo = pygame.Rect(b[0],self.a[1],(self.a[0]-b[0]),(b[1]-self.a[1]))
						
					if 	(self.a[0]<b[0] and self.a[1]>b[1]):
						self.Rectangulo = pygame.Rect(self.a[0],b[1],(b[0]-self.a[0]),(self.a[1]-b[1]))
						
					if 	(self.a[0]>b[0] and self.a[1]>b[1]):
						self.Rectangulo = pygame.Rect(b[0],b[1],(self.a[0]-b[0]),(self.a[1]-b[1]))	
						
					print (self.Rectangulo)	
					pygame.draw.rect(screen,(255,255,255),self.Rectangulo)	
					sleep(0.05)

def main():
	dimension=500
	MatrizLogica=[[0 for x in range(dimension)] for y in range(dimension)]
	
	
	for i in range (0,dimension):
		   for j in range (0,dimension):
			   MatrizLogica[i][j]= random.randint(0,2)
			   if MatrizLogica[i][j] ==1 or MatrizLogica[i][j]==2:
				   pygame.draw.rect(screen,(255,255,255),pygame.Rect(j,i,20,20))
				   
				   
	


 

main()
