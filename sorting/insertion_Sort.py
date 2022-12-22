def insertion_Sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i-1
        while (j >= 0 and temp < alist[j]):
            alist[j+1] = alist[j]
            j = j-1
            alist[j+1] = temp


alist = input('enter the list to sort: ').split()
alist = [int(x) for x in alist]
insertion_Sort(alist)
print('Sorted list: ', end='')
print(alist)
