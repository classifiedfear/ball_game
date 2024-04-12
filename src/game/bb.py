import sys
from pathlib import Path
import json

import pygame
from random import randint, choice
from time import sleep

from .settings import Settings
from .rect import Rectt
from .circle import Circle
from .gamestats import GameStats
from .button import Button
from .scoreboard import Scoreboard
from .sounds import Sounds

class BB():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('BB')
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.play_button = Button(self, "Play")
        self.rect = Rectt(self)
        self.circle = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.sounds = Sounds()
        self.path = Path("./record/record.json")
        if self.path.exists():
            self.load_record(path=self.path)
        self.timer_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.timer_event, 1000)
        self.bg_counter = randint (0, (len(self.settings.fons)-1))


    def _backgrounds(self):
        if self.settings.time <= 1:
            self.bg_counter = randint (0, len(self.settings.fons)-1)
            self._draw_bg(self.bg_counter)


    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.circle.update()
                self.rect.update()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_record(record=self.stats.high_score, path= self.path)
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                if event.type == pygame.KEYUP:
                    self._check_keyup_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                if self.sounds.STOPPED_PLAYING == event.type:
                    self.sounds.music_counter += 1
                    if self.sounds.music_counter >= len(self.sounds.musics):
                        self.sounds.music_counter = 0
                    pygame.mixer.music.queue(self.sounds.musics[self.sounds.music_counter])    
                if self.stats.game_active:
                    if event.type == self.timer_event:
                        self.settings.time -= 1
                        if self.settings.time <= 0:
                            self.sounds.victory()
                            self.start_level()
                    

    def start_level(self):
        self._backgrounds()
        sleep(0.5)
        self.settings.default_time()
        self.stats.lvl += 1
        self.circle.empty()
        self._create_ball()
        self.rect.rect_center()
        self.settings.increase_speed()
        


    def _check_play_button (self,mouse_pos):
        collision = self.play_button.rect.collidepoint(mouse_pos)
        if collision and not self.stats.game_active:
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()
            self.start_game()


    def _check_keydown_event(self,event):
        if event.key == pygame.K_ESCAPE:
            self.save_record(record=self.stats.high_score, path= self.path)
            sys.exit()
        if event.key == pygame.K_d:
            self.rect.moving_right = True
        if event.key == pygame.K_a:
            self.rect.moving_left = True


    def _check_keyup_event (self, event):
        if event.key == pygame.K_d:
            self.rect.moving_right = False
        if event.key == pygame.K_a:
            self.rect.moving_left = False


    def _update_screen(self):
        self._check_collisions()
        self._draw_bg(self.bg_counter)
        self.rect.draw_rect()
        self.sb.show_score()
        self.sb.prep_image()
        for circ in self.circle.sprites():
            circ.draw_circle()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.update()
    

    def _check_collisions(self):
        for circ in self.circle.sprites():
            collide = circ.rect.colliderect(self.rect)
            if collide:
                self.sounds.sound_cirlce_edge()
                self.stats.score += self.settings.points_circle
                self.settings.circle_direction_y *= -1
                
                self.sb.check_high_score()

            if circ.check_edges_top():
                self.sounds.sound_cirlce_edge()
                self.settings.circle_direction_y *= -1
                

            if circ.check_edges_goriz():
                self.sounds.sound_cirlce_edge()
                self.settings.circle_direction_x *= -1
                
            if circ.check_edges_bottom():
                self.circle_down()


    def circle_down(self):
        if self.stats.circle_left > 1:
            self.stats.circle_left -= 1
            self.sounds.lose()
            sleep(0.25)
            self.start_game()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        
    def _create_ball(self):
        new_circle = Circle(self, down_circle=True)
        self.circle.add(new_circle)


    def start_game(self):
        self.stats.game_active = True
        self.settings.default_time()
        self.circle.empty()
        self._create_ball()
        self.rect.rect_center()
        pygame.mouse.set_visible(False)


    def save_record(self, path, record):
        contents = json.dumps(record)
        path.write_text(contents)


    def load_record(self, path):
        contents = path.read_text()
        record = json.loads(contents)
        self.stats.high_score = record
        self.sb.prep_high_score()

    def _draw_bg (self, bg_counter):
        self.screen.blit(self.settings.fons[bg_counter], (0,0))

            
if __name__=="__main__":
    game = BB()
    game.run_game()
    