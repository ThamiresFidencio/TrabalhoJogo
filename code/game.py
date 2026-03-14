import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 400))

    def run(self):

        while True:
            menu = menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
               # if event.type == pygame.QUIT:
                   # pygame.quit() #Close Window
                   # quit() #End Pygame