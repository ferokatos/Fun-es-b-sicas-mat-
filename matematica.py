def soma (a,b):
    return a + b
def sub (a,b):
    return a - b
def mul (a,b):
    return a*b
def div (a,b):
    return a/b
def segundo_grau (a,b,c):
    D = (b*b) - (4*a*c)
    x1 = (-b + (D**0.5))/(2*a)
    x2 = (-b - (D**0.5))/(2*a)
    return x1,x2
