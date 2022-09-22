def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_number=-1
    
    for i in range(0, len(numbers)):
        if numbers[i]>max_number:
            max_number = numbers[i]
    return max_number



if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
