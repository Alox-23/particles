import pygame
import particles.Particle
import random
import time
import light


class Source:

    def __init__(self, x=0, y=0):
        self.particles = []
        self.x = x
        self.y = y

    def emmit(self,
              life_span,
              particle,
              size=3,
              amount=1,
              dx=0,
              dy=0,
              gravity=0.1,
              light_type=light.lightCircle,
              light_color=(50, 50, 50),
              light_radius=5,
              light_mask=pygame.image.load("light/mask.png"),
              light_size=(10, 10),
              colorkey=(0, 0, 0)):
        for i in range(amount):
            self.particles.append(
                particle(self.x,
                         self.y,
                         life_span,
                         size,
                         dx,
                         dy,
                         gravity,
                         light_type=light_type,
                         light_radius=light_radius,
                         light_color=light_color,
                         light_mask=light_mask,
                         light_size=light_size,
                         colorkey=colorkey))

    def update(self, rand=0.2, change=0.1, rects=[], b=2, delta_time=1):
        for part_num, part in enumerate(self.particles):
            part.update(change, rand, rects, b, delta_time)
            if part.checkDeath():
                del self.particles[part_num]
            if part.size < 0:
                del self.particles[part_num]

    def setSource(self, x, y):
        self.x, self.y = x, y

    def draw_rand(self, screan):
        for particle in self.particles:
            particle.draw(screan, (random.randint(
                0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_light(self, screan, size_multiplier):
        for particle in self.particles:
            particle.draw_light(screan, size_multiplier)

    def draw(self, screan, color):
        for particle in self.particles:
            particle.draw(screan, color)

    def init_source_light(self, mask= pygame.image.load("light/mask.png"), light_size= (50, 50), colorkey= (0,0,0)):
        self.light = light.lightMask(mask = mask, size = light_size, colorkey = colorkey)

    def draw_source_light(self, screan, size_multiplier = 1):
        self.light.draw(screan, self.x, self.y, size_multiplier)
		
    def draw_rect(self, screan, color):
        for particle in self.particles:
            particle.draw_rect(screan, color)

    def print_length(self):
        print(len(self.particles))
