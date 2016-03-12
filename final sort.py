
#list of results from searching
resultList=user #user is the variable name for the list with resutlts from searching

#list for prices to be sorted
priceList=[] #list to add prices to for sorting 

#final sorted list
Sorted_Results_List=[] #final list which will be used to for the sorted full list low to high

Sorted_Results_List2=[] #high to low

#putting prices for individual car in seperate list
for n in resultList:
    # for each element in price list
    #add the price (6th element in tuple) to price list
    priceList.append(n[6])

#selection sort algorithm
def selectionSort(sqc):
   for i in range(len(sqc)-1,0,-1):
       maxPos=0
       for n in range(1,i+1):
           if sqc[n]>sqc[maxPos]:
               maxPos = n

       j = sqc[i]
       sqc[i] = sqc[maxPos]
       sqc[maxPos] = j
       
#insertion sort algorithm
def insertionsort( seq ):
    for i in range( 1, len( seq ) ):
        t = seq[i]
        j = i
        while j > 0 and t < seq[j - 1]:
            seq[j] = seq[j - 1]
            j -= 1
        seq[j] = t

#merge sort algorithm
def mergeSort(alist):
    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


#using sorted priceList and unsorted resultList to form sorted results list 
def finalSort():
    #comparing resultList and priceList and adding results in asending order to
    #sorted_Results_List
    for x in priceList:
        for y in resultList:
            if x!=y[6]:
                pass
            else:
                Sorted_Results_List.append(y)
                Sorted_Results_List2.append(y)
                
# if statements deciding which sorting algorithm to use depending on size

if len(priceList)<=5:
    '''call selection sort function
    if the length o the list is 5 or less '''
    selectionSort(priceList)
else:
    pass

if len(priceList)>5 and len(priceList)<=25:
    '''call insetion sort function
    if the list is longer than 5 but less than 25 '''
    insertionsort(priceList)


if len(priceList)>25:
    '''call merge sort function if the list is longer than 50 '''
    mergeSort(priceList)
    
'''calling final sort
function after decision
on algorithm to use has been made and list has been sorted''' 
finalSort()

Sorted_Results_List2.reverse()
