def binary_search(lst, x):
    lo = 0
    hi = len(lst)-1
    while lo <= hi:
        mid = (lo + hi) / 2
        if x == lst[mid]:
            return mid
        elif x < lst[mid]:
            if (lst[lo] < lst[mid] and
                lst[lo] <= x):
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if (lst[mid] < lst[hi] and
                lst[hi] >= x):
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

print binary_search([0,1,2,3,4,5], -1)
print binary_search([0,1,2,3,4,5], 0)
print binary_search([0,1,2,3,4,5], 1)
print binary_search([0,1,2,3,4,5], 2)
print binary_search([0,1,2,3,4,5], 3)
print binary_search([0,1,2,3,4,5], 4)
print binary_search([0,1,2,3,4,5], 5)
print binary_search([0,1,2,3,4,5], 6)

print binary_search([3,4,5,0,1,2], -1)
print binary_search([3,4,5,0,1,2], 3)
print binary_search([3,4,5,0,1,2], 4)
print binary_search([3,4,5,0,1,2], 5)
print binary_search([3,4,5,0,1,2], 0)
print binary_search([3,4,5,0,1,2], 1)
print binary_search([3,4,5,0,1,2], 2)
print binary_search([3,4,5,0,1,2], 6)

