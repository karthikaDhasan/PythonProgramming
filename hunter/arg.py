
n=5
string='guvi'
def exploder(str,c):
    print str*c
def myfun(exp,string,n):
    a=string
    b=n
    exp(a,b)
myfun(exploder,string,n)
