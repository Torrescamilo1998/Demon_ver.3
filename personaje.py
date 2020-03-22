import pygame,sys
import threading
from time import sleep 
ruta = 'media/Imagenes/Sprites/'

class personaje:
	
	

	def __init__(self, arriba, abajo, izquierda , derecha, ancho, largo,limite ,posicionInicial, skin):
		self.imagen = pygame.image.load(ruta+skin)
		self.posicionInicial = posicionInicial
		self.derecha = derecha
		self.izquierda = izquierda
		self.abajo = abajo
		self.limite = limite
		self.arriba = arriba 
		self.identacion =0
		self.ancho=ancho 
		self.largo=largo
		self.velocidad = 5
		self.Rectangulo = pygame.Rect(posicionInicial[0],posicionInicial[1]+30,20,20)
		self.List = []
		self.Impresion=(self.imagen,(self.posicionInicial),self.derecha*self.largo,self.derecha*self.largo,self.ancho,self.largo)	

		
		
		
		
	def getSpawn(self , Mapa): 
		self.Impresion = (self.imagen,(self.posicionInicial),self.derecha*self.largo,self.derecha*self.largo,self.ancho,self.largo)	
		return self.Impresion

	def movimiento(self , Mapa):

		    		    
		if pygame.key.get_pressed()[276] == 1 and permitirPaso([(self.posicionInicial[0]-self.velocidad), self.posicionInicial[1] ] , Mapa.ListRect) :
			
			#screen.fill((255,255,255))
			
			self.identacion = self.identacion +1
			self.posicionInicial[0] -=self.velocidad
			self.Impresion= (self.imagen,self.posicionInicial,self.identacion*self.ancho,self.izquierda*self.largo,self.ancho,self.largo)
			#sleep(0.05)
			
		if pygame.key.get_pressed()[274] == 1 and permitirPaso([(self.posicionInicial[0]), self.posicionInicial[1]+ self.velocidad ] , Mapa.ListRect):
			
			#screen.fill((255,255,255))
			
			self.identacion = self.identacion +1
			self.posicionInicial[1] +=self.velocidad
			self.Impresion = (self.imagen,self.posicionInicial,self.identacion*self.ancho,self.abajo*self.largo,self.ancho,self.largo)
			#sleep(0.05)					
				
		if pygame.key.get_pressed()[275] == 1 and permitirPaso([(self.posicionInicial[0]+self.velocidad), self.posicionInicial[1] ] , Mapa.ListRect):
			
			#screen.fill((255,255,255))
			self.identacion = self.identacion +1
			self.posicionInicial[0] +=self.velocidad
			self.Impresion=(self.imagen,self.posicionInicial,self.identacion*self.ancho,self.derecha*self.largo,self.ancho,self.largo)
			
			#sleep(0.05)
			
		if pygame.key.get_pressed()[273] == 1 and permitirPaso([(self.posicionInicial[0]), self.posicionInicial[1]-self.velocidad ] , Mapa.ListRect):
			
			#screen.fill((255,255,255))
			
			self.identacion = self.identacion +1
			self.posicionInicial[1] -=self.velocidad
			self.Impresion=(self.imagen,(self.posicionInicial),self.identacion*self.ancho,self.arriba*self.largo,self.ancho,self.largo)
			#sleep(0.05)	
				
		if self.identacion >= self.limite:
			self.identacion = 0	
		
		#Mapa.limpiar(self.posicionInicial)

		self.Rectangulo.left,self.Rectangulo.top = self.posicionInicial[0],self.posicionInicial[1]+30
		return self.Impresion	
		
				

class Orda:
	def __init__(self, personajes):
		self.personajes = personajes 
		
	
	def movimiento(self, Matriz):	    
		test = Matriz
		for i in self.personajes:   
	    
		    i.movimiento(test)
	
	def setPersonaje(self, personaje ):
		self.personajes.append(personaje)
		
	def borrarOrda(self):
		self.personajes = []			 	





class Mouse:
	def __init__(self):
		self.estado = False
		self.Rectangulo= pygame.Rect(0,0,0,0)
		self.a=(0,0)
	
	def seleccion(self,screen, personajes,orda):
		
		
		if pygame.mouse.get_pressed()[0]==1 and self.estado ==False :
				self.a = pygame.mouse.get_pos()
				print (self.a)
				self.estado=True
		if pygame.mouse.get_pressed()[0]==0 and self.estado==True:
					b=pygame.mouse.get_pos()
					self.estado = False
					if (self.a[0]<b[0] and self.a[1]<b[1]):
						self.Rectangulo = pygame.Rect(self.a[0],self.a[1],(b[0]-self.a[0]),(b[1]-self.a[1]))
						
					if 	(self.a[0]>b[0] and self.a[1]<b[1]):
						self.Rectangulo = pygame.Rect(b[0],self.a[1],(self.a[0]-b[0]),(b[1]-self.a[1]))
						
					if 	(self.a[0]<b[0] and self.a[1]>b[1]):
						self.Rectangulo = pygame.Rect(self.a[0],b[1],(b[0]-self.a[0]),(self.a[1]-b[1]))
						
					if 	(self.a[0]>b[0] and self.a[1]>b[1]):
						self.Rectangulo = pygame.Rect(b[0],b[1],(self.a[0]-b[0]),(self.a[1]-b[1]))
					orda.borrarOrda()
					for i in personajes:
                       
						if self.Rectangulo.contains(i.Rectangulo)==1:
							print("True")
							orda.setPersonaje(i)
							screen.blit(pygame.image.load('media/Imagenes/seleccion.png'),i.posicionInicial)

							
						    							    
							    
		
		 			 			 
					 
				
def permitirPaso(posicion, Lista):
	if (pygame.Rect(posicion[0]+10,posicion[1]+30,20,20).collidelist(Lista) == -1):
		return True 
	else:
		return False					
