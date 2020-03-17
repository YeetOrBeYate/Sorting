# TO-DO: Complete the selection_sort() function below 

yeet = [6,9,7,21,63,4,1]

arr = [1,5,3,4,2]


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        smallest_index = i


        print('-------------')
        print(f"ITERATION-position:{i} what is the smallest number: {arr[smallest_index]}")
        # Making the given assumption that our first item is our smallest

        # Looping through the remaining right items of our assumed smallest
        for x in range(smallest_index+1, len(arr)):

            print(f"looping through indexes: {smallest_index+1}-{len(arr)}")

            if arr[x] < arr[smallest_index]:

                print(f"COMPARE-{arr[x]} is smaller than {arr[smallest_index]}")

                smallest_index = x

                print(f"TRUTH-The true smallests number:{arr[smallest_index]}")
             
        # TO-DO: swap
        # tuple swap
        # basically make the true smallest number swap values, and therefore positions, with the assumed smallest value
        print(f"SWAP-:{arr[smallest_index]} in position:{smallest_index} will replace :{arr[i]} in position:{i}")
        print(f"SWAP-:{arr[i]} in position:{i} will replace :{arr[smallest_index]} in position:{smallest_index}")

        
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]



    return arr

# print(selection_sort(yeet))


# arr = [1,5,3,4,2]
# arr = [1,3,5,4,2]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for x in range(0, len(arr)-1):

        for j in range(0, len(arr)-1):
            #when the right value is smaller
            if arr[j +1] < arr[j]:
                #make the smaller value and bigger value switch posisions
                #since this parent loop goes through each parent element we can just change the array using this child loops indexes
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(arr))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr