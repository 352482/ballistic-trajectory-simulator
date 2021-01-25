import sys
import pygame
from Projectile import Projectile
import asyncio
import datetime

pygame.display.init()

width=800
height=800

framerate=40 #frames/s
simulation_time_step=.01 #s

scale_factor=10

screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))
pygame.display.set_caption("Ballistic Trajectory Simulator")

initial_velocity=(20,20)

projectile = Projectile(10,1,(initial_velocity[0],initial_velocity[1]*-1),(0,height/2),0.4)

atmospheric_density = 1.225 #kg/m^3

simulating=True

async def simulation_loop():
    previous_time=datetime.datetime.now()
    global simulating
    while simulating:
        projectile.step(simulation_time_step,atmospheric_density,scale_factor)
        await asyncio.sleep(simulation_time_step)

async def update_loop():
    last_position=(0,height/2)
    trail=[]
    global simulating
    while True:
        pygame.event.pump()
        if projectile.position != last_position:
            screen.fill((255,255,255))
            projectile.draw(screen,scale_factor)
            trail.append((screen, (0,0,0), last_position, projectile.position))
            for line in trail:
                pygame.draw.aaline(*line)
            last_position = projectile.position
            if last_position[1]>height:
                simulating=False
        await asyncio.sleep(1/framerate)

async def draw_loop():
    while True:
        pygame.display.update()
        await asyncio.sleep(1/framerate)

asyncio.get_event_loop().create_task(simulation_loop())
asyncio.get_event_loop().create_task(update_loop())
asyncio.get_event_loop().create_task(draw_loop())
asyncio.get_event_loop().run_forever()
