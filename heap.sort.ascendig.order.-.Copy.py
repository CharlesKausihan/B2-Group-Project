import sys

def main():

    #list of results from searching
    resultList=user
    #list for prices to be sorted
    priceList=[]
    #final sorted list
    Sorted_Results_List=[]
      
    #putting prices for individual car in seperate list
    for n in resultList:
        priceList.append(n[6])
    
    def swap(i, j):                    
        sqc[i], sqc[j] = sqc[j], sqc[i] 

    def heapify(end,i):   
        l=2 * i + 1  
        r=2 * (i + 1)   
        max=i   
        if l < end and sqc[i] < sqc[l]:   
            max = l   
        if r < end and sqc[max] < sqc[r]:   
            max = r   
        if max != i:   
            swap(i, max)   
            heapify(end, max)   

    def heap_sort():     
        end = len(sqc)   
        start = end // 2 - 1
        for i in range(start, -1, -1):   
            heapify(end, i)   
        for i in range(end-1, 0, -1):   
            swap(i, 0)   
            heapify(i, 0)

    sqc = priceList
    heap_sort()
    '''comparing resultList and priceList and adding results in asending order to
    sorted_Results_List'''
    for x in priceList:
        for y in resultList:
            if x!=y[6]:
                pass
            else:
                Sorted_Results_List.append(y)

    print(Sorted_Results_List)                



if __name__ == '__main__':
    sys.exit(main())    
