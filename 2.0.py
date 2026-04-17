import pygame
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

my_font = pygame.font.SysFont("Arial", 28, bold=1)

# Kart 
kart_img = pygame.Surface((40, 20), pygame.SRCALPHA)
pygame.draw.rect(kart_img, (255, 0, 0), (0, 0, 40, 20)) # Red Kart

x, y = 400, 100
angle = 0
speed = 0
max_speed = 5
acceleration = 0.1
friction = 0.05
steering = 4
running = True
while running:
    screen.fill((50, 150, 50)) # Grass background
    pygame.draw.ellipse(screen,(100, 100, 100), (50, 50, 700, 500))
    pygame.draw.ellipse(screen, (50, 150, 50), [150, 150, 500, 300])
    pygame.draw.rect(screen, (255, 255, 255), [380, 50, 40, 100])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input Handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        speed = min(speed + acceleration, max_speed)
    elif keys[pygame.K_s]:
        speed = max(speed - acceleration, -max_speed/2)
    else:
        # Apply friction
        if speed > 0: speed -= friction
        if speed < 0: speed += friction

    if keys[pygame.K_a] and abs(speed) > 0.1:
        angle += steering
        speed *=0.97
    if keys[pygame.K_d] and abs(speed) > 0.1:
        angle -= steering
        speed *=0.97
    if keys[pygame.K_x]:
        running = False


    # Physics: Calculate new position
    # Use Trigonometry to move in the direction the kart is facing
    radians = math.radians(angle)
    x += speed * math.cos(radians)
    y -= speed * math.sin(radians) # Subtract because Pygame Y increases downwards

    # Rendering
    rotated_kart = pygame.transform.rotate(kart_img, angle)
    new_rect = rotated_kart.get_rect(center=(x, y))
    screen.blit(rotated_kart, new_rect.topleft)
    display_speed = speed
    pygame.display.flip()
    clock.tick(60)
    # Inside your main loop:
    try:
        # Check the color of the pixel at the kart's position
        current_color = screen.get_at((int(x), int(y)))
        print(str(current_color))
    
    # If the color is Green (Grass), slow the kart down significantly
        if str((50, 150, 50)) in str(current_color): # Match your grass color
            max_speed = 1.5  # Penalize for off-roading
        else:
            max_speed = 5.0  # Full speed on the track
    except IndexError:
        # If the kart goes off the screen, reset it
        x, y = 400, 100
        speed = 0

        #speedmeter
    display_speed = int(round(((abs(speed))*20), 2)) #  go to powershell terminal then run py 2.0.py
    speed_text = my_font.render(f"{display_speed} KPH", True, (255, 255, 0))# wait i will run
    
    screen.blit(speed_text, (10, 50))
    pygame.display.flip() #click run na bro

    clock.tick(60)

pygame.quit()
