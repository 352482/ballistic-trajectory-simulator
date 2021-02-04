import sys
import pygame
from Projectile import Projectile
import asyncio
import datetime
import argparse

parser = argparse.ArgumentParser(description="Simulate the trajectory of a ballistic projectile using PyGame.")
parser.add_argument("--scale", type=float, default=10.0)
parser.add_argument("--initial-velocity", nargs=2, type=float, default=(60.0,30.0))
parser.add_argument("--drag-coefficient", type=float, default=0.4)
parser.add_argument("--mass", type=float, default=10.0)
parser.add_argument("--radius", type=float, default=1.0)

args = parser.parse_args()
scale_factor=args.scale
initial_velocity=args.initial_velocity
drag_coefficient=args.drag_coefficient
mass=args.mass
radius=args.radius

pygame.display.init()

width=800
height=800

framerate=30 #frames/s
simulation_time_step=.01 #s

screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))
pygame.display.set_caption("Ballistic Trajectory Simulator")

projectile = Projectile(mass,radius,(initial_velocity[0],initial_velocity[1]*-1),(0,height/2),drag_coefficient)

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
    peak=None
    global simulating
    while True:
        pygame.event.pump()
        if projectile.position != last_position:
            screen.fill((0,0,0))
            trail.append((screen, (255,255,255), last_position, projectile.position))
            for line in trail:
                pygame.draw.aaline(*line)
            projectile.draw(screen,scale_factor)
            if last_position[1]>height-projectile.radius*scale_factor:
                simulating=False
            if projectile.position[1] > last_position[1] and peak == None:
                peak=last_position
            if peak != None:
                pygame.draw.circle(screen, (0,0,255), peak, 5)
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
