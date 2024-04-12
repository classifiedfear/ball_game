import pygame.font
import pygame
from .circle import Circle
from pygame.sprite import Group


class Scoreboard ():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.stats = game.stats
        self.screen_rect = self.screen.get_rect()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_image()

    def prep_image(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_time()
        self.prep_circles()
        self.prep_lvl()


    def prep_lvl(self):
        str_lvl = str(self.stats.lvl)
        self.img_lvl = self.font.render(str_lvl, True, self.text_color, )
        self.img_lvl_rect = self.img_lvl.get_rect()
        self.img_lvl_rect.x = 20
        self.img_lvl_rect.y = self.screen_rect.bottom - 40
        

    def prep_circles(self):
        self.cirlces = Group()
        for circ_number in range(self.stats.circle_left):
            circ = Circle(self.game, hp_circle= True)
            circ.rect.x = 10 + circ_number * (1.5 * circ.rect.width)
            circ.rect.y = 10
            self.cirlces.add(circ)

    def prep_time(self):
        str_time = str(self.settings.time)
        self.img_time = self.font.render(str_time, True,self.text_color, )
        self.img_time_rect = self.img_time.get_rect()
        self.img_time_rect.centerx = self.screen_rect.centerx
        self.img_time_rect.top = 20

    def prep_score(self):
        rounded_score = round(self.stats.score)
        str_scrore = "{:,}".format(rounded_score)
        self.img_score = self.font.render(str_scrore, True, self.text_color, )
        self.img_score_rect = self.img_score.get_rect()
        self.img_score_rect.right = self.screen_rect.right - 20
        self.img_score_rect.top = 20


    def prep_high_score(self):
        rounded_score = round(self.stats.high_score, -1)
        str_score = "{:,}".format(rounded_score)
        self.img_high_score = self.font.render(str_score, True, self.text_color, )
        self.img_high_score_rect = self.img_high_score.get_rect()
        self.img_high_score_rect.centerx= self.screen_rect.centerx 
        self.img_high_score_rect.bottom = self.screen_rect.bottom - 20

    def show_score(self):
        self.screen.blit(self.img_score, self.img_score_rect)
        self.screen.blit (self.img_high_score, self.img_high_score_rect)
        self.screen.blit(self.img_time, self.img_time_rect)
        self.screen.blit(self.img_lvl, self.img_lvl_rect)
        self.cirlces.draw(self.screen)

    
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
