a= 5
b=6
def add(a,b):
    return a+b
print(add(a,b))
print("rajesj")

def max_of_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        return str(num1)+"is grater among all"
    elif num2>num1 and num2>num3:
        return str(num2)+"is grater among all"
    else:
        str(num3)+"is grater among all"
print(max_of_num(5,8,1))
