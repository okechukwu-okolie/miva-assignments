#1. Create two sets with your choice of elements and find their union.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1 | set2
print("Union of set1 and set2:", union_set)
print('')

#2. For the above sets, determine their intersection
intersection_set = set1 & set2
print("Intersection of set1 and set2:", intersection_set)
print('')

#3.Using a set of numbers from 1 to 10 and another set of numbers from 5 to 15, determine the symmetric difference.
set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set4 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
sym_diff_set = set3 ^ set4
print("Symmetric difference of set3 and set4:", sym_diff_set)
print('')


#4. Check if the set `{1, 2, 3}` is a subset of `{0, 1, 2, 3, 4, 5}
subset_set = {1, 2, 3}
superset_set = {0, 1, 2, 3, 4, 5}
is_subset = subset_set.issubset(superset_set)
print("Is {1, 2, 3} a subset of {0, 1, 2, 3, 4, 5}?", is_subset)
print('')