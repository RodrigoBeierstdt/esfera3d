import pygame
import math


WIDTH, HEIGHT = 800, 600
FPS = 60
CHARS = " .:-=+*#%@" 
SCALE = 250          
SPACING = 0.15     

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('monospace', 12, bold=True)
clock = pygame.time.Clock()

def rotate_x(x, y, z, angle):
    rad = math.radians(angle)
    ny = y * math.cos(rad) - z * math.sin(rad)
    nz = y * math.sin(rad) + z * math.cos(rad)
    return x, ny, nz

def rotate_y(x, y, z, angle):
    rad = math.radians(angle)
    nx = x * math.cos(rad) + z * math.sin(rad)
    nz = -x * math.sin(rad) + z * math.cos(rad)
    return nx, y, nz

angle_x = 0
angle_y = 0

running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0)) 
    mouse_rel = pygame.mouse.get_rel()
    if pygame.mouse.get_pressed()[0]: 
        angle_y += mouse_rel[0] * 0.5
        angle_x += mouse_rel[1] * 0.5
    
    lat = -math.pi/2
    while lat < math.pi/2:
        lat += SPACING
        lon = 0
        while lon < 2 * math.pi:
            lon += SPACING
            
            x = math.cos(lat) * math.cos(lon)
            y = math.cos(lat) * math.sin(lon)
            z = math.sin(lat)
            x, y, z = rotate_x(x, y, z, angle_x)
            x, y, z = rotate_y(x, y, z, angle_y)
            proj_x = int(x * SCALE + WIDTH / 2)
            proj_y = int(y * SCALE + HEIGHT / 2)
                
            char_surf = font.render("#", True, (255, 255, 255))
            screen.blit(char_surf, (proj_x, proj_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()