from typing import List

from abc import ABC


class Transform():

    def __init__(self, x = 0, y = 0, width = 0, height = 0, scale_x = 1, scale_y = 1) -> None:
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale_x = scale_x
        self.scale_y = scale_y

    @property
    def center(self):

        x = self.x + (self.width / 2)
        y = self.y + (self.height / 2)

        return x, y

    def new_pos(self, x, y):

        self.x = x or self.x
        self.y = y or self.y

    def new_shape(self, width, height):

        self.width = width or self.width
        self.height = height or self.height

    def new_scale(self, sx, sy):

        self.scale_x = sx
        self.scale_y = sy
    
    def change_scale(self, sx, sy):

        self.scale_x = sx + self.scale_x
        self.scale_y = sy + self.scale_y

class AbstractGameObject():

    def __init__(self, transform: Transform, tag: List[str] = [], name: str = None) -> None:
        
        self.__transform__: Transform = transform or Transform()
        self.__tag__ = tag
        self.__name__ = name
    
    @property
    def transform(self):
        return self.__transform__

    @property
    def tag(self):
        return self.__tag__

    @property
    def name(self):
        return self.__name__