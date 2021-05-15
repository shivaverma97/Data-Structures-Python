def inserstion_sort(elements):
    for i in range(len(elements)-1):
        start = elements[i]
        j = i -1
        while j>=0 and start < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = start

    return elements

numbers = [11, 5, 9, 2, 15, 29, 3, 23]
inserstion_sort(numbers)
print(numbers)