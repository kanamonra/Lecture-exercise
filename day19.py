# Sorting algorithm
# Insertion sort
import random


def find_insert_idx(ary, data):
    find_idx = -1
    for i in range(0, len(ary)):
        if ary[i] < data:
            find_idx = i
            break
    if find_idx == -1:
        return len(ary)
    else:
        return find_idx


before = [random.randint(0, 200) for _ in range(10)]
after = []


print('Before -->', before)
for i in range(len(before)):
    data = before[i]
    insPos = find_insert_idx(after, data)
    after.insert(insPos, data)
print('After -->', after)
