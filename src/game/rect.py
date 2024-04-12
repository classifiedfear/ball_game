import pygame
from pygame.sprite import Sprite

class Rectt(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = game.settings
        self.width = 200
        self.height = 20
        self.color = (0,0,0)
        self.rect = pygame.Rect(0,0, self.width,self.height)
        self.rect.center = self.screen_rect.centerx, self.screen_rect.centery + 100
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.rect,)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.rect_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.setting.rect_speed
        self.rect.x = self.x

    def rect_center(self):
        self.rect.center = self.screen_rect.centerx, self.screen_rect.centery + 100
        self.x = float(self.rect.x)