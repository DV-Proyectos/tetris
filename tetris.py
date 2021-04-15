#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The classic Tetris developed using PyGame.
    Copyright (C) 2018 Recursos Python - recursospython.com.
"""
import os
import pygame
import numpy as np

#Importamos los modulos
from excepciones.excepciones import *
from colores.colores import *
from bloques.bloques import BlocksGroup
from juego.juego import *

image_play = pygame.image.load(os.path.join('imagenes', 'play.png'))
image_pause = pygame.image.load(os.path.join('imagenes', 'pause.png'))
image_retry = pygame.image.load(os.path.join('imagenes', 'retry.png'))
image_mute = pygame.image.load(os.path.join('imagenes', 'mute.png'))
image_volume = pygame.image.load(os.path.join('imagenes', 'volume.png'))
image_exit = pygame.image.load(os.path.join('imagenes', 'exit.png'))

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 601
GRID_WIDTH, GRID_HEIGHT = 300, 600
TILE_SIZE = 30
    
juego = Juego(Window(WINDOW_WIDTH,WINDOW_HEIGHT),Grid(GRID_WIDTH,GRID_HEIGHT),TILE_SIZE)

def draw_centered_surface(screen, surface, y):
    screen.blit(surface, (400 - surface.get_width()/2, y))



def main():
    
    pygame.init()
    pygame.display.set_caption("Tetris con PyGame")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    run = True
    paused = False
    game_over = False
    volume = True
    # Create background.
    background = pygame.Surface(screen.get_size())
    bgcolor = negro
    background.fill(bgcolor)

    track = pygame.mixer.Channel(0)
    track.set_volume(0.25)
    misc_sound = pygame.mixer.Channel(1)
    main_track = pygame.mixer.Sound(os.path.join('sounds', 'musica.mp3'))
    drop_audio = pygame.mixer.Sound(os.path.join('sounds', 'drop.wav'))
    lose_track = pygame.mixer.Sound(os.path.join('sounds', 'lose.mp3'))
    track.play(main_track,-1)
    # Draw the grid on top of the background.
    juego.draw_grid(background)
    # This makes blitting faster.
    background = background.convert()

    try:
        font = pygame.font.Font(os.path.join('fuentes', '8-bit-blanco.ttf'), 24)
        font_score = pygame.font.Font(os.path.join('fuentes', '8-bit-blanco.ttf'), 32)
    except OSError:
        # If the font file is not available, the default will be used.
        pass
    next_block_text = font.render(
        "Siguiente figura", True, blanco, bgcolor)
    score_msg_text = font.render(
        "Puntaje", True, blanco, bgcolor)
    game_over_text = font.render(
        "GAME OVER", True, rojo, bgcolor)
    paused_text = font.render(
        "Juego pausado", True, amarillo, bgcolor)
    boton_play_pause = Boton((400 - image_play.get_width()/2)-50,360,image_play)    
    boton_mute = Boton((400 - image_mute.get_width()/2)+50,365,image_mute)    
    boton_retry = Boton((400 - image_retry.get_width()/2)-45,490,image_retry)    
    boton_exit = Boton((400 - image_exit.get_width()/2)+45,500,image_exit)    
    
    # Event constants.
    MOVEMENT_KEYS = pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_SPACE
    EVENT_UPDATE_CURRENT_BLOCK = pygame.USEREVENT + 1
    EVENT_MOVE_CURRENT_BLOCK = pygame.USEREVENT + 2
    pygame.time.set_timer(EVENT_UPDATE_CURRENT_BLOCK, 1000)
    pygame.time.set_timer(EVENT_MOVE_CURRENT_BLOCK, 50)
    
    blocks = BlocksGroup(juego)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYUP:
                if not paused and not game_over:
                    if event.key in MOVEMENT_KEYS:
                        blocks.stop_moving_current_block()
                    elif event.key == pygame.K_UP:
                        blocks.rotate_current_block()
                
                if event.key == pygame.K_p:
                    if not game_over:
                        paused = not paused
                if event.key == pygame.K_m:
                    if volume and not game_over:
                        track.pause()
                    else:
                        track.unpause()  
                    volume = not volume  
        
            # Stop moving blocks if the game is over or paused.
            if game_over or paused:
                continue     
            if event.type == pygame.KEYDOWN:
                if event.key in MOVEMENT_KEYS:
                    blocks.start_moving_current_block(event.key)
                if event.key == pygame.K_SPACE:
                    pygame.time.set_timer(EVENT_MOVE_CURRENT_BLOCK, 1) 
                    misc_sound.play(drop_audio,0)
                else: 
                    pygame.time.set_timer(EVENT_MOVE_CURRENT_BLOCK, 50) 

            try:
                if event.type == EVENT_UPDATE_CURRENT_BLOCK:
                    blocks.update_current_block()
                elif event.type == EVENT_MOVE_CURRENT_BLOCK:
                    blocks.move_current_block()
            except TopReached:
                game_over = True
                if volume:
                    track.play(lose_track,-1)
        
        # Draw background and grid.
        screen.blit(background, (0, 0))
        # Blocks.
        blocks.draw(screen)
        # Sidebar with misc. information.
        draw_centered_surface(screen, next_block_text, 50)
        draw_centered_surface(screen, blocks.next_block.image, 100)
        draw_centered_surface(screen, score_msg_text, 240)
        score_text = font_score.render(
            str(blocks.score), True, blanco, bgcolor)
        draw_centered_surface(screen, score_text, 270)
        if boton_exit.draw(screen): 
            break
        if volume:
            boton_mute.image = image_volume
            if boton_mute.draw(screen) and not game_over:
                volume = False
                track.pause()
        else:
            boton_mute.image = image_mute
            if boton_mute.draw(screen) and not game_over:
                volume = True
                track.unpause()

        if paused:
            draw_centered_surface(screen, paused_text, 330)
            boton_play_pause.image = image_play
            if boton_play_pause.draw(screen) and not game_over:
                paused = not paused
        else: 
            boton_play_pause.image = image_pause
            if boton_play_pause.draw(screen) and not game_over:
                paused = not paused

        if game_over:
            draw_centered_surface(screen, game_over_text, 450)
            if boton_retry.draw(screen):
                main()
                break
        # Update.
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
