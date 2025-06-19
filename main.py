from random import shuffle
from sys import exit as sysexit
import pygame as pg
from settings import nb_values, screend, line_width

# Initialiser pg
pg.init()

# Configuration de la fenêtre
screen = pg.display.set_mode(screend)
pg.display.set_caption('Sorting algorythms')

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Boucle principale
clock = pg.time.Clock()

FPS = 0 # on se limite à 60 fps (max pour l'ordi)

frame = 0

ratio = (screend[1] - 200) / nb_values


def check_sorted(array):
    return all(a < b for a, b in zip(array, array[1:]))

def update(array, current):
    draw_lines(array, current)
    check_events()

tot_x = screend[0] - line_width * nb_values
startx = tot_x // 2
bottom_margin = 100

def draw_lines(array, current):
    screen.fill(BLACK)

    for idx, nb in enumerate(array):
        color = RED if idx == current else WHITE
        new_nb = nb * ratio
        x = startx + (idx * line_width)
        y = screend[1] - (bottom_margin + new_nb)
        rect = pg.Rect(x, y, line_width, new_nb)
        pg.draw.rect(screen, color, rect)

    pg.display.flip()

    clock.tick(FPS)


def bubble_sort(array):
    pg.display.set_caption("Bubble sort")
    array_sorted = False

    while not array_sorted:

        n = len(array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                update(array, j)
            array_sorted = check_sorted(array)

    update(array, i)

def coktail_sort(array):
    pg.display.set_caption("Cocktail Sort")
    array_sorted = False

    while not array_sorted:

        n = len(array)
        swapped = True
        start = 0
        end = n - 1
        while swapped == True:
            swapped = False

            for i in range(start, end):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True
                update(array, i)

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True
                update(array, i)

            start = start + 1


            array_sorted = check_sorted(array)

    update(array, start)


def insertion_sort(array):
    pg.display.set_caption("Insertion Sort")
    array_sorted = False

    while not array_sorted:

        for idx in range(1, len(array)):
            value = array[idx]
            value2 = idx - 1
            while value2 >= 0 and value < array[value2]:
                update(array, value2)
                array[value2 + 1] = array[value2]
                value2 -= 1
            array[value2 + 1] = value

            array_sorted = check_sorted(array)

    update(array, idx)

def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sysexit()


def run_with_profile():
    array = list(range(0, nb_values + 1))
    shuffle(array)
    insertion_sort(array.copy())

    shuffle(array)
    bubble_sort(array.copy())

    shuffle(array)
    coktail_sort(array.copy())


if __name__ == "__main__":
    # profiler = cProfile.Profile()
    # profiler.enable()

    run_with_profile()

    # profiler.disable()
    # profiler.dump_stats("profiling_results.prof")
    # print("Profil enregistré dans 'profiling_results.prof'.")


pg.quit()
