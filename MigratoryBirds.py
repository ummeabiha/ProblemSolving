arr=[1,1,2,2,3]

def arrToDict(arr):
    birds= dict()
    for i in arr:
        if i in birds.keys():
            birds[i]+=1
        else:
            birds[i]=1
    return birds


def maxCount(arr):
    birds= arrToDict(arr)
    maxKey=[] #key
    maxValue=0 
    
    for i in birds.values():
        if maxValue<=i: 
            maxValue=i
    
    for i,j in birds.items():
        if j==maxValue:
            maxKey.append(i)
            
    max= sort(maxKey)
    return max
    

def sort(maxKey):
    for i in range(len(maxKey)-1):
        if maxKey[i] > maxKey[i+1]:
            maxKey[i], maxKey[i+1]= maxKey[i+1], maxKey[i]
        else:
            continue
    return maxKey
    
sorted_arr= maxCount(arr)
print(sorted_arr[0])
