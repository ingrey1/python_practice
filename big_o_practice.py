

# 1

def foo(array): 
    sum = 0
    product = 1
    for i in range(len(array)):
        sum += array[i]
    for i in range(len(array)):
        product * array[i]
    print("sum {}, product {}".format(sum, product)) 

numbers = [1, 2, 3]
# foo(numbers)
# O(N^2)



