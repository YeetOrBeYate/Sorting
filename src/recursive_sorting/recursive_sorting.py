# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a = 0
    b = 0 

    for k in range(0, elements):
        # compare A and B 
        # if a is out of range, push b and iterate
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b +=1
        # if b is out of range, push a and iterate
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        # if a is bigger, put it in array and iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a+=1
        # if b is bigger put it in array and iterate both
        else:
            merged_arr[k] = arrB[b]
            b+=1
        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

yeet = [1,5,3,90,30,22,6,78]

def merge_sort( arr ):

    if len(arr) > 1:

        left = merge_sort(arr[0:len(arr)//2])

        right = merge_sort(arr[len(arr)//2: ])


        arr = merge(left,right)

    return arr

merge_sort(yeet)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
