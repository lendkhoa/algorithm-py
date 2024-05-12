# Write a function that takes in a non empty array of integers and
# return an array of the same length, where each element in the output
# array is equal to the product of every other number in the input array

def arrayOfProducts(array):
    # fill the array with 1s
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct;
        leftRunningProduct *= array[i];

    # traverse the reversed input array
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products
