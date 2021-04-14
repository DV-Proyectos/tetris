from pygame import Rect
import pygame
import sys
import numpy as np
import tetris  #importamos los metodos del otro archivo 
import creditos
import opciones


pygame.init()
#WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
#tile_size = 50

#Creo la ventana
#ventana = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#pygame.display.set_caption("TETRIS")
#fondo = pygame.image.load("imagenes/fondotetris.png").convert()

# Creamos la fuente de nuestra pantalla
# Creamos un objeto fuente 
miFuente = pygame.font.Font(None,30)
miTexto = miFuente.render("Start", 0, (200,60,80),(224,231,122))
miTexto2 = miFuente.render("Opciones", 0, (255,255,255))

#cargamos las imagenes para los botones
start_img = pygame.image.load('imagenes/start.png')
opciones_img = pygame.image.load('imagenes/opciones2.png')
salir_img = pygame.image.load('imagenes/salir2.png')
creditos_img = pygame.image.load('imagenes/creditos.png')

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
#-----------------------------------------------------------------------------------#

#Leer archivo desde funcion
archivo = open("creditos.txt","r")
contenido = archivo.read()


def mostrar_menu():

	pygame.init()
	WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
	tile_size = 50

#Creo la ventana
	ventana = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption("TETRIS")
	fondo = pygame.image.load("imagenes/fondotetris.png").convert()
	
	start_boton = Boton(175, 250 , start_img)
	opciones_boton = Boton(120, 330, opciones_img)
	creditos_boton = Boton(125,410, creditos_img)
	quit_boton = Boton(190 , 490, salir_img)

	#Declaramos una variable cualquiera, en este caso run 
	run = True

	#Dentro de este while se va a correr todo el codigo del pygame
	while run:
	
		ventana.blit(fondo, [0,0])

		if start_boton.draw(ventana):
			tetris.main()
			break
			
		if opciones_boton.draw(ventana):
			opciones.mostrar_opciones()
			break

		if creditos_boton.draw(ventana):
			creditos.mostrar_creditos()
			break

		if quit_boton.draw(ventana):
			run = False

	# Esto sirve para que cuando 
	# se ejecute el programa no se cuelgue la ventana.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
	pygame.quit()

if __name__ == "__main__":
    mostrar_menu()



    

   
        
