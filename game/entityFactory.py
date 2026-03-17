#!/usr/bin/python
# -*- coding: utf-8 -*-
from game.Const import WIN_WIDTH
from game.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        list_bg = []

        match entity_name:
            case "Level1Bg":
                for i in range(7):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))

        return list_bg
