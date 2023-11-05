import pygame
from settings import *

class BATSMAN(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # start animation images
        batsman_start_1 = pygame.image.load('graphics/batsman/start-1.png').convert_alpha()
        batsman_start_2 = pygame.image.load('graphics/batsman/start-2.png').convert_alpha()
        batsman_start_3 = pygame.image.load('graphics/batsman/start-3.png').convert_alpha()
        batsman_start_4 = pygame.image.load('graphics/batsman/start-4.png').convert_alpha()

        # start animation images - transformed
        batsman_start_1 = pygame.transform.scale(batsman_start_1, (260,180))
        batsman_start_2 = pygame.transform.scale(batsman_start_2, (260,180))
        batsman_start_3 = pygame.transform.scale(batsman_start_3, (260,180))
        batsman_start_4 = pygame.transform.scale(batsman_start_4, (260,180))
        
        # start animation order
        self.batsman_start = [
            batsman_start_1, batsman_start_2, batsman_start_3, batsman_start_4]
        self.player_index = 0
		
        self.image = self.batsman_start[self.player_index]  
        self.rect = self.image.get_rect(midbottom=pitch_mid_point)

    def animation_state(self):
        self.player_index += 0.1
        if self.player_index >= len(self.batsman_start):self.player_index = 3
        self.image = self.batsman_start[int(self.player_index)]
    
    def update(self):
        self.animation_state()


class BOWLER(pygame.sprite.Sprite):
    def __init__(self, type):
        pass

    def update(self):
        pass


class BALL(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/cricket-ball-8pixels.png")
        self.rect = self.image.get_rect(midbottom=(375,380))
    
    def update(self):
        if self.rect.y >= 250:
            self.rect.y += -5
            self.rect.x += 0.5
        else:
            self.rect.y += -5
            self.rect.x -= 0.5

        if self.rect.y <= 175:
            self.kill()
