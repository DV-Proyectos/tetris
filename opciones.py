import pygame
import sys
import numpy as np
import menu_principal

#Creamos una clase boton
class Boton():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self,ventana):
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

#tamaño de la ventana del pygame
WINDOW_WIDTH2, WINDOW_HEIGHT2 = 600, 600
tile_size = 50

def mostrar_opciones():
	pygame.init()
	pygame.display.set_caption("OPCIONES")
	ventana = pygame.display.set_mode((WINDOW_WIDTH2, WINDOW_HEIGHT2))
	fondo = pygame.image.load("imagenes/fondotetris.png").convert()

	miFuente = pygame.font.Font(None,30)
	miTexto = miFuente.render("OPCIONES DEL JUEGO", 0, (255,255,255))

	
	#cargamos la fuente tipo arcade
	letra_arcade = pygame.font.Font("ka1.ttf", 16)
	
	#creamos los textos
	letra = letra_arcade.render("OPCIONES DEL JUEGO", 0, (255,255,255),(0,0,0))


	#esto sirve para centrar los textos de cada parrafo
	rectanguloTextoPresent = letra.get_rect()
	rectanguloTextoPresent.centerx = ventana.get_rect().centerx
	rectanguloTextoPresent.centery = 270

	

	#cargamos las imagenes para los botones
	volver_img = pygame.image.load('imagenes/volver.png') 

	# Creamos los botones para interactuar con la ventana
	#restart_button = Boton(100, 250, start_img)
	volver_boton = Boton(30,550, volver_img)
	run = True 

	#Dentro de este while se va a correr todo el codigo del pygame
	while run:

			ventana.blit(fondo, [0,0])
			ventana.blit(letra,rectanguloTextoPresent)

			if volver_boton.draw(ventana):
				menu_principal.mostrar_menu()
				break
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
		# Esto sirve para que cuando 
		# se ejecute el programa no se cuelgue la ventana.
			pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
    mostrar_opciones()




    

   
        
