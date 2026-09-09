import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake settings
block = 20
speed = 10

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def message(text):
    msg = font.render(text, True, WHITE)
    screen.blit(msg, (150, 180))

def game():
    x = WIDTH // 2
    y = HEIGHT // 2

    dx = 0
    dy = 0

    snake = []
    length = 1

    food_x = random.randrange(0, WIDTH - block, block)
    food_y = random.randrange(0, HEIGHT - block, block)

    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = block
                    dx = 0

        x += dx
        y += dy

        # Wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False

        head = [x, y]
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        # Self collision
        for part in snake[:-1]:
            if part == head:
                running = False

        # Draw apple
        pygame.draw.rect(screen, RED, [food_x, food_y, block, block])

        # Draw snake
        for part in snake:
            pygame.draw.rect(screen, GREEN, [part[0], part[1], block, block])

        # Eat apple
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - block, block)
            food_y = random.randrange(0, HEIGHT - block, block)
            length += 1

        score = font.render("Score: " + str(length - 1), True, WHITE)
        screen.blit(score, (10, 10))

        pygame.display.update()
        clock.tick(speed)

    screen.fill(BLACK)
    message("Game Over!")
    pygame.display.update()
    pygame.time.wait(2000)

game()
pygame.quit()
