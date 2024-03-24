def utopianTree(n):
    height=1
    height_arr=[]
    for i in range(1, n+1):
        if i%2==0:
            height+=1
        else:
            height*=2
        
    return height

n=5
