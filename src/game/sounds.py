import pygame
from random import randint
class Sounds:
    def __init__(self):
        self.musics = ["sounds\\main.wav","sounds\\main2.wav", "sounds\\main3.wav"]
        self.music_counter = randint(0, (len(self.musics)-1))
        self.STOPPED_PLAYING = pygame.USEREVENT + 1
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        pygame.mixer.music.set_endevent(self.STOPPED_PLAYING)
        pygame.mixer.music.load(self.musics[self.music_counter])
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.3)

        

    def sound_cirlce_edge(self):
        pygame.mixer.Sound("./sounds/zvuk-udara-v-igre.wav").play()

    def victory(self):
        pygame.mixer.Sound("./sounds/zvuk-pobedyi-v-igrovom-urovne-30120.wav").play()


    def lose(self):
        sound =  pygame.mixer.Sound("./sounds/4e9c206b994181f (online-audio-converter.com).wav").play()
        sound.set_volume(0.4)

    


