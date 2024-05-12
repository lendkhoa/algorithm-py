from typing import List


def fixed_size_sliding_window(array: List[int], k: int):
    n = len(array)
    max_sum = 0
    window_sum = sum(array[0:k])

    for i in range(n - k):
        # remove left index
        window_sum = window_sum - array[i] + array[i + k]


# fixed_size_sliding_window([1,2,3,4,5], 3);


def add(a, b):
    running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b

    while temp_a or temp_b:
        ak, bk = a & k, b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        running_sum |= ak ^ bk ^ carryin
        carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
        return running_sum | carryin


"""
Imagine you have two jars of candies, one labeled x and the other labeled y. Each candy represents a bit (either a 0 or a 1).

Now, you want to add the candies from both jars together. Here's how the function works:

You start by looking at both jars (bits) and see if there are any candies (bits) in both jars. 
These are the ones you need to carry over to the next place value if they add up to more than one.
Next, you take out all the candies (bits) from jar x and y that are different from each other and put them in a new jar called x. 
This is like adding the candies from both jars together, but ignoring the ones you need to carry over.
Then, you look at the candies you set aside (carry) from the previous step. You shift them one place to the left and put them back into jar y. 
This is like carrying over the extra candies to the next place value.
You keep doing these steps until you've added all the candies from jar y to jar x, and there are no more candies left in jar y.
Finally, you look at jar x, which now has all the candies added together. That's your answer!
"""


def Add(x, y):
    # continues until y becomes zero,
    # indicating that there are no more carry-over bits to add.
    while y != 0:
        # carry the common set bits of x & y
        # This operation identifies the bits where both x and y have a 1.
        carry = x & y
        print(f"carry {carry}")

        # Sum of bits of x and y where at
        # least one of the bits is not set
        # This operation sets the bits in x
        # that are different from the corresponding bits in y
        x = x ^ y
        print(f"XOR {x}")

        # Carry is shifted by one so that
        # adding it to x gives the required sum
        y = carry << 1
        print(f"y: {y}")

    return x


def multiply(x, y):
    running_sum = 0
    while x:  # examine each bit of x
        if x & 1:
            running_sum = Add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum


# Time: O(n)
# Space: O(1)
def divide(x, y):
    result, power = 0, 32
    y_power = y << 32  # y * 2^32
    print(f"Result {result}, power: {power}, y_power: {y_power}")
    while x >= y:
        print(f" x, y: {x}, {y}, y_power {y_power}")
        while y_power > x:
            y_power >>= 1
            power -= 1
            print(f"  y_power {y_power} | power {power}")
        result += 1 << power
        x -= y_power
        print(f" result: {result} | x {x}")
    return result


def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x

    while power:
        if power & 1:
            result *= x
            print(f"LSB of y is 1 | result: {result} * x: {x}")
        x, power = x * x, power >> 1
        print(f"x: {x} | y: {power} | result: {result}")
    return result


def count_pairs_with_diff_1(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == 1:
                count += 1
    return count


power(2, 2)
# print(Add(1, 2))
# print(multiply(1, 2))
# divide(11, 2)

# print(count_pairs_with_diff_1([4, 5, 2]))
