import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BALL_COLOR = (255, 0, 0)
PADDLE_COLOR = (0, 0, 255)
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_SPEED = 2  # Reduced ball speed
PADDLE_SPEED = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Initialize variables
ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
ball_y = 0
ball_dy = BALL_SPEED
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - 2 * PADDLE_HEIGHT
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += PADDLE_SPEED

    # Update ball position
    ball_y += ball_dy

    # Check for collision with the paddle
    if (
        paddle_x - BALL_RADIUS < ball_x < paddle_x + PADDLE_WIDTH + BALL_RADIUS
        and paddle_y - BALL_RADIUS < ball_y < paddle_y + PADDLE_HEIGHT
    ):
        ball_dy *= -1
        score += 1

    # Check if the ball is out of bounds (reached the bottom)
    if ball_y > HEIGHT:
        ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        ball_y = 0

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball and paddle
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, int(ball_y)), BALL_RADIUS)
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Update the display
    pygame.display.update()

# Display final score
font = pygame.font.Font(None, 36)
text = font.render(f"Final Score: {score}", True, (0, 0, 0))
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.update()

# Wait for a few seconds before quitting
time.sleep(1)

# Quit Pygame
pygame.quit()
