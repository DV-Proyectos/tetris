import pygame
import sys
import tetris  #importamos los metodos del otro archivo 
import creditos
import como_jugar
from juego.juego import Boton



#cargamos las imagenes para los botones
start_img = pygame.image.load('imagenes/start.png')

comojugar_img = pygame.image.load('imagenes/comojugar.png')
salir_img = pygame.image.load('imagenes/salir2.png')
creditos_img = pygame.image.load('imagenes/creditos.png')


def mostrar_menu():

	pygame.init()
	WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600

	#Creo la ventana
	ventana = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption("TETRIS")
	fondo = pygame.image.load("imagenes/fondotetris.png").convert()
	
	start_boton = Boton(175, 250 , start_img)
	comojugar_boton = Boton(70, 330, comojugar_img)
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
			
		if  comojugar_boton.draw(ventana):
			como_jugar.mostrar_como_jugar()
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



    

   
        
