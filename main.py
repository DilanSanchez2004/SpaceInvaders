import pygame
import sys
from disparo import Bullet
# Inicialización de pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((640, 480))

# Título e icono del juego
pygame.display.set_caption('Space Invaders')
pygame_icon = pygame.image.load(
    'C:\\Users\\user\\Desktop\\Space Invaders\\SpaceInvaders\\sprites\\Icono.png')
pygame.display.set_icon(pygame_icon)

# Reloj para controlar la tasa de actualización
clock = pygame.time.Clock()

# Variables del juego
running = True
Fondo = pygame.image.load(
    'C:\\Users\\user\\Desktop\\Space Invaders\\SpaceInvaders\\sprites\\Fondo.png')
playerImg = pygame.image.load(
    'C:\\Users\\user\\Desktop\\Space Invaders\\SpaceInvaders\\sprites\\Player.png')
bunkerImg = pygame.image.load(
    'C:\\Users\\user\\Desktop\\Space Invaders\\SpaceInvaders\\sprites\\Bunker.png')

playerX = 300
playerY = 450
playerX_change = 0
player_speed = 300  # Pixeles por segundo

# Función para dibujar al jugador


def player(x, y):
    screen.blit(playerImg, (x, y))


# Función para disparar balas
def shoot_bullet(playerX, playerY, all_sprites, bullets):
    bullet = Bullet(playerX, playerY)
    all_sprites.add(bullet)
    bullets.add(bullet)


# Inicialización de grupos de sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()


def bunkers(x, y):
    screen.blit(bunkerImg, (x, y))


while running:
    # Encuesta de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot_bullet(playerX + playerImg.get_width() // 2,
                             playerY, all_sprites, bullets)  # Crear una nueva bala

    # Obtener el estado actual de las teclas
    keys = pygame.key.get_pressed()
    playerX_change = 0
    if keys[pygame.K_a]:
        playerX_change = -player_speed
    if keys[pygame.K_d]:
        playerX_change = player_speed

    # Actualizar la posición del jugador
    dt = clock.tick(60) / 1000  # Calcular el tiempo transcurrido en segundos
    playerX += playerX_change * dt

    # Asegurarse de que el jugador no se salga de los límites de la pantalla
    if playerX < 0:
        playerX = 0
    elif playerX > 640 - playerImg.get_width():
        playerX = 640 - playerImg.get_width()

    # Rellenar la pantalla con el fondo
    screen.blit(Fondo, (-30, 0))

    # Dibujar al jugador en la nueva posición
    player(playerX, playerY)

    # Dibujar los bunkers
    bunkers(70, 390)
    bunkers(180, 390)
    bunkers(290, 390)
    bunkers(400, 390)
    bunkers(510, 390)

    # Actualizar y dibujar todos los sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.update()

pygame.quit()
