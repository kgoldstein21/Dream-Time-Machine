""" Interface for Dream Time Machine """
import pygame
pygame.init()

size = (1600,1200)
win = pygame.display.set_mode(size)
pygame.display.set_caption("Dream Time Machine")


# class test(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("sprite_images/Background.png")
#         self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
#         self.screen.blit(self.bigger_img, [100,100])

# class interface:
#     def __init__(self,window,xy):
#         """initilize class and class variables"""
#         self.window = win
#         self.xy = xy
#         self.color = {"white":(255,255,255),"black":(0,0,0), "blue":(0,0,255)}



#     def draw(self):
#         """initilizes interface display"""
#         background = pygame.image.load("sprite_images/Background.jpg")
#         bg = pygame.transform.scale(background,(int(size[0]*1.0), int(size[1]*1.0)))
#         win.blit(bg, (0,0))
#
#
#         #title
#         font = pygame.font.Font('freesansbold.ttf', 96)
#         text = font.render("Dream Time Machine", True, (255,255,255))
#
#         win.blit(text, (300,160))
#
#         # youtube link
#         yt_font = pygame.font.Font('freesansbold.ttf', 44)
#         yt_text = yt_font.render("Insert Youtube Link For Your Music!", True, (255,255,255))
#         win.blit(yt_text, (420,340))
#         button_out = pygame.Rect(400,400,800,60)
#         pygame.draw.rect(win, (255,255,255), button_out)
#
#
#
#         # button nightmare
#         nm_font = pygame.font.Font('freesansbold.ttf', 44)
#         nm_text = nm_font.render("Nightmare", True, (255,255,255))
#         win.blit(nm_text, (250, 590))
#
#         button_n_gif = pygame.image.load("sprite_images/bats.png")
#         b_n_gif = pygame.transform.scale(button_n_gif,(int(size[0]*0.15), int(size[1]*0.15)))
#         win.blit(b_n_gif, (240,650))
#
#
#         # button happy
#         hp_font = pygame.font.Font('freesansbold.ttf', 44)
#         hp_text = hp_font.render("Happy", True, (255,255,255))
#         win.blit(hp_text, (590, 590))
#
#         button_h_gif = pygame.image.load("sprite_images/friends.png")
#         b_h_gif = pygame.transform.scale(button_h_gif,(int(size[0]*0.15), int(size[1]*0.15)))
#         win.blit(b_h_gif, (540,650))
#
#
#         # button space
#         sp_font = pygame.font.Font('freesansbold.ttf', 44)
#         sp_text = sp_font.render("Space", True, (255,255,255))
#         win.blit(sp_text, (890, 590))
#
#         button_s_gif = pygame.image.load("sprite_images/ufo.png")
#         b_s_gif = pygame.transform.scale(button_s_gif,(int(size[0]*0.15), int(size[1]*0.15)))
#         win.blit(b_s_gif, (840,650))
#
#
#         # button boring
#         br_font = pygame.font.Font('freesansbold.ttf', 44)
#         br_text = br_font.render("Corporate", True, (255,255,255))
#         win.blit(br_text, (1160, 590))
#
# button_b_gif = pygame.image.load("sprite_images/businessman.png").convert()
# b_b_gif = pygame.transform.scale(button_b_gif,(int(size[0]*0.15), int(size[1]*0.15)))
# x = 1150
# y = 650
# win.blit(b_b_gif, (x,y))
#
#         # start button
# st_font = pygame.font.Font('freesansbold.ttf', 64)
# st_text = st_font.render("Start", True, (255,255,255))
# win.blit(st_text, (730, 900))
#
#
# pygame.display.update()
#
# # def script_loop():
#
# running = True
# while running:
#      for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#              runnning = False
#          if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = event.pos
#             if button_b_gif.get_rect().collidepoint(x, y):
#                 print('clicked on image')
#                 print(x, y)
# pygame.quit()

import pygame


pygame.init()
GRAY= pygame.Color('gray12')
BLUE = pygame.Color('dodgerblue1')
FONT = pygame.font.Font(None, 30)

BUTTON_UP_IMG = pygame.Surface((50, 30))
BUTTON_UP_IMG.fill(BLUE)
BUTTON_DOWN_IMG = pygame.Surface((50, 30))
BUTTON_DOWN_IMG.fill(pygame.Color('lightskyblue1'))

# The Button is a pygame sprite, that means we can add the
# instances to a sprite group and then update and render them
# by calling `sprite_group.update()` and `sprite_group.draw(screen)`.

class Button(pygame.sprite.Sprite):

    def __init__(self, pos, callback):
        pygame.sprite.Sprite.__init__(self)
        self.image = BUTTON_UP_IMG
        self.rect = self.image.get_rect(topleft=pos)
        self.callback = callback

    def handle_event(self, event):
        """Handle events that get passed from the event loop."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.image = BUTTON_DOWN_IMG
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.image = BUTTON_UP_IMG
                if self.rect.collidepoint(event.pos):
                    print('Button pressed.')
                    # Call the function that we passed during the
                    # instantiation. (In this case just `increase_x`.)
                    self.callback()


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.x = 0
        self.buttons = pygame.sprite.Group(
            Button((200, 200), callback=self.increase_x),
            Button((500, 200), callback=self.decrease_x))
        self.done = False

    # A callback function that we pass to the button instance.
    # It gets called if a collision in the handle_event method
    # is detected.
    def increase_x(self):
        """Increase self.x if button is pressed."""
        self.x += 1

    def decrease_x(self):
        """Decrease self.x if button is pressed."""
        self.x -= 1

    def run(self):
        while not self.done:
            self.handle_events()
            self.run_logic()
            self.draw()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            for button in self.buttons:
                button.handle_event(event)

    def run_logic(self):
        self.buttons.update()

    def draw(self):
        self.screen.fill(GRAY)
        self.buttons.draw(self.screen)
        txt = FONT.render(str(self.x), True, BLUE)
        self.screen.blit(txt, (360, 206))

        pygame.display.flip()


if __name__ == "__main__":
    Game().run()
    pygame.quit()
