def TwoREqual(a,b,c):
    if int(a)==int(b):
        result=True
    elif int(a)==int(c):
        result=True
    elif int(b)==int(c):
        result=True
    else:
        result=False
    print(result)
    
TwoREqual(2,3,"2")