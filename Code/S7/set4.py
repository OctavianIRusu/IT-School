list1 = [22, 34, 56, 65, 45]
list2 = [23, 34, 65, 55]

common = set(list1).intersection(set(list2))
print(common)

diff1 = set(list1).difference(set(list2))
diff2 = set(list2).difference(set(list1))
print(diff1)
print(diff2)

set1 = set(list1)
set1.update(list2)
print(set1)