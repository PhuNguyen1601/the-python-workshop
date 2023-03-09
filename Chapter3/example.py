 ## The nonlocal keyword
 
x = 4
def myfunc():
    x = 3
    def inner():
        nonlocal x
        print(x)
    inner()
    
    
myfunc()