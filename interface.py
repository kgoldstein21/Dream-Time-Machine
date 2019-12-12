""" Interface for Dream Time Machine

    run this script to play our Dream Time Machine program!

    This file generates the display and feeds variables to combVis.py to change
    the different possible songs + mode combinations for the dream time machine
    audio visualizer.
 """
import pygame
import sys
import combVis


"""initilize background and program title on  a display"""
pygame.init()
size = (1600,1200)
win = pygame.display.set_mode(size)
pygame.display.set_caption("Dream Time Machine")

# sets sprite image for background and resizes to fit display size
background = pygame.image.load("sprite_images/Background.jpg")
bg = pygame.transform.scale(background,(int(size[0]*1.0), int(size[1]*1.0)))
win.blit(bg, (0,0))

#sets interface title for background
title_font = pygame.font.Font('freesansbold.ttf', 96)
title_text = title_font.render("Dream Time Machine", True, (255,255,255))
win.blit(title_text, (350, 120))



"""sets large gold titles to designate sections for the songs and modes options """

# sets Songs as a title for the songs button section
b_font = pygame.font.Font('freesansbold.ttf', 52)
b_text = b_font.render("Songs", True, (255,220,60))
win.blit(b_text, (770, 270))

# sets Modes as a title for the modes button section
b_font = pygame.font.Font('freesansbold.ttf', 52)
b_text = b_font.render("Modes", True, (255,220,60))
win.blit(b_text, (760, 700))



"""initilize rectangles as buttons, drawing them, and then having a description text blitted above each button"""

""" initilize 'Modes' button section """
# sets nightmare mode button and description text
button_1 = pygame.Rect(500,800,100,100)
pygame.draw.rect(win, [169,169,169], button_1)
b1_font = pygame.font.Font('freesansbold.ttf', 24)
b1_text = b1_font.render("Nightmare", True, (255,255,255))
win.blit(b1_text, (492, 770))

# sets happy mode button and description text
button_2 = pygame.Rect(700,800,100,100)
pygame.draw.rect(win, [169,169,169], button_2)
b2_font = pygame.font.Font('freesansbold.ttf', 24)
b2_text = b2_font.render("Happy", True, (255,255,255))
win.blit(b2_text, (710, 770))

# sets space mode button and description text
button_3 = pygame.Rect(900,800,100,100)
pygame.draw.rect(win, [169,169,169], button_3)
b3_font = pygame.font.Font('freesansbold.ttf', 24)
b3_text = b3_font.render("Space", True, (255,255,255))
win.blit(b3_text, (910, 770))

# sets corporate mode button and description text
button_4 = pygame.Rect(1100,800,100,100)
pygame.draw.rect(win, [169,169,169], button_4)
b4_font = pygame.font.Font('freesansbold.ttf', 24)
b4_text = b4_font.render("Corporate", True, (255,255,255))
win.blit(b4_text, (1091, 770))


""" initilize 'Songs' button section """
# sets all star song button and description text
button_5 = pygame.Rect(500,390,100,50)
pygame.draw.rect(win, [169,169,169], button_5)
b5_font = pygame.font.Font('freesansbold.ttf', 18)
b5_text = b5_font.render("All Star", True, (255,255,255))
win.blit(b5_text, (518, 360))

# sets cotton eye joe song button and description text
button_6 = pygame.Rect(650,390,100,50)
pygame.draw.rect(win, [169,169,169], button_6)
b6_font = pygame.font.Font('freesansbold.ttf', 18)
b6_text = b6_font.render("Cotton Eye Joe", True, (255,255,255))
win.blit(b6_text, (635, 360))

# sets crazy song button and description text
button_7 = pygame.Rect(500,540,100,50)
pygame.draw.rect(win, [169,169,169], button_7)
b7_font = pygame.font.Font('freesansbold.ttf', 18)
b7_text = b7_font.render("Crazy", True, (255,255,255))
win.blit(b7_text, (525, 510))

# sets feel it stlil song button and description text
button_8 = pygame.Rect(650,540,100,50)
pygame.draw.rect(win, [169,169,169], button_8)
b8_font = pygame.font.Font('freesansbold.ttf', 18)
b8_text = b8_font.render("Feel It Still", True, (255,255,255))
win.blit(b8_text, (655, 510))

# sets psycho killer song button and description text
button_9 = pygame.Rect(800,540,100,50)
pygame.draw.rect(win, [169,169,169], button_9)
b9_font = pygame.font.Font('freesansbold.ttf', 18)
b9_text = b9_font.render("Psycho Killer", True, (255,255,255))
win.blit(b9_text, (790, 510))

