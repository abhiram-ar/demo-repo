def multiply(x, y):
    # initialize the result to zero
    result = 0
    # loop through the bits of y
    while y:
        # if the rightmost bit of y is set, add x to the result
        if y & 1:
            result = add(result, x)
        # shift x left by one bit and y right by one bit
        x = shift_left(x)
        y = shift_right(y)
    return result

# helper function to shift a number left by one bit
def shift_left(num):
    return num << 1

# helper function to shift a number right by one bit
def shift_right(num):
    return num >> 1

# helper function to add two numbers using bitwise operators
def add(x, y):
    # loop until there is no carry
    while y:
        # calculate the carry using bitwise AND
        carry = x & y
        # calculate the sum using bitwise XOR
        x = x ^ y
        # shift the carry left by one bit
        y = carry << 1
    return x

# example usage
print(multiply(3, 5)) # output: 15
