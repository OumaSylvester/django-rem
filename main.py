import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up game variables
background_color = (0, 0, 0)
player_color = (255, 255, 255)
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_height // 2
player_speed = 5
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

obstacle_color = (255, 0, 0)
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 3
obstacle_list = []

# Set up game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Spawn obstacles
    if random.randint(0, 100) < 10:
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        obstacle_list.append(obstacle_rect)

    # Move obstacles
    for obstacle_rect in obstacle_list:
        obstacle_rect.y += obstacle_speed

    # Remove obstacles that have gone off screen
    obstacle_list = [obstacle_rect for obstacle_rect in obstacle_list if obstacle_rect.y < screen_height]

    # Draw screen
    screen.fill(background_color)
    pygame.draw.rect(screen, player_color, player_rect)
    for obstacle_rect in obstacle_list:
        pygame.draw.rect(screen, obstacle_color, obstacle_rect)
    pygame.display.flip()

    # Set up clock
    clock = pygame.time.Clock()
    clock.tick(60)

# Quit Pygame
pygame.quit()
