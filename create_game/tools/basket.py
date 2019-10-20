from pymunk import Body
import pymunk
import pygame as pg
import numpy as np
from .img_tool import ImageTool
from .fixed_box import FixedBox
from .basic_obj import BasicObj, LINE_THICKNESS
from .gravity_obj import MOVING_OBJ_COLLISION_TYPE

class Basket(FixedBox):
    def __init__(self, pos, size=10.0, color='black'):
        super().__init__(pos, size=size)
        self.pos = pos
        self.size = size


    def add_to_space(self, space):
        super().add_to_space(space)
        self.img = ImageTool('basket.png', 0.0,
                self.pos[:], int(self.size), int(self.size),
                debug_render=False,
                use_shape=self.shape)
        basket = self.img.get_shape()
        basket.sensor=True

    def render(self, screen, scale=None):
        if scale is None:
            scale = 1

        self.img.render(screen, scale, self.flipy)
