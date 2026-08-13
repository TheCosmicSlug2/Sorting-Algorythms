
from renderer import Renderer
from utils import swap
from sorts.sort import Sort

class BubbleSort(Sort):
    def __init__(self, renderer: Renderer, array) -> None:
        super().__init__(renderer, array)


    def sort(self):
        
        self.renderer.captionize("Bubble sort")
        n = len(self.array)
        for k in range(n - 1):
            for i in range(n - 1 - k):
                if self.array[i] > self.array[i + 1]:
                    swap(self.array, i, i + 1)
                self.renderer.update_draw(self.array, i)
        self.renderer.update_draw(self.array, i)