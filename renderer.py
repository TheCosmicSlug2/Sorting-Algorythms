import pygame as pg
from settings import *

class Renderer:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(screend)
        pg.display.set_caption('Sorting algorythms')
        self.clock = pg.time.Clock()

        self.fps = FPS
        self.ratio = (screend[1] - 200) / nb_values

    def fill_screen(self, color):
        self.screen.fill(color)

    def draw_lines(self, array, current):
        self.fill_screen(BLACK)

        for idx, nb in enumerate(array):
            color = RED if idx == current else WHITE
            new_nb = nb * self.ratio
            x = startx + (idx * line_width)
            y = screend[1] - (bottom_margin + new_nb)
            rect = pg.Rect(x, y, line_width, new_nb)
            pg.draw.rect(self.screen, color, rect)

        pg.display.flip()

    def captionize(self, title):
        pg.display.set_caption(title)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

    def update(self):
        pg.display.flip()
        self.clock.tick(self.fps)

    def update_draw(self, array, current):
        self.check_events()
        self.draw_lines(array, current)
        self.update()
        
    