import pygame as pg
import numpy as np
import pymunk
import copy
from .img_loader import img_library
from .gravity_obj import GravityObj
from ..constants import asset_dir

class ImageTool(object):
    def __init__(self, image_loc, angle, pos, length, height, debug_render=False, use_circle=False,
        elasticity=None, friction=None, use_box=False, use_shape=None):

        image_loc = asset_dir + image_loc
        assert image_loc in img_library
        self.img = pg.image.fromstring(*img_library[image_loc]).convert()
        # self.img = pg.image.load(image_loc).convert()
        colorkey = self.img.get_at((0,0))
        self.img.set_colorkey(colorkey, pg.RLEACCEL)
        self.img.set_alpha(255)

        self.use_circle = use_circle
        self.use_box = use_box
        self.use_shape = use_shape
        self.debug_render = debug_render

        self.angle = angle
        self.orig_pos = pos[:]

        self.width = abs(length)
        self.height = height
        self.unscaled_img = self.img

        mass = 1.0
        if self.use_circle:
            inertia = pymunk.moment_for_circle(mass, 0, self.height/2, (0,0))
            circle_body = pymunk.Body(mass, inertia, pymunk.Body.STATIC)
            circle_body.position = self.orig_pos[:]

            self.img_shape = pymunk.Circle(circle_body, self.height/2 , pymunk.Vec2d(0,0))
        elif self.use_box:
            moment = pymunk.moment_for_box(mass, (length, length))
            box_body = pymunk.Body(mass, moment, pymunk.Body.STATIC)
            box_body.position = self.orig_pos[:]
            self.img_shape = pymunk.Poly.create_box(box_body, (length, length))
        elif self.use_shape is not None:
            self.img_shape = self.use_shape

        if elasticity is not None:
            self.img_shape.elasticity = elasticity

        if friction is not None:
            self.img_shape.friction = friction


    def get_shape(self):
        return self.img_shape


    def render(self, screen, scale, coord_convert):
        if scale is None:
            scale = 1

        if self.debug_render:
            if self.use_circle:
                draw_pos = scale * coord_convert(self.orig_pos)
                draw_pos[0] = int(draw_pos[0])
                draw_pos[1] = int(draw_pos[1])
                pg.draw.circle(screen, pg.Color('black'), draw_pos,
                    int(self.height/2 * scale))
            elif self.use_box:
                draw_pos = scale * coord_convert(self.orig_pos)
                draw_size = scale * self.width
                draw_rect = (draw_pos[0] - (draw_size / 2),
                    draw_pos[1] - (draw_size / 2),
                    draw_size,
                    draw_size)
                pg.draw.rect(screen, pg.Color('black'), draw_rect)
            elif self.use_shape is not None and isinstance(self.use_shape, pymunk.Poly):
                pointlist = []
                for v in self.use_shape.get_vertices():
                    x, y = v.rotated(self.use_shape.body.angle) + self.use_shape.body.position
                    point = scale * coord_convert([x, y])
                    pointlist.append([int(point[0]), int(point[1])])

                pg.draw.polygon(screen, pg.Color('black'), pointlist, 0)
            elif self.use_shape is not None and isinstance(self.use_shape, pymunk.Segment):
                p1 = scale * coord_convert(self.img_shape.a)
                p2 = scale * coord_convert(self.img_shape.b)

                pg.draw.lines(screen, pg.Color('black'), False, (p1,
                    p2), int(scale * self.height))
            elif self.use_shape is not None and isinstance(self.use_shape, pymunk.Circle):
                draw_pos = scale * coord_convert(self.orig_pos)
                draw_pos[0] = int(draw_pos[0])
                draw_pos[1] = int(draw_pos[1])
                pg.draw.circle(screen, pg.Color('black'), draw_pos,
                    int(self.height/2 * scale))

        if isinstance(self.img_shape, pymunk.Circle):
            img = pg.transform.rotate(self.unscaled_img, self.angle * (180.0 / np.pi))
            img = pg.transform.scale(img,
                [int(scale * self.width), int(scale * self.height)])
        elif self.img_shape.body.body_type != pymunk.Body.STATIC:
            img = pg.transform.scale(self.unscaled_img,
                [int(scale * self.width), int(scale * self.height)])
            img = pg.transform.rotate(img, self.img_shape.body.angle * (180.0 / np.pi))
        else:
            img = pg.transform.scale(self.unscaled_img,
                [int(scale * self.width), int(scale * self.height)])
            img = pg.transform.rotate(img, self.angle * (180.0 / np.pi))

        bb = self.img_shape.bb
        p1 = scale * coord_convert([bb.left, bb.top])
        draw_rect = (p1[0],
            p1[1],
            scale * (bb.right - bb.left),
            scale * (bb.top - bb.bottom))

        # pg.draw.rect(img, pg.Color('orange'), self.img.get_rect(), 1)
        # pg.draw.rect(screen, pg.Color('green'), draw_rect, 1)

        screen.blit(img, draw_rect)

