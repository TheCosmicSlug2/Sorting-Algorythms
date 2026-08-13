
from random import randint

def check_sorted(array):
    return all(a < b for a, b in zip(array, array[1:]))

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def choose_pivot(a, b):
    return randint(a, b)