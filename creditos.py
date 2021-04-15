import os
import pygame
import sys
import menu_principal
from juego.juego import Boton
from colores.colores import *
#----------------------------------------------------------------------------------#

#tamaño de la ventana del pygame
WINDOW_WIDTH2, WINDOW_HEIGHT2 = 600, 600

def mostrar_creditos():
	pygame.init()
	pygame.display.set_caption("Creditos:)")
	ventana = pygame.display.set_mode((WINDOW_WIDTH2, WINDOW_HEIGHT2))
	fondo = pygame.image.load(os.path.join('imagenes', "fondotetris.png")).convert()
	
	#cargamos la fuente tipo arcade
	letra_arcade = pygame.font.Font(os.path.join('fuentes', "ka1.ttf"), 16)
	
	#creamos los textos
	letra = letra_arcade.render("Proyecto para la materia de Ingracion Tecnologica", 0, blanco,(0,0,0))
	letra2 = letra_arcade.render("Integrantes", 0, gris_claro )
	letra3 = letra_arcade.render("Chen David  Romero Daiana  Torres Maximiliano", 0, gris_claro )	
	letra4 = letra_arcade.render("DOCENTE",0, gris_claro )	
	letra5 = letra_arcade.render("MISAEL CUDEK", 0, gris_claro )	

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
	volver_img = pygame.image.load(os.path.join('imagenes', 'volver.png')) 

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




    

   
        
