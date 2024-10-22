# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("media/tiny_ship.png").convert()
        self.rect = self.surf.get_rect(
            center = (
                random.randint(0, SCREEN_WIDTH // 4),
                random.randint(20, SCREEN_HEIGHT),
            )
        )

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("media/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("media/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

class Button:
    def __init__9

# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Artful Jet")

#initialize font
font = pygame.font.SysFont(None, 32)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
ADDSCORE = pygame.USEREVENT + 3
pygame.time.set_timer(ADDSCORE, 250)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("media/Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("media/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("media/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("media/Collision.ogg")

# Set the base volume for all sounds
move_up_sound.set_volume(0.5)
move_down_sound.set_volume(0.5)
collision_sound.set_volume(0.5)

# Variable to keep the main loop running
running = True

class Colors:
    WHITE = pygame.Color("white")
    RED = pygame.Color("red")
    GREEN = pygame.Color('green')
    BLUE = pygame.Color('blue')
    BLACK = pygame.Color('black')
    YELLOW = pygame.Color('yellow')
    CYAN = pygame.Color('cyan')
    MAGNETA = pygame.Color('magenta')
    DARK_ORANGE = pygame.Color('darkorange1')
    CRIMSON = pygame.Color('crimson')
    




player_score = 0


# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            # create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)   
         # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)     
        # Increment score
        elif event.type == ADDSCORE:
            player_score += 1    
            
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()
    clouds.update()

    # Fill the screen with black
    screen.fill((135, 206, 250))

    # Render the score
    score_text = font.render(f'Score: {player_score}', True, Colors.WHITE)
    # Display the score at the top-left corner
    screen.blit(score_text, (10, 10))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
    
        # Stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()

        running = False

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# All done! Stop and quit the mixer.
pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()