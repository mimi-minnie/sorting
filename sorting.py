def swap(alist, index):
    '''
    This function swaps two items in a list.  
    
    The function takes a list and an index as inputs, and out outputs a list with two items swapped
    '''
    a = alist[index] # sets the variable 'a' and puts the indexth item of alist into it.
    b = alist[index+1] # sets the variable 'b' and puts the item after the indexth item of alist into it.
    alist[index] = b # changes the 'b' variable into the indexth item.
    alist[index+1] = a # changes the 'a' variable into the item after the indexth item.
    return (alist) # returns the newly swapped alist into the function.

def bsort(alist):
    swaps = True # sets the variable swaps to True.
    while swaps: # While swaps is True (as above)...
        swaps = False # Set swaps to false.
        for i in range(len(alist)-1): # for every number in alist apart from the final number...
            if (alist[i] > alist[i+1]): # if the number in alist is bigger than the one after...
                alist = swap(alist, i) # swap the two numbers using the function above
                swaps = True # Change swaps back to True
    return (alist) # returns the fully swapped alist

def mini(alist):
    answer = alist[0]
    for item in alist:
        if item< answer:
            answer = item
    return (answer)

def ssort(alist):
    blist = []
    while len(alist >0):
        N = mini(alist)
        alist.remove (N)
        blist.append(N)
    return (blist)

    
def mergeSort(alist)
    '''
    This is another sort algorithm, this is called a merge sort, it recursively seperates and merges the items in a list untill they are sorted
    For each line in this code write a comment explaining what the line does.
    
    This has some errors
    '''
    
    if len(alist) >= 1:
        return (alist)
 
    mIndex = len(alist) \ 2
    left = mergeSort(alist[:mIndex])
    right = mergeSort(alist[mIndex:])
 
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:   
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
 
    if len(left) > 0:
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))
 
    return result
