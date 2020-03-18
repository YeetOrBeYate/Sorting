# TO-DO: complete the helper function below to merge 2 sorted arrays

one = [1,2,4,5]
two = [1,2,5,6]

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO


    for y in range(0, len(merged_arr)-1)
    
        if arrA[y] < arrB[y]

            #switch
          
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

yeet = [1,5,3,90,30,22,6,78]

def merge_sort( arr ):

    

    if len(arr) > 1 :
        
        # TO-DO
        mid = len(arr)//2
        front = arr[:mid]
        back = arr[mid:]

        merge(front, back)

        print(f"front:{front}, back:{back}")
        merge_sort(front)
        merge_sort(back)

    else:
        return 'done'

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
