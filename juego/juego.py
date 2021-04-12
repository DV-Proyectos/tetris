import pygame
from colores.colores import *
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
        grid_color = gris
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