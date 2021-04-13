from pygame.locals import *

from pygame import Rect
import pygame
import sys
import numpy as np


#Creamos una clase boton
class Boton():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		ventana.blit(self.image, self.rect)

		return action

#----------------------------------------------------------------------------------#

	WINDOW_WIDTH2, WINDOW_HEIGHT2 = 600, 600
	tile_size = 50

def mostrarCreditos():
 	pygame.init() 
	
	#Creo la ventana
 	ventana = pygame.display.set_mode((WINDOW_WIDTH2, WINDOW_HEIGHT2))
	pygame.display.set_caption("Creditos :) ")
		fondo = pygame.image.load("imagenes/fondotetris.png").convert()

	#cargamos las imagenes para los botones
		volver_img = pygame.image.load('imagenes/volver.png') 

	# Creamos la fuente de nuestra pantalla
	# Creamos un objeto fuente 

	# Creamos los botones para interactuar con la ventana
	#restart_button = Boton(100, 250, start_img)
		volver_boton = Boton(175, 250 , volver_img)

		run = True 
	#Dentro de este while se va a correr todo el codigo del pygame
		while run:
			

			ventana.blit(fondo, [0,0])

			if volver_boton.draw():
					run = False
					pygame.display.flip()
			# Esto sirve para que cuando 
			# se ejecute el programa no se cuelgue la ventana.
			for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()

			pygame.display.update()

		pygame.quit()





    

   
        
