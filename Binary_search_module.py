list_a = ''
for i in range(0, 101, 2):
    list_a += str(i) + ','
list_a = list_a.split(',')
list_a = list(list_a)
def binary_search(list_a, target):
    left = 0
    right = len(list_a)
    if str(target) in list_a:
        while left <= right:
            mid = left + right//2
            if int(list_a[mid]) == target:
                print('element is found at index', mid)
                break
            elif int(list_a[mid]) < target:
                left = mid +1
            else:
                right = mid - 1
    else:
        print('please enter valid number')
a = int(input())
binary_search(list_a, a)
