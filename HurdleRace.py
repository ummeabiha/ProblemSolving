def hurdleRace(k, height):
    
    def findMaxUsingSelectionSort(height):
        for i in range(len(height)): 
            min_idx = i 
            for j in range(i+1, len(height)): 
                if height[min_idx] > height[j]: 
                    min_idx = j 
        
            height[i], height[min_idx] = height[min_idx], height[i]
        
        return height[-1]
        

height=[6,3,4,2,1]
k=2
max= findMaxUsingSelectionSort(height)
totalPotions= max-k

if totalPotions>=0:
    return totalPotions   
else:
    return 0     
