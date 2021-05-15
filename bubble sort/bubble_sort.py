def bubble_sort(elements):
    size = len(elements)
    swapped = False
    for j in range(size-1):
        for i in range(size-1):
            if elements[i]>elements[i+1]:
                temp = elements[i+1]
                elements[i+1]=elements[i]
                elements[i] = temp
                swapped = True
        if swapped == False:
            break
    return elements


numbers = [12,43,1,3,15,78,6,33]
bubble_sort(numbers)
print(numbers)