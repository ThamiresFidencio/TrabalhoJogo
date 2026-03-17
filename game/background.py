

from game.entity import Entity
from game.Const import WIN_WIDTH


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):

        super().move()


        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH


