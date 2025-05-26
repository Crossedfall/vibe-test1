import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 10

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

class SnakeGame:
    def __init__(self):
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.food_pos = self.generate_food()

    def generate_food(self):
        while True:
            food_pos = [random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                        random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE]
            if food_pos not in self.snake_body:
                return food_pos

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'

            # Move the snake
            if self.direction == 'UP':
                self.snake_pos[1] -= BLOCK_SIZE
            elif self.direction == 'DOWN':
                self.snake_pos[1] += BLOCK_SIZE
            elif self.direction == 'LEFT':
                self.snake_pos[0] -= BLOCK_SIZE
            elif self.direction == 'RIGHT':
                self.snake_pos[0] += BLOCK_SIZE

            self.snake_body.insert(0, list(self.snake_pos))

            # Check if snake has eaten food
            snake_head_rect = pygame.Rect(self.snake_pos[0], self.snake_pos[1], BLOCK_SIZE, BLOCK_SIZE)
            food_rect = pygame.Rect(self.food_pos[0], self.food_pos[1], BLOCK_SIZE, BLOCK_SIZE)
            if snake_head_rect.colliderect(food_rect):
                self.food_pos = self.generate_food()
            else:
                self.snake_body.pop()

            # Check for collisions
            if (self.snake_pos[0] < 0 or self.snake_pos[0] >= WIDTH or
                self.snake_pos[1] < 0 or self.snake_pos[1] >= HEIGHT or
                self.snake_pos in self.snake_body[1:]):
                print("Game Over!")
                pygame.quit()
                sys.exit()

            # Draw everything
            screen.fill(BLACK)
            for pos in self.snake_body:
                pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
            text = font.render(f'Score: {len(self.snake_body) - 3}', True, WHITE)
            screen.blit(text, (10, 10))

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(FPS)

if __name__ == "__main__":
    game = SnakeGame()
    game.play()