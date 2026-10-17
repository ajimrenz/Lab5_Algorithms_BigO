import random
import time
from config import *


def bubble_sort(arr):
    a, comps, moves = arr[:], 0, 0
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                moves += 1
                swapped = True
        if not swapped:
            break
    return a, comps, moves


def selection_sort(arr):
    a, comps, moves = arr[:], 0, 0
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            comps += 1
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            moves += 1
    return a, comps, moves


def insertion_sort(arr):
    a, comps, moves = arr[:], 0, 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if a[j] > key:
                a[j + 1] = a[j]
                moves += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comps, moves


show_inputs()
print("=== 3. E-COMMERCE ORDER PROCESSING ===")
random.seed(SEED_DIGIT)
count = 20 + NAME_LENGTH
base = sorted(random.sample(range(ID_SUM, ID_SUM + 10 * count), count))
shuffled = base[:]
random.shuffle(shuffled)
conditions = {"Sorted": base, "Reverse": base[::-1], "Random": shuffled}

print("Orders (sorted):", base)
print("Random input   :", shuffled)
print(f"\n{'Algorithm':<10}{'Input':<9}{'Comparisons':>12}{'Movements':>11}{'Time (ms)':>11}  Sorted?")
for name, fn in [("Bubble", bubble_sort), ("Selection", selection_sort), ("Insertion", insertion_sort)]:
    for cond, data in conditions.items():
        t0 = time.perf_counter()
        out, c, m = fn(data)
        ms = (time.perf_counter() - t0) * 1000
        print(f"{name:<10}{cond:<9}{c:>12}{m:>11}{ms:>11.4f}  {out == sorted(data)}")

print("""
Big O summary:
Bubble    best O(n) (sorted, early exit) | avg/worst O(n^2)
Selection always O(n^2) comparisons      | at most n-1 swaps
Insertion best O(n) (sorted)             | avg/worst O(n^2)
""")