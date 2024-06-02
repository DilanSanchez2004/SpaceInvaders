import pygame
import sys

# Clase para la bala
bulletImg = pygame.image.load(
    'C:\\Users\\user\\Desktop\\Space Invaders\\SpaceInvaders\\sprites\\Laser.png')


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bulletImg
        self.image.fill((255, 255, 255))  # Color blanco
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= 10
        # Elimina la bala si sale de la pantalla
        if self.rect.bottom < 0:
            self.kill()
