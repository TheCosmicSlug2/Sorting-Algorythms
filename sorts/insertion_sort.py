from renderer import Renderer

class InsertionSort:
    def __init__(self, renderer: Renderer, array) -> None:
        self.renderer = renderer
        self.array = array

    def sort(self):
        self.renderer.captionize("Insertion Sort")

        for idx in range(1, len(self.array)):
            value = self.array[idx]
            value2 = idx - 1
            while value2 >= 0 and value < self.array[value2]:
                self.renderer.update_draw(self.array, value2)
                self.array[value2 + 1] = self.array[value2]
                value2 -= 1
            self.array[value2 + 1] = value

        self.renderer.update_draw(self.array, idx)

