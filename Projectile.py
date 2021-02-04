import pygame
from math import pi
from math import copysign

class Projectile:
    def __init__(self,mass,radius,velocity,position,drag_coefficient):
        self.mass=mass #kg
        self.radius=radius #m
        self.velocity=velocity #m/s
        self.position=position #(m,m)
        self.drag_coefficient=drag_coefficient
        self.cross_section_area=(pi)*(self.radius**2)
    def set_velocity(self,velocity):
        self.velocity=velocity
    def set_mass(self,mass):
        self.mass=mass
    def set_radius(self,radius):
        self.radius=radius
        self.cross_section_area=(pi)*(self.radius**2)
    def set_drag_coefficient(self,drag_coefficient):
        self.drag_coefficient=drag_coefficient
    def step(self,time_step,air_density,scale_factor):
        x=self.position[0]
        y=self.position[1]
        force_x=0
        force_y=0
        force_x-=copysign(1,self.velocity[0])*(1/2)*(air_density)*(self.velocity[0]**2)*(self.drag_coefficient)*(self.cross_section_area)
        force_y-=copysign(1,self.velocity[1])*(1/2)*(air_density)*(self.velocity[1]**2)*(self.drag_coefficient)*(self.cross_section_area)
        force_y+=(9.81*self.mass)
        self.velocity=(self.velocity[0]+(force_x*time_step/self.mass),self.velocity[1]+(force_y*time_step/self.mass))
        self.position=(x+self.velocity[0]*time_step*scale_factor,
            y+self.velocity[1]*time_step*scale_factor)
    def draw(self,surface,scale_factor):
        pygame.draw.line(surface, (255,0,0), self.position, (self.position[0]+self.velocity[0]+self.radius*scale_factor,self.position[1]),3)
        pygame.draw.line(surface, (0,0,255), self.position, (self.position[0],self.position[1]+self.radius*scale_factor+self.velocity[1]),3)
        normal_velocity=((self.velocity[0]**2)+(self.velocity[1]**2))**0.5
        x_velocity_color=copysign(1,self.velocity[0])*int(255*self.velocity[0]/normal_velocity)
        y_velocity_color=copysign(1,self.velocity[1])*int(255*self.velocity[1]/normal_velocity)
        pygame.draw.circle(surface, (x_velocity_color,0,y_velocity_color), self.position, self.radius*scale_factor)
