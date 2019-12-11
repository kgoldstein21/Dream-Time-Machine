""" Interface for Dream Time Machine """
import pygame
import sys
import combVis

pygame.init()

# initilize display
size = (1600,1200)
win = pygame.display.set_mode(size)
pygame.display.set_caption("Dream Time Machine")
songs = "roxanne"
mode = "happy"

# sprite image for background
background = pygame.image.load("sprite_images/Background.jpg")
bg = pygame.transform.scale(background,(int(size[0]*1.0), int(size[1]*1.0)))
win.blit(bg, (0,0))

#interface title
title_font = pygame.font.Font('freesansbold.ttf', 96)
title_text = title_font.render("Dream Time Machine", True, (255,255,255))
win.blit(title_text, (350, 120))


pygame.display.update()


# class ButtonMode(pygame.sprite.Sprite):
#
#     def __init__(self, picture_file, button_text, x, y, a, b):
#         """initilization of button class and their attributes"""
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(picture_file)
#         self.image_resize = pygame.transform.scale(self.image,(int(size[0]*a), int(size[1]*b)))
#         self.font = pygame.font.Font('freesansbold.ttf',44)
#         self.text = self.font.render(button_text, True, (255,255,255))
#         self.rect = self.image_resize.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#
#
#
#
# class ButtonSong(pygame.sprite.Sprite):
#
#     def __init__(self,img_file,song_file):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(img_file)
#         self.name = song_file
#
#
#
#
# class ButtonStart(pygame.sprite.Sprite):
#
#     def __init__(self, pos, s_font_size, text):
#         """initilization of buttons and their attributes"""
#         pygame.sprite.Sprite.__init__(self)
#         self.rect = self.image.get_rect(topleft=pos)
#         self.font = pygame.font.Font('freesansbold.ttf',s_font_size)
#         self.text = self.font.render(button_text, True, (255,255,255))
#
#
# def nightmare():
#     """helper function to organize the buttons being called in the run loop """
#     nightmare = ButtonMode("sprite_images/bats.png","Nightmare", 100, 100, 0.15, 0.15)
#     win.blit(nightmare.text, (250, 590))
#     #win.blit(nightmare.image_resize,(240,650))
#     win.blit(nightmare.image, (240,650))
#     pygame.display.flip()
#     return nightmare
#
# def happy():
#     """helper function to organize the buttons being called in the run loop """
#     happy = ButtonMode("sprite_images/friends.png","Happy", 200, 200, 0.15, 0.15)
#     win.blit(happy.text, (590, 590))
#     win.blit(happy.image_resize,(540,650))
#     pygame.display.flip()
#
# def space():
#     """helper function to organize the buttons being called in the run loop """
#     space = ButtonMode("sprite_images/ufo.png","Space", 300, 300, 0.15, 0.15)
#     win.blit(space.text, (890, 590))
#     win.blit(space.image_resize,(840,650))
#     pygame.display.flip()
#
# def corporate():
#     """helper function to organize the buttons being called in the run loop """
#     corporate = ButtonMode("sprite_images/businessman.png","Corporate", 400, 400, 0.15, 0.15)
#     win.blit(corporate.text, (1160, 590))
#     win.blit(corporate.image_resize,(1150,650))
#     pygame.display.flip()


# title
b_font = pygame.font.Font('freesansbold.ttf', 52)
b_text = b_font.render("Songs", True, (255,220,60))
win.blit(b_text, (770, 270))

# title 2
b_font = pygame.font.Font('freesansbold.ttf', 52)
b_text = b_font.render("Modes", True, (255,220,60))
win.blit(b_text, (770, 700))

button_1 = pygame.Rect(500,800,100,100)
b1_font = pygame.font.Font('freesansbold.ttf', 24)
b1_text = b1_font.render("Nightmare", True, (255,255,255))
win.blit(b1_text, (495, 770))

