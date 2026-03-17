import pygame

from game import entityFactory
from game.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(entityFactory.EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            for ent in self.entity_list:
                ent.move()
                self.window.blit(source=ent.surf, dest=ent.rect)

            pygame.display.flip()