# sets roxanne song button and description text
button_10 = pygame.Rect(950,540,100,50)
pygame.draw.rect(win, [169,169,169], button_10)
b10_font = pygame.font.Font('freesansbold.ttf', 18)
b10_text = b10_font.render("Roxanne", True, (255,255,255))
win.blit(b10_text, (965, 510))

# sets sunday best song button and description text
button_11 = pygame.Rect(1100,540,100,50)
pygame.draw.rect(win, [169,169,169], button_11)
b11_font = pygame.font.Font('freesansbold.ttf', 18)
b11_text = b11_font.render("Sunday Best", True, (255,255,255))
win.blit(b11_text, (1095, 510))

# sets super song button and description text
button_12 = pygame.Rect(800,390,100,50)
pygame.draw.rect(win, [169,169,169], button_12)
b12_font = pygame.font.Font('freesansbold.ttf', 18)
b12_text = b12_font.render("Super", True, (255,255,255))
win.blit(b12_text, (825, 360))

# sets thank u, next song button and description text
button_13 = pygame.Rect(950,390,100,50)
pygame.draw.rect(win, [169,169,169], button_13)
b13_font = pygame.font.Font('freesansbold.ttf', 18)
b13_text = b13_font.render("thank u, next", True, (255,255,255))
win.blit(b13_text, (940, 360))

# sets feels like song button and description text
button_14 = pygame.Rect(1100,390,100,50)
pygame.draw.rect(win, [169,169,169], button_14)
b14_font = pygame.font.Font('freesansbold.ttf', 18)
b14_text = b14_font.render("Feels Like", True, (255,255,255))
win.blit(b14_text, (1105, 360))


""" initilize 'start' button """
# sets start button and description text
button_15 = pygame.Rect(800,1030,100,50)
pygame.draw.rect(win, [255,255,255], button_15)
b_15 = pygame.font.Font('freesansbold.ttf', 44)
b_15 = b_15.render("Start", True, (255,220,60))
win.blit(b_15, (801, 980))

# updates display
pygame.display.update()


def run_interface():
    """interface run loop"""
    running = True
    while running:

        for event in pygame.event.get():
                """ make the program able to quit if you click on the top right quit icon"""
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                """recognition of button clicks
                input: user buttonclicks
                output: designates last song and mode combination choosen"""
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = event.pos


                    """ 'modes' section logic """
                    if button_1.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,0,0], button_1)
                        pygame.display.update()
                        modes = "nightmare"

                    if button_2.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,0,255], button_2)
                        pygame.display.update()
                        modes = "happy"

                    if button_3.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [0,0,0], button_3)
                        pygame.display.update()
                        modes = "space"

                    if button_4.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [0,0,255], button_4)
                        pygame.display.update()
                        modes = "corporate"



                     """ 'songs' section logic """
                    if button_5.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_5)
                        pygame.display.update()
                        songs = "all_star"

                    if button_6.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_6)
                        pygame.display.update()
                        songs = "cotton_eye_joe"

                    if button_7.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_7)
                        pygame.display.update()
                        songs = "crazy"

                    if button_8.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_8)
                        pygame.display.update()
                        songs = "feel_it_still"

                    if button_9.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_9)
                        pygame.display.update()
                        songs = "psycho_killer"

                    if button_10.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_10)
                        pygame.display.update()
                        songs = "roxanne"

                    if button_11.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_11)
                        pygame.display.update()
                        songs = "sunday_best"

                    if button_12.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_12)
                        pygame.display.update()
                        songs = "super"

                    if button_13.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_13)
                        pygame.display.update()
                        songs = "thanku_next"

                    if button_14.collidepoint(mouse_pos):
                        pygame.draw.rect(win, [255,255,255], button_14)
                        pygame.display.update()
                        songs = "feels_like"



                    """if the start button is pressed, pass in the currently selected song + mode and run combVis.py
                    then when you finish using the visualizer, quit out of the interface

                    input = mouse button click on button and the last song + mode button selected
                    output = running the audio visualizer program with the desired song + mode"""
                    if button_15.collidepoint(mouse_pos):
                        combVis.combinedVisual(combVis.cap, combVis.face_cascade, combVis.kernel, combVis.start_time, combVis.more_shapes, combVis.counter, combVis.corpcounter, combVis.dir, modes, songs)
                        pygame.quit()
                        quit()

# calls the run_interface function
if __name__ == '__main__':
    run_interface()
