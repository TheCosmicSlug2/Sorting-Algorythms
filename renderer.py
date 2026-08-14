import pygame as pg
from settings import *

class Renderer:
    def __init__(self, nb_valeurs) -> None:
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_DIMS)
        pg.display.set_caption('Sorting algorythms')
        self.clock = pg.time.Clock()

        self.fps = FPS
        self.bar_width = (SCREEN_DIMS[0] - 200) / nb_valeurs
        self.ratio = (SCREEN_DIMS[1] - 200) / nb_valeurs

    def fill_screen(self, color):
        self.screen.fill(color)

    def draw_lines(self, array, current):
        self.fill_screen(BLACK)

        for idx, value in enumerate(array):
            color = RED if idx == current else WHITE

            hauteur = value * self.ratio
            x = 100 + idx * self.bar_width
            y = SCREEN_DIMS[1] - (bottom_margin + hauteur)

            rect = pg.Rect(x, y, self.bar_width, hauteur)
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
        
    