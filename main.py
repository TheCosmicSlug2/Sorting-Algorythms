from random import shuffle
import pygame as pg
from renderer import Renderer
from settings import nb_values
from sorts.insertion_sort import InsertionSort
from sorts.fusion_sort import FusionSort
from sorts.cocktail_sort import CocktailSort
from sorts.bubble_sort import BubbleSort
from sorts.quicksort import QuickSort


def main():
    renderer = Renderer()
    SORTS = [
        FusionSort,
        InsertionSort, 
        QuickSort,
        CocktailSort, 
        BubbleSort
    ]


    for sort in SORTS:
        array = list(range(0, nb_values + 1))
        shuffle(array)
        if sort in (BubbleSort, InsertionSort, CocktailSort):
            renderer.fps = 0
        else:
            renderer.fps = 100
        sort(renderer, array).sort()
    
    pg.quit()


if __name__ == "__main__":
    main()
