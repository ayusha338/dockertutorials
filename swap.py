def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y

x=int(input("enter vlaue for x"))
y=int(input("enter value fro y"))
print("the value of x and y before swapping is {0} and {1}".format(x,y))
print("the value of x and y after swapping is {0} and {1} ",swap(x,y))