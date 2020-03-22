import random
import pygame
 
pygame.init() 
 
while(True):
	for i in pygame.key.get_pressed():
		if i == 1:
			print (pygame.key.get_pressed().index(i))

	

