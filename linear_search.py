
def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

print(linear_search(['koang','bol','pul','denile','desun','Yang','Del','Zaw'],'koang')) # should return 0