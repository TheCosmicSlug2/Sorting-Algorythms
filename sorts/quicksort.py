from renderer import Renderer
from utils import choose_pivot
from sorts.sort import Sort

class QuickSort(Sort):
    def __init__(self, renderer: Renderer, array) -> None:
        super().__init__(renderer, array)

    def partition(self, array, p, s, e, main_array):
        piv_valeur = array[p]

        list1 = []
        list2 = []

        for idx, element in enumerate(array):
            # On ne remet pas le pivot dans les sous-tableaux
            if idx == p:
                continue

            if element <= piv_valeur:
                list1.append(element)
            else:
                list2.append(element)

            self.renderer.update_draw(
                main_array[:s]
                + list1
                + [piv_valeur]
                + list2
                + array[idx + 1:]
                + main_array[e:],
                s + len(list1)
            )

        main_array[s:e] = list1 + [piv_valeur] + list2

        return list1, piv_valeur, list2


    def quicksort(self, array, s, e, main_array):
        if len(array) <= 1:
            return array

        p = choose_pivot(0, len(array) - 1)

        a1, pivot, a2 = self.partition(array, p, s, e, main_array)

        def dis(arr, s, e, main_array):
            if len(arr) >= 2:
                return self.quicksort(arr, s, e, main_array)
            return arr

        a1 = dis(
            a1,
            s,
            s + len(a1),
            main_array
        )

        a2 = dis(
            a2,
            s + len(a1) + 1,
            e,
            main_array
        )

        arr = a1 + [pivot] + a2

        main_array[s:e] = arr

        self.renderer.update_draw(main_array, s + len(a1))

        return arr


    def sort(self):
        self.renderer.captionize("Quick Sort")
        self.quicksort(self.array, 0, len(self.array), self.array.copy())