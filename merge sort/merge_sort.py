def merge_sort(element):
    if len(element)<=1:
        return
    mid = len(element)//2
    left = element[:mid]
    right = element[mid:]
    merge_sort(left)
    merge_sort(right)

    merge_sort_sorted(left,right,element)



def merge_sort_sorted(a,b,arr):
    i=j=k=0
    while len(a)-i>0 and len(b)-j>0:
        if a[i]>b[j]:
            arr[k] = b[j]
            j+=1
        else:
            arr[k] = a[i]
            i+=1
        k+=1
    while len(a)-i>0:
        arr[k] = a[i]
        i += 1
        k += 1
    while len(b)-j>0:
        arr[k] = b[j]
        j += 1
        k += 1

numbers = [34,56,2,54,26,5,22,3,7,876,44]
merge_sort(numbers)
print(numbers)