button_2 = pygame.Rect(700,800,100,100)
b2_font = pygame.font.Font('freesansbold.ttf', 24)
b2_text = b2_font.render("Happy", True, (255,255,255))
win.blit(b2_text, (710, 770))
#
button_3 = pygame.Rect(900,800,100,100)
b3_font = pygame.font.Font('freesansbold.ttf', 24)
b3_text = b3_font.render("Space", True, (255,255,255))
win.blit(b3_text, (910, 770))
#
button_4 = pygame.Rect(1100,800,100,100)
b4_font = pygame.font.Font('freesansbold.ttf', 24)
b4_text = b4_font.render("Corporate", True, (255,255,255))
win.blit(b4_text, (1100, 770))
#
#
#
button_5 = pygame.Rect(500,390,100,50)
b5_font = pygame.font.Font('freesansbold.ttf', 24)
b5_text = b5_font.render("All Star", True, (255,255,255))
win.blit(b5_text, (500, 360))
#
button_6 = pygame.Rect(650,390,100,50)
b6_font = pygame.font.Font('freesansbold.ttf', 18)
b6_text = b6_font.render("Cotton Eye Joe", True, (255,255,255))
win.blit(b6_text, (640, 360))
#
button_7 = pygame.Rect(500,540,100,50)
b7_font = pygame.font.Font('freesansbold.ttf', 24)
b7_text = b7_font.render("Crazy", True, (255,255,255))
win.blit(b7_text, (500, 510))
#
button_8 = pygame.Rect(650,540,100,50)
b8_font = pygame.font.Font('freesansbold.ttf', 24)
b8_text = b8_font.render("Feel it Still", True, (255,255,255))
win.blit(b8_text, (640, 510))
#
button_9 = pygame.Rect(800,540,100,50)
b9_font = pygame.font.Font('freesansbold.ttf', 18)
b9_text = b9_font.render("Psycho Killer", True, (255,255,255))
win.blit(b9_text, (790, 510))
#
button_10 = pygame.Rect(950,540,100,50)
b10_font = pygame.font.Font('freesansbold.ttf', 24)
b10_text = b10_font.render("Roxxane", True, (255,255,255))
win.blit(b10_text, (950, 510))
#
button_11 = pygame.Rect(1100,540,100,50)
b11_font = pygame.font.Font('freesansbold.ttf', 18)
b11_text = b11_font.render("Sunday Best", True, (255,255,255))
win.blit(b11_text, (1090, 510))
#
button_12 = pygame.Rect(800,390,100,50)
b12_font = pygame.font.Font('freesansbold.ttf', 24)
b12_text = b12_font.render("Super", True, (255,255,255))
win.blit(b12_text, (800, 360))
#
button_13 = pygame.Rect(950,390,100,50)
b13_font = pygame.font.Font('freesansbold.ttf', 18)
b13_text = b13_font.render("Thank You, Next", True, (255,255,255))
win.blit(b13_text, (940, 360))
#
button_14 = pygame.Rect(1100,390,100,50)
b14_font = pygame.font.Font('freesansbold.ttf', 24)
b14_text = b14_font.render("Feels Like", True, (255,255,255))
win.blit(b14_text, (1100, 360))


# start
button_15 = pygame.Rect(785,1000,100,50)
b_15 = pygame.font.Font('freesansbold.ttf', 28)
b_15 = b_15.render("Start", True, (255,255,255))
win.blit(b_15, (800, 970))


def run_interface():
    """interface run loop"""
    running = True

    while running:

        # nightmare()
        # happy()
        # space()
        # corporate()


        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    # modes
                    if button_1.collidepoint(mouse_pos):
                        # print ('clicked button 1')

                        modes = "nightmare"
                    if button_2.collidepoint(mouse_pos):
                        # print ('clicked button 2')
                        modes = "happy"


                    if button_3.collidepoint(mouse_pos):
                        # print ('clicked button 3')
                        modes = "space"

                    if button_4.collidepoint(mouse_pos):
                        # print ('clicked button 4')
                        modes = "corporate"



                    # songs
                    if button_5.collidepoint(mouse_pos):
                        # print("5")
                        songs = "all_star"

                    if button_6.collidepoint(mouse_pos):
                        # print("6")
                        songs = "cotton_eye_joe"

                    if button_7.collidepoint(mouse_pos):
                        # print("7")
                        songs = "crazy"

                    if button_8.collidepoint(mouse_pos):
                        # print("8")
                        songs = "feel_it_still"

                    if button_9.collidepoint(mouse_pos):
                        # print("9")
                        songs = "psycho_killer"

                    if button_10.collidepoint(mouse_pos):
                        # print("10")
                        songs = "roxanne"

                    if button_11.collidepoint(mouse_pos):
                        # print("11")
                        songs = "sunday_best"

                    if button_12.collidepoint(mouse_pos):
                        # print("12")
                        songs = "super"

                    if button_13.collidepoint(mouse_pos):
                        # print("13")
                        songs = "thanku_next"

                    if button_14.collidepoint(mouse_pos):
                        # print("14")
                        songs = "feels_like"

                    # start button
                    if button_15.collidepoint(mouse_pos):
                        # print("15")
                        combVis.combinedVisual(combVis.cap, combVis.face_cascade, combVis.kernel, combVis.start_time, combVis.more_shapes, combVis.counter, combVis.corpcounter, combVis.dir, modes, songs)
                        pygame.quit()
                        quit()
# create start button using combvis line, and setting a variable for each button

        # modes
        pygame.draw.rect(win, [255,0,0], button_1)
        pygame.draw.rect(win, [255,0,255], button_2)
        pygame.draw.rect(win, [0,0,0], button_3)
        pygame.draw.rect(win, [0,0,255], button_4)

        # songs
        pygame.draw.rect(win, [255,255,255], button_5)
        pygame.draw.rect(win, [255,255,255], button_6)
        pygame.draw.rect(win, [255,255,255], button_7)
        pygame.draw.rect(win, [255,255,255], button_8)
        pygame.draw.rect(win, [255,255,255], button_9)
        pygame.draw.rect(win, [255,255,255], button_10)
        pygame.draw.rect(win, [255,255,255], button_11)
        pygame.draw.rect(win, [255,255,255], button_12)
        pygame.draw.rect(win, [255,255,255], button_13)
        pygame.draw.rect(win, [255,255,255], button_14)
        pygame.draw.rect(win, [255,255,255], button_15)
        pygame.display.update()



    pygame.quit()
    sys.exit


if __name__ == '__main__':
    run_interface()
