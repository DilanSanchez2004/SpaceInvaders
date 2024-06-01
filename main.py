# Importación de la libreria "game loop"
import pygame

# Se define el lienzo y su tamaño
pygame.init()
# icono del juego
pygame_icon = pygame.image.load(
    'C:\\Users\\user\\Desktop\\Space Invaders\\SpaceInvaders\\sprites\\icono_invader.jpg')
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('Space Invaders')  # titulo del juego
screen = pygame.display.set_mode((640, 480))  # resolucion del juego
clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(
    screen.get_width() / 2, screen.get_height() / 1.08)

while running:  # ciclo infinito del juego

    # Creacion de lienzo
    for event in pygame.event.get():  # encuesta para eventos
        if event.type == pygame.QUIT:  # evento pygame.QUIT significa que el usuario hizo clic en X para cerrar la ventana
            running = False

    screen.fill("black")

    pygame.draw.circle(screen, "white", player_pos, 15)

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    # llenar la pantalla con un color para borrar cualquier cosa del último fotograma

    # RENDER YOUR GAME HERE

    # flip() la pantalla para poner tu trabajo en pantalla
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limite de FPS a 60

pygame.quit()
