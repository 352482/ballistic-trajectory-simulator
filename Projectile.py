class Projectile:
    def __init__(self,mass,cross_section_area,velocity,position):
        self.mass=mass
        self.surface_area=cross_section_area
        self.velocity=velocity
        self.position=position
    def set_velocity(self,velocity):
        self.velocity=velocity
    def move(self,time_step):
        x=self.position[0]
        y=self.position[1]
        self.position=(x*time_step,y*time_step)
