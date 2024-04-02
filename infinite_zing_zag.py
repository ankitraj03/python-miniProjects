import time, sys

indent =0  
indentincreasing= True

while True:
    print(' ' * indent, end='')
    time.sleep(0.1)
    if indentincreasing==True:
        print("******")
        indent=indent+1
        if indent==20:
            indentincreasing=False
    else:
        print("******")
        indent-=1
        if indent==0:
            indentincreasing=True
