import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1700
screen_height = 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zombie Shooter Game")
bg_color = (0, 0, 0)  # Black background

# Load the image
image_path = "C:/Users/luis.pereira/Desktop/gif.gif"
shooter_image = pygame.image.load(image_path)
shooter_image = pygame.transform.rotate(shooter_image, 0)  # Initial rotation

# Create the shooter
shooter_rect = shooter_image.get_rect(center=(screen_width // 2, screen_height // 2))
shooter_angle = 0  # Initial angle for rotation
shooter_speed = 5  # Movement speed

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Define the movement and rotation functions
def move_forward():
    global shooter_rect
    dx = shooter_speed * math.cos(math.radians(shooter_angle))
    dy = shooter_speed * math.sin(math.radians(shooter_angle))
    shooter_rect.x += dx
    shooter_rect.y -= dy

def move_backward():
    global shooter_rect
    dx = shooter_speed * math.cos(math.radians(shooter_angle))
    dy = shooter_speed * math.sin(math.radians(shooter_angle))
    shooter_rect.x -= dx
    shooter_rect.y += dy

def rotate_left():
    global shooter_angle
    shooter_angle += 10

def rotate_right():
    global shooter_angle
    shooter_angle -= 10

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move_forward()
    if keys[pygame.K_DOWN]:
        move_backward()
    if keys[pygame.K_LEFT]:
        rotate_left()
    if keys[pygame.K_RIGHT]:
        rotate_right()

    # Clear the screen
    screen.fill(bg_color)

    # Rotate the image
    rotated_image = pygame.transform.rotate(shooter_image, shooter_angle)
    rotated_rect = rotated_image.get_rect(center=shooter_rect.center)

    # Draw the shooter
    screen.blit(rotated_image, rotated_rect.topleft)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
p