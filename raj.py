
def add(a,b):
    return str(a+b)+" "+"is sum of numbers"
print(add(5,4))


def max_of_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        return str(num1)+"is grater among all"
    elif num2>num1 and num2>num3:
        return str(num2)+"is grater among all"
    else:
        str(num3)+"is grater among all"
print(max_of_num(5,8,1))
