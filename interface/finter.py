import pygame

# class Button:
#
#     def __init__(self, xy):
#
#         self.colors = {"blue":(0,0,255), "yellow":(255,255,0), "white":(255,255,255), "black":(0,0,0)}
#         self.window = window
#         self.xy = xy
#         self.rect = pygame.Rect(xy)
#         self.image = pygame.image.load("filepath")

    # def draw(self):
    #     """Draws the display for the module and any visible interactions with the module"""
    #
    #     # module background rectangle


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()


def interface_loop():
    # # game loop
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             return False

    # game logic
    # screen background
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (0,0,0), (220,165,200,150))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()

        # base screen
    size = (800,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Dream Time Machine")
        # how fast screen refresh is
    clock = pygame.time.Clock()
    running = True
    while running:
        running = interface_loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return false
    pygame.quit()
