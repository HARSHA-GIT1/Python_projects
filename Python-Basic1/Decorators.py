#IN PYTHON DECORATORS IS USE TO CHANGE THE FUNCTIONALITY OF A EXISTS FUNCTION DURING COMPLILE TIME
def x(a,b):
    if a<b:
        a,b=b,a
    return a/b
print(x(6,3))