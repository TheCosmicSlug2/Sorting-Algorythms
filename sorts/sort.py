
class Sort:
    def __init__(self, renderer, array) -> None:
        self.renderer = renderer
        self.array = array

    def reset(self, array):
        self.array = array.copy()