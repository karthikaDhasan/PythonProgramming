list=['aa','bb','gg']
def fun(x):
    return x.upper()
list1=[fun(x) for x in list]
print list1
