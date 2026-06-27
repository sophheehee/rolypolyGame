import pygame

pygame.init()

# initialize the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Roly Poly Game")

player = pygame.Rect(100, 100, 50, 50)

#create game loop 
running = True
while running:
    screen.fill((0, 0, 0)) #fill screen with black (so there's not a trail of player)
    pygame.draw.rect(screen, (255, 0, 0), player)

    # determine which keys are pressed for movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
