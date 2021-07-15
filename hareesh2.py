def find_value(array, x):
    for index,value in enumerate(array):
        if value == x:
            return index 
    return -1 
array = [1, 2,3,4]
x = 30 
print(x,find_value(array,x))