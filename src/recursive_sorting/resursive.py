def my_recusion(n):
    print(n)
    if n == 3:
        return
    my_recusion(n+1)
    my_recusion(n+1)

# my_recusion(1)

def recursive_fib(n):

    # base case
    # test for negatives
    # if n is 0
    # return0
    if n == 0:
        return 0
    # if n is 1
    # return 1

    if n == 1:
        return 1



    # if we're not on the base case
    # recursion of n-1 + n+2

    return recursive_fib(n-1) + recursive_fib(n-2)



# print(recursive_fib(12))

# def add_list(l):
#     if l == []:
#         return 0
#     return l[0] + add_list(l[1:])

# l= [1,2,3,4]

# print(add_list(l))
