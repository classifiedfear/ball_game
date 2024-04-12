import pygame.font

class Button():
    def __init__(self,game, msg):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.text_color_black = (0, 0, 0)
        self.button_color_green =(0, 255, 0)
        self.width, self.height = 200, 50
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg (self, msg):
        self.msg_imag = self.font.render(msg, True, self.text_color_black, self.button_color_green)
        self.msg_imag_rect = self.msg_imag.get_rect()
        self.msg_imag_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color_green, self.rect)
        self.screen.blit(self.msg_imag, self.msg_imag_rect)
    
