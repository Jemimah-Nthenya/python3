def add(x,y):
    result=x + y
    return result

def subtract(x,y):
    result=x-y
    return result

def divide(x,y):
    result=x/y
    return result

def multiply(x,y):
    result=x*y
    return result

def remainder(x,y):
    result=x%y
    return result

def power_of(x,y):
    result=x**y
    return result

def merge(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
print(merge(dict1, dict2))
 
print(dict2)



