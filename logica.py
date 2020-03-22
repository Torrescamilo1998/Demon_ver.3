import time
import pygame,sys,random
from personaje import *
from aura import *
import threading
		
		
class mediadorLogico:
	def __init__(self, Mapa, MapaLogico, Personajes):
		self.Mapa = Mapa
		self.MapaLogico = MapaLogico
		self.Personajes = Personajes 
		
		
	def actualizacion():
		Mapa.MatrizLogica =	Mapa.MatrizLogica2
		 
	def generarMateriales(self):
		for j in range (0,50):
		  for i in range (1,2):
		    x = random.randint(3,480)
		    y = random.randint(3,480)
		    self.Mapa.MatrizLogica[y][x] = i
		    self.Mapa.MatrizLogica[y+1][x] = i
		    self.Mapa.MatrizLogica[y][x+1] = i
		    self.Mapa.MatrizLogica[y+1][x+1] = i
	
	
	def crearLogicaRestrictiva(self):
		for i in range (0,self.Mapa.dimension):
		   for j in range (0,self.Mapa.dimension):
			   if self.Mapa.MatrizLogica[i][j] ==1:
				   self.MapaLogico.ListRect.append(pygame.Rect(j*46,i*64,46,64))	  
			   if self.Mapa.MatrizLogica[i][j]==2:
				   self.MapaLogico.ListRect.append(pygame.Rect(j*46,i*64,46,64))
	
	
	
	def mediarImpresionPersonajes(self):
	   self.Mapa.imprimirMapa(self.Mapa.screen)
	   for i in self.Personajes:
		   elem = i.movimiento(self.MapaLogico)
		   self.Mapa.screen.blit(elem[0],elem[1],(elem[2],elem[3],elem[4],elem[5]))
		   
	def mediarEstado(self):
		if pygame.mouse.get_pressed()[0]==1:
		  R = Recolectando()	
		  a = pygame.mouse.get_pos()	
		  for i in self.Personajes:
			  if i.Rectangulo.collidepoint(a):
				  
				  R.actuar(i)
				  R = Construyendo()
				  R.actuar(i)
				  R = Atacando() 
				  R.actuar(i)
				  
					   




class boton():
	def __init__(self, texto,screen):
		self.text = texto
		self.screen = screen 
	
			   




class IEstadoPersonaje:
	def actuar(self,personaje):
		pass



class Recolectando(IEstadoPersonaje):
	
	def actuar (self,personaje):
		print ("soldado en posicion: " + str(personaje.posicionInicial) + " 	Recolectando materiales" )
		


class Atacando(IEstadoPersonaje):
	
	def actuar (self,personaje):
		print ("soldado en posicion: " + str(personaje.posicionInicial) + " Atacando" )



class Construyendo(IEstadoPersonaje):
	
	def actuar (self, personaje):
		print ("soldado en posicion: " + str(personaje.posicionInicial) + " Construyendo" )
