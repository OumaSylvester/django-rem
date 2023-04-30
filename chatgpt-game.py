import pygame

pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ChatGPT's Adventure")

# Load the player character
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                jump()  # Jump function to be implemented

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update the player position
    player_x += player_x_change

    # Draw the player character
    screen.blit(player_img, (player_x, player_y))

    # Update the screen
    pygame.display.update()

# Quit the game
pygame.quit()
