import pygame

class Projectile:
    def __init__(self,mass,radius,velocity,position):
        self.mass=mass #kg
        self.radius=radius #m
        self.velocity=velocity #m/s
        self.position=position #(m,m)
    def set_velocity(self,velocity):
        self.velocity=velocity
    def set_mass(self,mass):
        self.mass=mass
    def set_radius(self,radius):
        self.radius=radius
    def move(self,time_step):
        x=self.position[0]
        y=self.position[1]
        self.position=(x+self.velocity[0]*time_step,
            y+self.velocity[1]*time_step)
    def draw(self,surface):
        pygame.draw.circle(surface, (0,0,0), self.position, self.radius)
