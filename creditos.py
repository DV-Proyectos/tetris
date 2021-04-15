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

def mostrar_creditos():
	pygame.init()
	pygame.display.set_caption("Creditos:)")
	ventana = pygame.display.set_mode((WINDOW_WIDTH2, WINDOW_HEIGHT2))
	fondo = pygame.image.load("imagenes/fondotetris.png").convert()

	miFuente = pygame.font.Font(None,30)
	miTexto = miFuente.render("Proyecto para la materia de Ingracion Tecnologica", 0, (255,255,255))

	
	#cargamos la fuente tipo arcade
	letra_arcade = pygame.font.Font("ka1.ttf", 16)
	
	#creamos los textos
	letra = letra_arcade.render("Proyecto para la materia de Ingracion Tecnologica", 0, (255,255,255),(0,0,0))
	letra2 = letra_arcade.render("Integrantes", 0, (200,200,200) )
	letra3 = letra_arcade.render("Chen David  Romero Daiana  Torres Maximiliano", 0, (200,200,200) )	
	letra4 = letra_arcade.render("DOCENTE",0, (200,200,200) )	
	letra5 = letra_arcade.render("MISAEL CUDEK", 0, (200,200,200) )	

	#esto sirve para centrar los textos de cada parrafo
	rectanguloTextoPresent = letra.get_rect()
	rectanguloTextoPresent.centerx = ventana.get_rect().centerx
	rectanguloTextoPresent.centery = 300

	rectanguloTextoPresent2 = letra2.get_rect()
	rectanguloTextoPresent2.centerx = ventana.get_rect().centerx
	rectanguloTextoPresent2.centery = 350

	rectanguloTextoPresent3 = letra3.get_rect()
	rectanguloTextoPresent3.centerx = ventana.get_rect().centerx
	rectanguloTextoPresent3.centery = 400

	rectanguloTextoPresent4 = letra4.get_rect()
	rectanguloTextoPresent4.centerx = ventana.get_rect().centerx
	rectanguloTextoPresent4.centery = 450

	rectanguloTextoPresent5 = letra5.get_rect()
	rectanguloTextoPresent5.centerx = ventana.get_rect().centerx
	rectanguloTextoPresent5.centery = 500

	#cargamos las imagenes para los botones
	volver_img = pygame.image.load('imagenes/volver.png') 

	# Creamos los botones para interactuar con la ventana
	#restart_button = Boton(100, 250, start_img)
	volver_boton = Boton(30,550, volver_img)
	run = True 

	#Dentro de este while se va a correr todo el codigo del pygame
	while run:

			ventana.blit(fondo, [0,0])
			ventana.blit(letra, rectanguloTextoPresent)
			ventana.blit(letra2, rectanguloTextoPresent2)
			ventana.blit(letra3, rectanguloTextoPresent3)
			ventana.blit(letra4, rectanguloTextoPresent4)
			ventana.blit(letra5, rectanguloTextoPresent5)
			
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
    mostrar_creditos()




    

   
        
