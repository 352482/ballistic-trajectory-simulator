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

screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))
pygame.display.set_caption("Ballistic Trajectory Simulator")

initial_velocity=(30,100)

projectile = Projectile(1,10,(initial_velocity[0],initial_velocity[1]*-1),(0,height))

atmospheric_density = 1.225 #kg/m^3

async def simulation_loop():
    previous_time=datetime.datetime.now()
    while True:
        time_delta=datetime.datetime.now()-previous_time
        previous_time=datetime.datetime.now()
        projectile.step(time_delta.microseconds/1000000)
        await asyncio.sleep(simulation_time_step)

async def update_loop():
    last_position=(-1,-1)
    trail=[]
    while True:
        pygame.event.pump()
        if projectile.position != last_position:
            screen.fill((255,255,255))
            projectile.draw(screen)
            trail.append((screen, (0,0,0), last_position, projectile.position))
            for line in trail:
                pygame.draw.aaline(*line)
            last_position = projectile.position
        await asyncio.sleep(1/framerate)

async def draw_loop():
    while True:
        pygame.display.update()
        await asyncio.sleep(1/framerate)

asyncio.get_event_loop().create_task(simulation_loop())
asyncio.get_event_loop().create_task(update_loop())
asyncio.get_event_loop().create_task(draw_loop())
asyncio.get_event_loop().run_forever()
