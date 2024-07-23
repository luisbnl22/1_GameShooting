import pygame
import math


class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10  # Speed of the bullet
        self.radius = 5  # Radius of the bullet
        self.color = (255, 0, 0)  # Color of the bullet (red)

    def update(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class ZombieShooterGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the screen
        self.screen_width = 1700
        self.screen_height = 1200
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Zombie Shooter Game")
        self.bg_color = (0, 0, 0)  # Black background

        # Load the image
        self.image_path = "C:/Users/luis.pereira/Desktop/1_GameShooting/gif.gif"
        self.shooter_image = pygame.image.load(self.image_path)
        self.shooter_image = pygame.transform.rotate(self.shooter_image, 0)  # Initial rotation

        # Create the shooter
        self.shooter_rect = self.shooter_image.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.shooter_angle = 0  # Initial angle for rotation
        self.shooter_speed = 5  # Movement speed

        # List to store bullets
        self.bullets = []

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        self.running = True

    def move_forward(self):
        dx = self.shooter_speed * math.cos(math.radians(self.shooter_angle))
        dy = self.shooter_speed * math.sin(math.radians(self.shooter_angle))
        self.shooter_rect.x += dx
        self.shooter_rect.y -= dy

    def move_backward(self):
        dx = self.shooter_speed * math.cos(math.radians(self.shooter_angle))
        dy = self.shooter_speed * math.sin(math.radians(self.shooter_angle))
        self.shooter_rect.x -= dx
        self.shooter_rect.y += dy

    def rotate_left(self):
        self.shooter_angle += 2

    def rotate_right(self):
        self.shooter_angle -= 2

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Create a new bullet
                    bullet = Bullet(self.shooter_rect.centerx, self.shooter_rect.centery, self.shooter_angle)
                    self.bullets.append(bullet)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_forward()
        if keys[pygame.K_DOWN]:
            self.move_backward()
        if keys[pygame.K_LEFT]:
            self.rotate_left()
        if keys[pygame.K_RIGHT]:
            self.rotate_right()

        # Update bullets
        for bullet in self.bullets:
            bullet.update()

        # Remove off-screen bullets
        self.bullets = [bullet for bullet in self.bullets if 0 <= bullet.x <= self.screen_width and 0 <= bullet.y <= self.screen_height]

    def draw(self):
        # Clear the screen
        self.screen.fill(self.bg_color)

        # Rotate the image
        rotated_image = pygame.transform.rotate(self.shooter_image, self.shooter_angle)
        rotated_rect = rotated_image.get_rect(center=self.shooter_rect.center)

        # Draw the shooter
        self.screen.blit(rotated_image, rotated_rect.topleft)

        # Draw bullets
        for bullet in self.bullets:
            bullet.draw(self.screen)

        # Update the display
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = ZombieShooterGame()
    game.run()
