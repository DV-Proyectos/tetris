#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The classic Tetris developed using PyGame.
    Copyright (C) 2018 Recursos Python - recursospython.com.
"""

from collections import OrderedDict
import random

from pygame import Rect
import pygame
import numpy as np

#Importamos las excepciones
from excepciones.excepciones import *
from bloques.bloques import BlocksGroup

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 601
GRID_WIDTH, GRID_HEIGHT = 300, 600
TILE_SIZE = 30

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height    

class Juego():
 
    def __init__(self, window, grid, title_size):
        self.window = window
        self.grid = grid
        self.title_size = title_size
        self.COLUMNAS = 10
        self.FILAS = 20

    def draw_grid(self, background):
        """Draw the background grid."""
        grid_color = 50, 50, 50
        # Vertical lines.
        for i in range(self.COLUMNAS+1):
            x = self.title_size * i
            pygame.draw.line(
                background, grid_color, (x, 0), (x, self.grid.height)
            )
        # Horizontal liens.
        for i in range(self.FILAS+1):
            y = self.title_size * i
            pygame.draw.line(
                background, grid_color, (0, y), (self.grid.width, y)
            )
    
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
    # Create background.
    background = pygame.Surface(screen.get_size())
    bgcolor = (0, 0, 0)
    background.fill(bgcolor)
    # Draw the grid on top of the background.
    juego.draw_grid(background)
    # This makes blitting faster.
    background = background.convert()
    
    try:
        font = pygame.font.Font("Roboto-Regular.ttf", 20)
    except OSError:
        # If the font file is not available, the default will be used.
        pass
    next_block_text = font.render(
        "Siguiente figura:", True, (255, 255, 255), bgcolor)
    score_msg_text = font.render(
        "Puntaje:", True, (255, 255, 255), bgcolor)
    game_over_text = font.render(
        "¡Juego terminado!", True, (255, 220, 0), bgcolor)
    paused_text = font.render(
        "¡Juego pausado!", True, (255, 220, 0), bgcolor)
    
    # Event constants.
    MOVEMENT_KEYS = pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN
    EVENT_UPDATE_CURRENT_BLOCK = pygame.USEREVENT + 1
    EVENT_MOVE_CURRENT_BLOCK = pygame.USEREVENT + 2
    pygame.time.set_timer(EVENT_UPDATE_CURRENT_BLOCK, 1000)
    pygame.time.set_timer(EVENT_MOVE_CURRENT_BLOCK, 100)
    
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
                    paused = not paused
            
            # Stop moving blocks if the game is over or paused.
            if game_over or paused:
                continue
            
            if event.type == pygame.KEYDOWN:
                if event.key in MOVEMENT_KEYS:
                    blocks.start_moving_current_block(event.key)
            
            try:
                if event.type == EVENT_UPDATE_CURRENT_BLOCK:
                    blocks.update_current_block()
                elif event.type == EVENT_MOVE_CURRENT_BLOCK:
                    blocks.move_current_block()
            except TopReached:
                game_over = True
        
        # Draw background and grid.
        screen.blit(background, (0, 0))
        # Blocks.
        blocks.draw(screen)
        # Sidebar with misc. information.
        draw_centered_surface(screen, next_block_text, 50)
        draw_centered_surface(screen, blocks.next_block.image, 100)
        draw_centered_surface(screen, score_msg_text, 240)
        score_text = font.render(
            str(blocks.score), True, (255, 255, 255), bgcolor)
        draw_centered_surface(screen, score_text, 270)
        if paused:
            draw_centered_surface(screen, paused_text, 360)
        if game_over:
            draw_centered_surface(screen, game_over_text, 360)
        # Update.
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
