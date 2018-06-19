import math
from pygame.math import Vector2

class Rectangle:
    def __init__(self, bounds, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        pass

    def draw(self, screen, pygame):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)
