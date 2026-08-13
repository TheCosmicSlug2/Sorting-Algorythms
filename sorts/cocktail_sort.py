from renderer import Renderer
from utils import swap
from sorts.sort import Sort

class CocktailSort(Sort):
    def __init__(self, renderer: Renderer, array) -> None:
        super().__init__(renderer, array)

    def sort(self):
        self.renderer.captionize("Cocktail Sort")

        start = 0
        end = len(self.array) - 1

        while start < end:
            swapped = False

            # Gauche -> droite
            for i in range(start, end):
                if self.array[i] > self.array[i + 1]:
                    swap(self.array, i, i + 1)
                    swapped = True
                self.renderer.update_draw(self.array, i)

            if not swapped:
                break

            end -= 1
            swapped = False

            # Droite -> gauche
            for i in range(end - 1, start - 1, -1):
                if self.array[i] > self.array[i + 1]:
                    swap(self.array, i, i + 1)
                    swapped = True
                self.renderer.update_draw(self.array, i)

            if not swapped:
                break

            start += 1

        self.renderer.update_draw(self.array, i)