
def sum_num(lst):
    # remove the last element of the list
    lst.pop()
    # sum the list
    total = sum(lst)
    

    return total


numbers = [1,2,3,4,5]

print(sum_num(numbers))