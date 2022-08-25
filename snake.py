import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
ORANGE = (255, 128, 0)

width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("new times roman", 45)

x, y = 600/2-7, 400/2-7

snake_list = []

points = 0

direction = ""

vel = 4

game_over = False

random_x = random.randint(0, 585)
random_y = random.randint(0, 385)
while random_x == x and random_y == y:
    random_x = random.randint(0, 585)
    random_y = random.randint(0, 385)
fruit = pygame.Rect(random_x, random_y, 14, 14)

snake = pygame.Rect(x, y, 14, 14)

def your_score(score):
    value = font.render("Score: " + str(score), True, BLUE)
    screen.blit(value, [0, 0])

while True:
    if not game_over:
        snake_head = [snake.x, snake.y]
        snake_list.append(snake_head)

        collide = snake.colliderect(fruit)

        if collide:
            random_x = random.randint(0, 585)
            random_y = random.randint(0, 385)
            for q in snake_list:
                while q == [random_x, random_y]:
                    random_x = random.randint(0, 585)
                    random_y = random.randint(0, 385)
            fruit = pygame.Rect(random_x, random_y, 14, 14)
            points += 1
            snake_list.append([snake.x, snake.y])
        screen.fill(BLACK)
        your_score(points)
        pygame.draw.rect(screen, GREEN, snake)
        pygame.draw.rect(screen, RED, fruit)

        for x in snake_list[:-3]:
            if x == snake_head:
                game_over = True

        if len(snake_list) > points:
          del snake_list[0]

        if snake.x >= 600 or snake.x < 0 or snake.y >= 400 or snake.y < 0:
            game_over = True

        for snake_block in snake_list:
            pygame.draw.rect(screen, GREEN,[snake_block[0], snake_block[1], 14, 14])


    else:
        score = font.render("You scored " + str(points) + " points.", True, BLUE)
        screen.blit(score, (10, height / 2 - 100))
        text = font.render("You lost! Press spacebar to play again.", True, BLUE)
        screen.blit(text, (10, height / 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and game_over:
        game_over = False
        snake.x, snake.y = 600 / 2 - 7, 400 / 2 - 7
        points = 0
        snake_list = []
        direction = None
        random_x = random.randint(0, 585)
        random_y = random.randint(0, 385)
        for q in snake_list:
            while q == [random_x, random_y]:
                random_x = random.randint(0, 585)
                random_y = random.randint(0, 385)
        fruit = pygame.Rect(random_x, random_y, 14, 14)
    if keys[pygame.K_LEFT]:
        direction = "left"

    elif keys[pygame.K_RIGHT]:
        direction = "right"

    elif keys[pygame.K_UP]:
        direction = "up"

    elif keys[pygame.K_DOWN]:
        direction = "down"

    if direction == "left":
        snake.x -= vel

    elif direction == "right":
        snake.x += vel

    elif direction == "up":
        snake.y -= vel

    elif direction == "down":
        snake.y += vel
    pygame.display.flip()
    clock.tick(60)