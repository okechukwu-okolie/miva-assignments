# creating sets
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {4, 5, 6, 7, 8}
C = {1, 2, 3}

#performing unions
union_set = A | B
print('these contain all the elements of A and B without repeating any elements:')
print("Union of A and B:", union_set)
print('')
print('')

#performing intersections
intersection_set = A & B
print('these only contain the common elements of A and B:')
print("Intersection of A and B:", intersection_set)
print('')
print('')
#performing symmetric difference
sym_diff_set = A ^ B
print('these only contain the elements that are in A or B but not in both:')
print("Symmetric difference of A and B:", sym_diff_set)
print('')
print('')

#checking subset and supersets
#what is a subset? A set A is a subset of another set B if all elements of A are also elements of B. In other words, A is contained within B. For example, if A = {1, 2} and B = {1, 2, 3}, then A is a subset of B because all elements of A (1 and 2) are also in B.

#what is a superset? A set A is a superset of another set B if all elements of B are also elements of A. In other words, A contains B. For example, if A = {1, 2, 3} and B = {1, 2}, then A is a superset of B because all elements of B (1 and 2) are also in A.
print('these are used to check if one set is a subset or superset of another set:')
print("Is C a subset of A?", C.issubset(A))
print('')
print("Is A a superset of C?", A.issuperset(C))
print('')
print("Is B a subset of A?", B.issubset(A))
print('')
print("Is A a superset of B?", A.issubset(B))
print('')