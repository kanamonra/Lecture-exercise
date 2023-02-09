# Sorting algorithm chapter 12
# Quick sort
import random

def quickSort(ary):
    global count_quick
    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[n // 2]
    leftAry, rightAry, midAry = [], [], []

    for num in ary:
        if num > pivot:
            leftAry.append(num)
        elif num < pivot:
            rightAry.append(num)
        else:
            midAry.append(num)

    count_quick = count_quick + 1
    return quickSort(leftAry) + [pivot] + quickSort(rightAry)


dataAry = [random.randint(0, 200) for _ in range(20)]
count_quick = 0
print('Before sort -->', dataAry)
dataAry = quickSort(dataAry)
print('After sort', dataAry)
print("Quick repeat time:", count_quick, end=' ')
