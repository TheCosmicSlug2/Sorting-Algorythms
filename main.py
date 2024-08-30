import random
import pygame
from sys import exit as sysexit

# Initialiser Pygame
pygame.init()

# Configuration de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sorting algorythms')

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Boucle principale

distance = 1

clock = pygame.time.Clock()

fps = 60 # on se limite à 60 fps (max pour l'ordi)

frame = 0
running = True






def check_sorted(array):
    for idx in range(len(array) - 1):
        if array[idx] >= array[idx + 1]:
            return False
    return True


def draw_line(x, width, height):

    pygame.draw.rect(screen, white, (x, 500-height, width, height)) # x, y, width, longueur



def draw_lines(array):
    screen.fill(black)


    len_array = len(array)

    # la width est à 800, mais on part pour 600 "d'utilisable" (100 inutilisables de chaque côté)

    line_width = 600/len_array # on peut pas vraiment arrondir, sinon décalages

    pygame.display.set_caption(f"{len_array} {line_width}")

    for idx in range(len(array)):
        x = 100 + (idx * line_width)
        line_height = array[idx]
        draw_line(x, line_width, line_height)



    pygame.display.update()

    clock.tick(90)




def bubble_sort(array):

    array_sorted = False

    while array_sorted == False:

        n = len(array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            draw_lines(array)
            array_sorted = check_sorted(array)

    draw_lines(array)
    return

def coktail_sort(array):

    array_sorted = False

    while array_sorted == False:

        n = len(array)
        swapped = True
        start = 0
        end = n - 1
        while (swapped == True):
            swapped = False

            for i in range(start, end):
                if (array[i] > array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            if (swapped == False):
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if (array[i] > array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            start = start + 1

            draw_lines(array)

            array_sorted = check_sorted(array)

    draw_lines(array)
    return

def insertion_sort(array):

    array_sorted = False

    while array_sorted == False:

        for idx in range(1, len(array)):
            value = array[idx]
            value2 = idx - 1
            while value2 >= 0 and value < array[value2]:
                array[value2 + 1] = array[value2]
                value2 -= 1
            array[value2 + 1] = value

            draw_lines(array)

            array_sorted = check_sorted(array)

    draw_lines(array)
    return

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sysexit()

    array = [_ for _ in range(400)]

    random.shuffle(array)
    insertion_sort(array)

    random.shuffle(array)
    bubble_sort(array)

    random.shuffle(array)
    coktail_sort(array)

    running = False

pygame.quit()



