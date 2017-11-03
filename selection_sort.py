def sort(lst,i=0,ik=-1,index=0,small=100):
    '''
    objective-to sort a list using selection sort
    input parameters:
                      lst-a list that is to be sorted
                      i-default argument(default value-0)
                      ik-default argument(default value--1)
                      index-default argument(default value-0))
                      small-default argument(default value-100)
   return value-none
   '''
   #assumption-smallest element of list is greater than 100
   #approach-using recursion
   
    size=len(lst)
    if(i==size):
        return

    if lst[index]<small:
        small=a[index]
        ik=index

    if(index==size-1):
        if(i!=ik):
            temp=lst[i]
            lst[i]=lst[ik]
            lst[ik]=temp
        index=i+1
        sort(lst,i+1,ik,index,100)
        return
	    
    sort(a,i,ik,index+1,small)
	
lst=[67,1,3,100,2,4,90]
print('Before',lst)
sort(lst)
print('After',lst)
