
def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.
    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    # sort list
    list.sort()
    print(list)
    while left <= right:
        middle = (left + right) // 2
        #print(middle)
        # check if key is at middle
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

print(binary_search(['koang','bol','pul','denile','desun','Yang','Del','Zaw'],'koang')) # should return 6