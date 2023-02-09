# Sorting algorithm chapter 12
# Quick sort

def quickSort(ary):
    global count_quick
    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[n // 2]
    leftAry, rightAry, midAry = [], [], []

    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
        else:
            midAry.append(num)

    count_quick = count_quick + 1
    return quickSort(leftAry) + [pivot] + quickSort(rightAry)


dataAry = [55, 55, 66, 67, 67, 78, 78, 898, 122, 65, 2, 57, 33, 98]
count_quick = 0
print('Before sort -->', dataAry)
dataAry = quickSort(dataAry)
print('After sort', dataAry)
print("Quick repeat time:", count_quick, end=' ')
