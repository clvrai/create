from .fixed_obj import FixedObj
import pymunk
import pygame as pg
from .img_tool import ImageTool

class FixedBox(FixedObj):
    def __init__(self, pos, size=10.0, friction=1.0, elasticity = 0.4, color='slategray'):
        super().__init__(pos)
        mass = 1.0
        moment = pymunk.moment_for_box(mass, (size, size))
        self.body = self._create_body(mass, moment)
        self.body.position = pymunk.Vec2d(pos[0], pos[1])

        self.shape = pymunk.Poly.create_box(self.body, (size, size))
        self.shape.friction = friction
        self.shape.elasticity = elasticity
        self.color = color
        self.size = size

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def render(self, screen, scale=None):
        if scale is None:
            scale = 1

        draw_pos = scale * self.flipy(self.body.position)

        draw_size = scale * self.size
        draw_rect = (draw_pos[0] - (draw_size / 2),
            draw_pos[1] - (draw_size / 2),
            draw_size,
            draw_size)

        pg.draw.rect(screen, pg.Color(self.color), draw_rect)


class BouncyBox(FixedObj):
    def __init__(self, pos, size=10.0, friction=1.0, elasticity=1.2, color='slategray'):
        super().__init__(pos)
        self.friction = friction
        self.elasticity = elasticity
        self.color = color

        self.img = ImageTool('bouncy_square.png', angle=0, pos=pos[:],
            length=size, height=size, debug_render=False,
            use_box=True, elasticity=elasticity, friction=friction)

        self.shape = self.img.get_shape()


    def get_body(self):
        return self.shape.body

    def get_shape(self):
        return self.shape

    def render(self, screen, scale=None):
        if scale is None:
            scale = 1
        self.img.render(screen, scale, self.flipy)
