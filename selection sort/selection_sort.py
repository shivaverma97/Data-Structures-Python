def selection_sort(element):
    size = len(element)
    for i in range(size):
        min_index = i
        for j in range(min_index,size):
            if element[min_index]>element[j]:
                min_index=j
        if i!= min_index:
            element[min_index], element[i] = element[i], element[min_index]



numbers = [12,3,34,5,2,67,78,9,1]
selection_sort(numbers)
print(numbers)