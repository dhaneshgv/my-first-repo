i = 5

def f(arg=i):
    print(arg)
print(i,'b4')
i = 6
print(i,'aftr')
f(i)
