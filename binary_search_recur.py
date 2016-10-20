def binary_search(lst, x):
    if len(lst) == 0:
        return -1     

    mid = len(lst) / 2
    if x == lst[mid]:
        return mid
    elif x < lst[mid]:
        return binary_search(lst[0:mid], x)
    else:
        result = binary_search(lst[mid+1:], x)
        if result == -1:
            return result
        else:
            return result + mid + 1
    return -1

print binary_search([0,1,2,3,4,5], -1)
print binary_search([0,1,2,3,4,5], 0)
print binary_search([0,1,2,3,4,5], 1)
print binary_search([0,1,2,3,4,5], 2)
print binary_search([0,1,2,3,4,5], 3)
print binary_search([0,1,2,3,4,5], 4)
print binary_search([0,1,2,3,4,5], 5)
print binary_search([0,1,2,3,4,5], 6)