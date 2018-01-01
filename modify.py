def Remove(lst,i=0):
    '''
    objective-to remove adjacent duplicate elements from the list
    input parameters-
                    lst- a list
    return value-
                lst- a modified list
    '''
    #approach-using recursion
    
    if(i==len(lst)-1):
        return lst
    
    elif(lst[i]!=lst[i+1]):
        return Remove(lst,i+1)
    else:
        while(lst[i]==lst[i+1]):
            lst.remove(lst[i+1])
        lst.remove(lst[i])
        return Remove(lst,i)
#testcase1    
lst=[1,2,2,2,4,4,5,5,6,6,6,6,6,6,9]
print(Remove(lst))
        
        
#testcase2
lst=[1,2,4,4,5,7,7,7,8,8,9,7]
print(Remove(lst))
