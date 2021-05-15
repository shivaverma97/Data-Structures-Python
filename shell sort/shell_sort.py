def shell_sort(element):
    size = len(element)
    gap = size//2

    while gap> 0 :
        for i in range(gap,size):
            var = element[i]
            j = i
            while j>=gap and element[j-gap]>var:
                element[j] = element[j-gap]
                j-=gap
            element[j] = var
        gap = gap//2


numbers = [3,1,53,7,23,764,232,33]
shell_sort(numbers)
print(numbers)




