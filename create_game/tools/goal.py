from .fixed_obj import FixedObj
import pymunk
import pygame as pg
from pygame import gfxdraw
from .img_tool import ImageTool
from ..constants import goal_color

GOAL_RADIUS = 4.0

class GoalObj(FixedObj):
    def __init__(self, pos, color=goal_color, radius=GOAL_RADIUS):
        super().__init__(pos)
        mass = 1.0
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
        self.body = self._create_body(mass, inertia)
        self.body.position = self.pos
        self.shape = pymunk.Circle(self.body, radius, pymunk.Vec2d(0,0))
        self.radius = radius
        self.shape.sensor = True
        self.color = color

        # if color == 'cyan':
        #     img_file = 'gem.png'
        # else:
        #     img_file = 'yellow_gem.png'

        # self.img = ImageTool(img_file, angle=0, pos=pos[:],
        #     length=2 * radius, height=2 * radius, debug_render=False,
        #     use_shape=self.shape)

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def render(self, screen, scale=None):
        # self.img.render(screen, scale, self.flipy)
        if scale is None:
            scale = 1
        draw_radius = int(self.radius * scale)
        draw_pos = scale * self.flipy(self.body.position)
        draw_pos[0] = int(draw_pos[0])
        draw_pos[1] = int(draw_pos[1])

        # pg.draw.circle(screen, pg.Color(self.color), draw_pos, draw_radius)
        gfxdraw.filled_circle(screen, draw_pos[0], draw_pos[1], draw_radius, pg.Color(self.color))
        gfxdraw.aacircle(screen, draw_pos[0], draw_pos[1], draw_radius, pg.Color(self.color))
