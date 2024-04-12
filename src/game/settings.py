from random import randint, randrange
import pygame
class Settings():
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color =(232, 125, 231)
        self.fon_image =pygame.image.load("./images/2.png")
        self.fon_image_2 =pygame.image.load("./images/1.png")
        self.fon_image_3 = pygame.image.load("./images/3.jpg")
        self.fons = [self.fon_image,self.fon_image_3]
        

        self.circle_direction_x = 1
        self.circle_direction_y = 1

        self.circle_limit = 3
        
        self.points_scale = 1.3
        self.speed_scale = 1.1
        self.default_time()
        self.initialize_dynamic_settings()

    def default_time(self):
        self.time = 10


    def initialize_dynamic_settings(self):
        self.circle_speed_x = 5
        self.circle_speed_y = 5
        self.rect_speed = 5
        self.points_circle = 5
        self.level = 1


    def increase_speed(self):
        self.rect_speed *= self.speed_scale
        self.circle_speed_x *= self.speed_scale
        self.circle_speed_y *= self.speed_scale
        self.points_circle *= self.points_scale