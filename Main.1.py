numbers1 = [1, 2, 3,4]
numbers2 = [4, 5, 6,3]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

nums = [1, 2, 3, 4, 5,8]
def sq(n):
    return n * n

square = list(map(sq, nums))
print("Square of numbers in list")
print(square)
