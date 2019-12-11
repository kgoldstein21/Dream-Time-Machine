""" Interface for Dream Time Machine """
import pygame
import sys

pygame.init()

# initilize display
size = (1600,1200)
win = pygame.display.set_mode(size)
pygame.display.set_caption("Dream Time Machine")


# sprite image for background
background = pygame.image.load("sprite_images/Background.jpg")
bg = pygame.transform.scale(background,(int(size[0]*1.0), int(size[1]*1.0)))
win.blit(bg, (0,0))

#interface title
title_font = pygame.font.Font('freesansbold.ttf', 96)
title_text = title_font.render("Dream Time Machine", True, (255,255,255))
win.blit(title_text, (320, 120))


pygame.display.update()


class ButtonMode(pygame.sprite.Sprite):

    def __init__(self, picture_file, button_text, x, y, a, b):
        """initilization of button class and their attributes"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(picture_file)
        self.image_resize = pygame.transform.scale(self.image,(int(size[0]*a), int(size[1]*b)))
        self.font = pygame.font.Font('freesansbold.ttf',44)
        self.text = self.font.render(button_text, True, (255,255,255))
        self.rect = self.image_resize.get_rect()
        self.rect.x = x
        self.rect.y = y




class ButtonSong(pygame.sprite.Sprite):

    def __init__(self,img_file,song_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.name = song_file




class ButtonStart(pygame.sprite.Sprite):

    def __init__(self, pos, s_font_size, text):
        """initilization of buttons and their attributes"""
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect(topleft=pos)
        self.font = pygame.font.Font('freesansbold.ttf',s_font_size)
        self.text = self.font.render(button_text, True, (255,255,255))


def nightmare():
    """helper function to organize the buttons being called in the run loop """
    nightmare = ButtonMode("sprite_images/bats.png","Nightmare", 100, 100, 0.15, 0.15)
    win.blit(nightmare.text, (250, 590))
    #win.blit(nightmare.image_resize,(240,650))
    win.blit(nightmare.image, (240,650))
    pygame.display.flip()
    return nightmare

def happy():
    """helper function to organize the buttons being called in the run loop """
    happy = ButtonMode("sprite_images/friends.png","Happy", 200, 200, 0.15, 0.15)
    win.blit(happy.text, (590, 590))
    win.blit(happy.image_resize,(540,650))
    pygame.display.flip()

def space():
    """helper function to organize the buttons being called in the run loop """
    space = ButtonMode("sprite_images/ufo.png","Space", 300, 300, 0.15, 0.15)
    win.blit(space.text, (890, 590))
    win.blit(space.image_resize,(840,650))
    pygame.display.flip()

def corporate():
    """helper function to organize the buttons being called in the run loop """
    corporate = ButtonMode("sprite_images/businessman.png","Corporate", 400, 400, 0.15, 0.15)
    win.blit(corporate.text, (1160, 590))
    win.blit(corporate.image_resize,(1150,650))
    pygame.display.flip()

button_1 = pygame.Rect(400,400,100,100)

button_2 = pygame.Rect(600,400,100,100)

button_3 = pygame.Rect(800,400,100,100)

button_4 = pygame.Rect(1000,400,100,100)



def run_interface():
    """interface run loop"""
    running = True

    while running:

        nightmare()
        happy()
        space()
        corporate()


        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if button_1.collidepoint(mouse_pos):
                        print ('clicked button 1')


                    if button_2.collidepoint(mouse_pos):
                        print ('clicked button 2')


                    if button_3.collidepoint(mouse_pos):
                        print ('clicked button 3')


                    if button_4.collidepoint(mouse_pos):
                        print ('clicked button 4')


        pygame.draw.rect(win, [255,255,255], button_1)
        pygame.draw.rect(win, [255,255,255], button_2)
        pygame.draw.rect(win, [255,255,255], button_3)
        pygame.draw.rect(win, [255,255,255], button_4)

        pygame.display.update()



    pygame.quit()
    sys.exit


if __name__ == '__main__':
    run_interface()