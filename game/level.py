import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from game import entityFactory
from game.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTIONS, EVENTY_ENEMY, SPAWW_TIME
from game.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(entityFactory.EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(entityFactory.EntityFactory.get_entity('Player1'))
        if game_mode in (MENU_OPTIONS[1], MENU_OPTIONS[2]):
            self.entity_list.append(entityFactory.EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENTY_ENEMY, SPAWW_TIME)

    def run(self):
        pygame.mixer.music.load(f'./assets/{self.name}.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENTY_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(entityFactory.EntityFactory.get_entity(choice))


            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',
                            text_color=COLOR_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=COLOR_WHITE,
                            text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=COLOR_WHITE,
                            text_pos=(10, WIN_HEIGHT - 20))
            pygame.display.flip()


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)



