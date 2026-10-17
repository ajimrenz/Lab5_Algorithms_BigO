from config import *


def merge(a, b):
    result, i, j, comparisons = [], 0, 0, 0
    while i < len(a) and j < len(b):
        comparisons += 1
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result, comparisons


show_inputs()
print("=== 2. UNIVERSITY ENROLLMENT RECORDS ===")
size = 8
A = [SEED_DIGIT + i * ID_SUM for i in range(size)]
B = [NAME_LENGTH + i * ARTIST_LENGTH for i in range(size)]
merged, comps = merge(A, B)
print("Dept A      :", A)
print("Dept B      :", B)
print("Consolidated:", merged)
print("Records before:", len(A), "+", len(B), "| after:", len(merged))
print("Comparisons :", comps)
print("Ordering verified:", merged == sorted(merged),
      "| count verified:", len(merged) == len(A) + len(B))
print("Time: O(m+n) | Space: O(m+n)")