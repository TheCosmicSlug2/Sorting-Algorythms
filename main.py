from random import shuffle
import pygame as pg
import smartfust as sf

from renderer import Renderer
from settings import SCREEN_DIMS

from sorts.insertion_sort import InsertionSort
from sorts.fusion_sort import FusionSort
from sorts.cocktail_sort import CocktailSort
from sorts.bubble_sort import BubbleSort
from sorts.quicksort import QuickSort


SORTS = {
    "Bubble sort": BubbleSort,
    "Cocktail sort": CocktailSort,
    "Insertion sort": InsertionSort,
    "Fusion sort": FusionSort,
    "Quick sort": QuickSort,
}

SLOW_SORTS = {
    BubbleSort,
    CocktailSort,
    InsertionSort,
}

SORT_MENU_WIDGETS = {
    0: sf.Label(
        (220, 50), (350, 80),
        "Sorting Algorithms",
        sf.WHITE,
        text_height=40,
        colors=[sf.WHITE, sf.BLACK, sf.WHITE, sf.BLACK],
        borders=[3, 3, 3]
    ),

    1: sf.Label(
        (200, 180), (200, 30),
        "Number of values :",
        sf.WHITE,
        text_height=25,
        colors=[sf.TRANSPARENT]
    ),

    2: sf.Slider(
        (420, 180), (150, 30),
        _range=(50, 200),
        default_value=100,
        colors=[sf.WHITE, sf.BLACK],
        bar_text_fg=sf.WHITE
    ),

    3: sf.Label(
        (270, 230), (150, 30),
        "Algorithm :",
        sf.WHITE,
        text_height=25,
        colors=[sf.TRANSPARENT]
    ),

    4: sf.List(
        (420, 230), (180, 30),
        text_height=18,
        values=["All"] + list(SORTS.keys()),
        colors=[sf.WHITE, sf.BLACK],
        text_color=sf.WHITE

    ),

    5: sf.Button(
        (285, 430), (230, 60),
        text="Start",
        return_value="quit",
        textfg=sf.WHITE,
        text_height=20,
        colors=[
            sf.WHITE,
            sf.BLACK,
            sf.WHITE,
            (20, 20, 20)
        ],
        borders=[3, 3, 3],
        animation={"color": -6, "size": (3, 2)}
    ),
}


def execute_sorting(sorts, nb_values):
    renderer = Renderer(nb_values)

    for sort in sorts:
        array = list(range(nb_values))
        shuffle(array)

        renderer.fps = 0 if sort in SLOW_SORTS else 100
        sort(renderer, array).sort()


def menu():
    display = sf.Display(
        dims=SCREEN_DIMS,
        title="Sorting Algorithms",
        widgets=SORT_MENU_WIDGETS
    )
    display.set_bg_color(sf.BLACK)
    display.mainloop()

    if display.output_code == sf.GLOBAL_QUIT:
        return None

    values = display.widget_values()
    display.reset()
    del display

    nb_values = values[2]
    selected = values[4]

    sorts = list(SORTS.values()) if selected == "All" else [SORTS[selected]]

    return sorts, nb_values


def main():
    while True:
        result = menu()

        if result is None:
            break

        sorts, nb_values = result
        execute_sorting(sorts, nb_values)

    pg.quit()


if __name__ == "__main__":
    main()