import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from game.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.rect = None
        self.window = window
        self.surf = pygame.image.load("./assets/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load("assets/Menu.mp3")
        pygame.mixer_music.play(-1)

        while True:
            # Draw images / Desenhe as imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, (WIN_WIDTH / 2, 40))
            self.menu_text(50, "Shooter", COLOR_ORANGE, (WIN_WIDTH / 2, 80))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTIONS[i], COLOR_YELLOW, (WIN_WIDTH // 2, 160 + 35 * i))
                else:
                    self.menu_text(20, MENU_OPTIONS[i], COLOR_WHITE, (WIN_WIDTH // 2, 160 + 35 * i))

            pygame.display.flip()

            # Check for all events / Confira todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1

                    if event.key == pygame.K_RETURN:  # Enter
                        return MENU_OPTIONS[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)