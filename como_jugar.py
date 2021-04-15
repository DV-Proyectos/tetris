import os
import pygame
import sys
import menu_principal
from juego.juego import Boton
from colores.colores import *
#tamaño de la ventana del pygame
WINDOW_WIDTH2, WINDOW_HEIGHT2 = 600, 600

def mostrar_como_jugar():
	pygame.init()
	pygame.display.set_caption("Cómo Jugar?")
	ventana = pygame.display.set_mode((WINDOW_WIDTH2, WINDOW_HEIGHT2))	

	#cargamos la fuente tipo arcade
	letra_arcade = pygame.font.Font(os.path.join('fuentes', "ka1.ttf"), 30)
	
	#creamos los textos
	letra = letra_arcade.render("TECLAS DEL JUEGO", 0, blanco)

	textoUP = letra_arcade.render("ROTAR FICHA", 0, blanco)
	textoDOWN = letra_arcade.render("BAJAR FICHA", 0, blanco)
	textoIZQ = letra_arcade.render("MOVER A IZQUIERDA", 0, blanco)
	textoDER = letra_arcade.render("MOVER A DERECHA", 0, blanco)
	textoSPACE = letra_arcade.render("HARD DROP", 0, blanco)
	textoP = letra_arcade.render("PAUSA", 0, blanco)
	textoM = letra_arcade.render("MUTEAR", 0, blanco)



	#esto sirve para centrar los textos de cada parrafo
	rectanguloTextoPresent = letra.get_rect()
	rectanguloTextoPresent.centerx = ventana.get_rect().centerx
	rectanguloTextoPresent.centery = 50

	

	#cargamos las imagenes para los botones
	volver_img = pygame.image.load(os.path.join('imagenes', 'volver.png')) 

	flecha_der = pygame.image.load(os.path.join('imagenes', "flechader.png"))
	flecha_izq = pygame.image.load(os.path.join('imagenes', "flechaizq.png"))
	flecha_up = pygame.image.load(os.path.join('imagenes', "flechaup.png"))
	flecha_down = pygame.image.load(os.path.join('imagenes', "flechadown.png"))

	space = pygame.image.load(os.path.join('imagenes', "space2.png"))
	tecla_p = pygame.image.load(os.path.join('imagenes', "teclaP.png"))
	tecla_m = pygame.image.load(os.path.join('imagenes', "teclaM.png"))


	# Creamos los botones para interactuar con la ventana
	#restart_button = Boton(100, 250, start_img)
	volver_boton = Boton(30,550, volver_img)
	
	run = True 

	#Dentro de este while se va a correr todo el codigo del pygame
	while run:

			ventana.fill((14,8,52))
			ventana.blit(letra,rectanguloTextoPresent)
			
			#ventana de flechas
			ventana.blit(flecha_up,[70,100])
			ventana.blit(textoUP,[150,100])

			ventana.blit(flecha_izq,[70,180])
			ventana.blit(textoIZQ,[150,180])

			ventana.blit(flecha_der,[70,260])
			ventana.blit(textoDER,[150,260])

			ventana.blit(flecha_down,[70,340])
			ventana.blit(textoDOWN,[150,340])

			ventana.blit(space,[70,420])
			ventana.blit(textoSPACE,[210,420])

			ventana.blit(tecla_p,[70,480])
			ventana.blit(textoP,[150,480])

			ventana.blit(tecla_m,[330,480])
			ventana.blit(textoM,[410,480])
			

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
    mostrar_como_jugar()




    

   
        
