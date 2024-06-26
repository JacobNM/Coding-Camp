# Linear search function

def linear_search(target: int, data: list[int]) -> int:
    for number in data:
        print(number, target, data)
        if target == number:
            return target
    return None

#print(linear_search(3, [1, 2, 9, 5, 7, 8, 3]))

# Binary Search Function

def binary_search(target: int, data: list[int]) -> int:
    midpoint = len(data)//2
    while target != data[midpoint]:
        print(midpoint, target, data)
        if target < data[midpoint]:
            data = data[:midpoint]
        else:
            data = data[midpoint+1:]
        midpoint = len(data)//2
        if not data:
            return None
    return target

print(binary_search(2, [1, 2, 3, 5, 7, 8, 9, 10]))