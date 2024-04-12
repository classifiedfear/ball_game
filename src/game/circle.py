import pygame
from pygame.sprite import Sprite

class Circle(Sprite):
    def __init__(self,game, down_circle = False, hp_circle = False):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.Red = (250, 0, 0)
        if down_circle:
            self.image = pygame.Surface((80,80), pygame.SRCALPHA)
            pygame.draw.circle(self.image,self.Red,(40,40),40)
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.top + 40
        if hp_circle:
            self.image = pygame.Surface((40,40), pygame.SRCALPHA)
            pygame.draw.circle(self.image,self.Red,(20,20),20)
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.top + 40

        self.y = float (self.rect.y)
        self.x = float (self.rect.x)
        #   Второй вариант создания рект
        #self.rect = pygame.Rect(0,0, 80, 80)
        #self.rect.centerx = self.screen_rect.centerx 
        #self.rect.centery = self.screen_rect.top + 40
        #self.x = float(self.circle.rect.x)
        #self.y =float(self.circle.rect.y)

    def draw_circle(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.settings.circle_speed_y * self.settings.circle_direction_y
        self.x += self.settings.circle_speed_x * self.settings.circle_direction_x

        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges_top(self):
        if self.rect.top < self.screen_rect.top:
            return True


    def check_edges_goriz(self):
        if self.rect.right > self.screen_rect.right or self.rect.left < self.screen_rect.left:
            return True
        
    def check_edges_bottom(self):
       if self.rect.top >= self.screen_rect.bottom:
        return True 
            





    

