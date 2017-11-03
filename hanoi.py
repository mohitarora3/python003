def hanoi(n,source,spare,target):
    '''
    objective:to solve problem of tower of hanoi using n discs and 3 poles
    input parameters:
                    n-number of disks
                    source-starting point where all disks are stored(in order)
                    spare-number of empty positions where there are no disks
                    target-the destination position where to place all disks(in order)
    return value:none
    '''

    assert n>0
    if n==1:
        print ('Move a disk from',source,'to',target)
    else:
        hanoi(n-1,source,target,spare)
        print('Move a disk from',source,'to',target)
        hanoi(n-1,spare,source,target)

hanoi(3,1,2,3)
