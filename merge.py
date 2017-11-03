#initializing two sorted list
lst1=[2,4,6,8,10]
lst2=[1,3,5,7,9]

def merge(lst1,lst2,i=0,j=0):
    '''
    objective:to merge two sorted list
    input parameters:lst1-first sorted list
                     lst2-second sorted list
                     i(default argument)-that points to current element in lst1
                     j(default argument)-that points to current element in lst2
    return value-a merged list
    '''
    #approach-using concatenator operator '+'

    first_list_size=len(lst1)
    second_list_size=len(lst2)
    if((i==first_list_size)&(j==second_list_size)):
        return []
    elif(i==first_list_size):
        return [lst2[j]]+merge(lst1,lst2,i,j+1)
    elif(j==second_list_size):
        return [lst1[i]]+merge(lst1,lst2,i+1,j)
    elif(lst1[i]<lst2[j]):
        return [lst1[i]]+merge(lst1,lst2,i+1,j)
    else:
        return [lst2[j]]+merge(lst1,lst2,i,j+1)
        
print(merge(lst1,lst2))
