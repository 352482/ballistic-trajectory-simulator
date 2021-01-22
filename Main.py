import pygame
from Projectile import Projectile
import time
import threading
import sys

pygame.init()

simulation_time_step=0.01 #cycles/s
framerate=40 #frames/s

screen = pygame.display.set_mode((700,700))
screen.fill((255,255,255))
pygame.display.set_caption("Ballistic Trajectory Simulator")

projectile = Projectile(1,1,(1,1),(0,0))

atmospheric_density = 1.225 #kg/m^3

def simulation_loop():
    while True:
        projectile.move(simulation_time_step)
        time.sleep(simulation_time_step)

threading.Thread(target=simulation_loop).start()

last_position=(0,0)


while True:
    #TODO capture pygame events
    #draw projectile and trajectory
    if projectile.position != last_position:
        projectile.draw(screen)
        pygame.draw.line(screen, (0,0,0), last_position, projectile.position)
        last_position = projectile.position
    pygame.display.flip()
    time.sleep(1/framerate)
