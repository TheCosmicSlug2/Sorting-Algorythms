
from renderer import Renderer
from sorts.sort import Sort

class FusionSort(Sort):
    def __init__(self, renderer: Renderer, array) -> None:
        super().__init__(renderer, array)

    def split_array(self, array, s, e, main_array):
        mid = len(array) // 2

        a1 = array[:mid]
        a2 = array[mid:]

        self.renderer.update_draw(
            main_array[:s] + a1 + a2 + main_array[e:],
            s + mid
        )

        main_array[s:e] = a1 + a2

        return a1, a2


    def refusion(self, a1, a2, s, e, main_array):
        new_arr = []

        idx1 = 0
        idx2 = 0

        while idx1 < len(a1) or idx2 < len(a2):

            self.renderer.update_draw(
                main_array[:s]
                + new_arr
                + a1[idx1:]
                + a2[idx2:]
                + main_array[e:],
                s + len(new_arr)
            )

            if idx1 == len(a1):
                new_arr.append(a2[idx2])
                idx2 += 1

            elif idx2 == len(a2):
                new_arr.append(a1[idx1])
                idx1 += 1

            elif a1[idx1] <= a2[idx2]:
                new_arr.append(a1[idx1])
                idx1 += 1

            else:
                new_arr.append(a2[idx2])
                idx2 += 1

        self.renderer.update_draw(
            main_array[:s] + new_arr + main_array[e:],
            s + len(new_arr) - 1
        )

        return new_arr


    def fusion_sort(self, array, s, e, main_array):
        if len(array) <= 1:
            return array

        a1, a2 = self.split_array(array, s, e, main_array)

        mid = s + len(a1)

        a1 = self.fusion_sort(
            a1,
            s,
            mid,
            main_array
        )

        a2 = self.fusion_sort(
            a2,
            mid,
            e,
            main_array
        )

        arr = self.refusion(
            a1,
            a2,
            s,
            e,
            main_array
        )

        main_array[s:e] = arr

        return arr

    

    def sort(self):
        self.renderer.captionize("Fusion Sort")

        main_array = self.array.copy()

        self.fusion_sort(
            main_array,
            0,
            len(main_array),
            main_array
        )
