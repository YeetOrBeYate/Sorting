# TO-DO: Complete the selection_sort() function below 

yeet = [6,9,7,21,63,4,1]

arr = [1,3,2,4]


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        print(f"ITERATION-position:{i} what is the smallest number: {arr[smallest_index]}")
        # Making the given assumption that our first item is our smallest

        # Looping through the remaining right items of our assumed smallest
        for x in range(smallest_index+1, len(arr)):
            if arr[x] < arr[smallest_index]:
                print(f"COMPARE-{arr[x]} is smaller than {arr[smallest_index]}")
                smallest_index = x
             
        # TO-DO: swap
        # tuple swap
        # basically make the true smallest number swap values, and therefore positions, with the assumed smallest value
        print(f"SWAP-:{arr[smallest_index]} will replace :{arr[i]}")
        print(f"SWAP-:{arr[i]} will replace :{arr[smallest_index]}")
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr

print(selection_sort(yeet))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr