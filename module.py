import pygame
from settings import *


target_runs = 200
current_runs = "100/2"
current_overs = "5.1"

# scoreboard

class SCOREBOARD():
    def display_score(self,target):
        scoreboard = pygame.Rect(0,screen_height-scoreboard_height,screen_width,scoreboard_height)
        pygame.draw.rect(target,"#343434",scoreboard)
        
        # rectangles
        rect = pygame.Rect(10,screen_height-scoreboard_height+5,50,scoreboard_height-5)
        pygame.draw.rect(target,"#ff8c00",rect)
        rect = pygame.Rect(100,screen_height-scoreboard_height+5,120,scoreboard_height-5)
        pygame.draw.rect(target,"#B22222",rect)
        rect = pygame.Rect(260,screen_height-scoreboard_height+5,40,scoreboard_height-5)
        pygame.draw.rect(target,"#ff8c00",rect)
        for i in range(6):
            rect = pygame.Rect(600+i*32,screen_height-scoreboard_height+5,30,scoreboard_height-5)
            pygame.draw.rect(target,"#ff8c00",rect)

        rect = pygame.Rect(screen_width-220,10,120,30)
        pygame.draw.rect(target,"#343434",rect)

        # text 
        TEXT().blit("AUS",target,(35,screen_height-15),16,color=(255,255,255))
        TEXT().blit("VS",target,(80,screen_height-15),16,color=(255,255,255))
        TEXT().blit(f"IND {current_runs}",target,(160,screen_height-15),16,color=(255,255,255))
        TEXT().blit(current_overs,target,(240,screen_height-15),16,color=(255,255,255))
        TEXT().blit("10",target,(280,screen_height-15),16,color=(255,255,255))
        TEXT().blit(f"TARGET : {target_runs}",target,(screen_width-160,25),16,color=(255,255,255))


    def update(self):
        pass



# objects

class TEXT():
    ds = 0
    sign = 1
    def blit(self,text,target,pos,size=20,font="Aller",bold=False,color=(0,0,0),bounce=False):
        if bounce:
            if TEXT.ds >= 2.75: TEXT.sign = -1
            elif TEXT.ds == 0: TEXT.sign = 1
            TEXT.ds += TEXT.sign*0.125
        if bold:
            font = pygame.font.Font(f"fonts/{font}-Bold.ttf",(size+int(TEXT.ds)))
        else:
            font = pygame.font.Font(f"fonts/{font}-Regular.ttf",(size+int(TEXT.ds)))
        txt = font.render(text,False,color)
        txt_rect = txt.get_rect(center = pos)
        target.blit(txt,txt_rect)


class PROGRESS_BAR():
    ds = 0
    loading = True
    def load(self,target,pos,size):
        if PROGRESS_BAR.loading:
            rect1 = pygame.Rect(pos[0],pos[1],size[0],size[1])
            pygame.draw.rect(target,"Black",rect1)
            rect2 = pygame.Rect(pos[0],pos[1],int(PROGRESS_BAR.ds),size[1])
            PROGRESS_BAR.ds += 1.5
            pygame.draw.rect(target,"Orange",rect2)
        if PROGRESS_BAR.ds >= size[0]:
            PROGRESS_BAR.loading = False



# functions

def blit_alpha(target, source, location, opacity):
    """ 
        It is used for adjusting the opacity of the surfaces
    """
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)


def get_frames(player,action,scale=None):
    """
        Importing all the frames from the folders in a dictionary
    """
    frames, c = {}, 0
    while True:
        try:
            file = f'graphics/{player}/{action}/frame-{c+1}.png'
            frame = pygame.image.load(file).convert_alpha()
            if scale != None:
                frame = pygame.transform.scale(frame, scale)
            frames[c] = frame
            c+=1
        except: break
    return frames

def display_runs(runs,target):
    """
        Display the runs scored on that ball
    """
    rect1 = pygame.Rect(screen_width/2-100,screen_height/2-125,200,250)
    pygame.draw.rect(target,"#343434",rect1)
    rect2 = pygame.Rect(screen_width/2-100,screen_height/2-90,200,180)
    pygame.draw.rect(target,"#B22222",rect2)

    match runs:
        case 6: txt = "SIX"
        case 4: txt = "FOUR"
        case 3: txt = "TRIPLE"
        case 2: txt = "DOUBLE"
        case 1: txt = "SINGLE"

    if runs != 0:
        TEXT().blit(str(runs),target,(screen_width/2,screen_height/2-20),132)
        TEXT().blit(txt,target,(screen_width/2,screen_height/2+60),50,"Action_Man")
    else:
        TEXT().blit("DOT",target,(screen_width/2,screen_height/2-30),50,"Action_Man")
        TEXT().blit("BALL",target,(screen_width/2,screen_height/2+30),50,"Action_Man")