from config import *


def linear_search(data, target):
    comparisons = 0
    for i, v in enumerate(data):
        comparisons += 1
        if v == target:
            return i, comparisons
    return -1, comparisons

show_inputs()
print("=== 1. EMERGENCY DISPATCH RECORD SEARCH ===")
n = 10 + NAME_LENGTH
step = SEED_DIGIT + 2
original = [ID_SUM + i * step for i in range(n)]
rot = (SEED_DIGIT + 1) % n
rotated = original[rot:] + original[:rot]
target = ID_SUM + (ARTIST_SUM % n) * step

print("Original :", original)
print("Rotation point:", rot)
print("Rotated  :", rotated)
print("Target   :", target)
idx, comps = linear_search(rotated, target)
print(f"Found at index {idx}" if idx != -1 else "Target NOT found", "| comparisons:", comps)
print("Time: O(n) worst, O(1) best | Space: O(1)")