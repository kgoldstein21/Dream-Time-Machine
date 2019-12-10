""" Interface for Dream Time Machine """
import pygame
pygame.init()

size = (1600,1200)
# size = (800,600)
win = pygame.display.set_mode(size)
pygame.display.set_caption("Dream Time Machine Interface")


# class test(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("sprite_images/Background.png")
#         self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
#         self.screen.blit(self.bigger_img, [100,100])

class interface:
    def __init__(self,window,xy):
        """initilize class and class variables"""
        self.window = win
        self.xy = xy






background = pygame.image.load("sprite_images/Background.jpg")
bg = pygame.transform.scale(background,(int(size[0]*1.0), int(size[1]*1.0)))

win.blit(bg, (0,0))



#title
font = pygame.font.Font('freesansbold.ttf', 96)
text = font.render("Dream Time Machine", True, (255,255,255))
# textRect = text.get_rect()
win.blit(text, (300,160))

# youtube link
yt_font = pygame.font.Font('freesansbold.ttf', 44)
yt_text = yt_font.render("Insert Youtube Link For Your Music!", True, (255,255,255))
win.blit(yt_text, (420,340))
button_out = pygame.Rect(400,400,800,60)
pygame.draw.rect(win, (255,255,255), button_out)

#
# bt_font = pygame.font.Font('freesansbold.ttf', 22)
# bt_text = bt_font.render("Choose Which Background Mode", True, (255,255,255))
# win.blit(bt_text, (360, 450))


# button nightmare
nm_font = pygame.font.Font('freesansbold.ttf', 44)
nm_text = nm_font.render("Nightmare", True, (255,255,255))
win.blit(nm_text, (250, 590))
# button_nightmare = pygame.Rect(120,325,120,70)
# pygame.draw.rect(win, (255,255,255), button_nightmare)
button_n_gif = pygame.image.load("sprite_images/bats.png")
b_n_gif = pygame.transform.scale(button_n_gif,(int(size[0]*0.15), int(size[1]*0.15)))
win.blit(b_n_gif, (240,650))


# button happy
hp_font = pygame.font.Font('freesansbold.ttf', 44)
hp_text = hp_font.render("Happy", True, (255,255,255))
win.blit(hp_text, (590, 590))
# button_happy = pygame.Rect(270,325,120,70)
# pygame.draw.rect(win, (255,255,255), button_happy)
button_h_gif = pygame.image.load("sprite_images/friends.png")
b_h_gif = pygame.transform.scale(button_h_gif,(int(size[0]*0.15), int(size[1]*0.15)))
win.blit(b_h_gif, (540,650))


# button space
sp_font = pygame.font.Font('freesansbold.ttf', 44)
sp_text = sp_font.render("Space", True, (255,255,255))
win.blit(sp_text, (890, 590))
# button_space = pygame.Rect(420,325,120,70)
# pygame.draw.rect(win, (255,255,255), button_space)
button_s_gif = pygame.image.load("sprite_images/ufo.png")
b_s_gif = pygame.transform.scale(button_s_gif,(int(size[0]*0.15), int(size[1]*0.15)))
win.blit(b_s_gif, (840,650))


# button boring
br_font = pygame.font.Font('freesansbold.ttf', 44)
br_text = br_font.render("Corporate", True, (255,255,255))
win.blit(br_text, (1160, 590))
# button_boring = pygame.Rect(570,325,120,70)
# pygame.draw.rect(win, (255,255,255), button_boring)
button_b_gif = pygame.image.load("sprite_images/businessman.png")
b_b_gif = pygame.transform.scale(button_b_gif,(int(size[0]*0.15), int(size[1]*0.15)))
win.blit(b_b_gif, (1150,650))

# start button
st_font = pygame.font.Font('freesansbold.ttf', 64)
st_text = st_font.render("Start", True, (255,255,255))
win.blit(st_text, (730, 900))
# button_start = pygame.Rect(100,450,100,30)
# pygame.draw.rect(win, (255,255,255), button_start)

pygame.display.update()


running = True
while running:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             runnning = False
pygame.quit()
