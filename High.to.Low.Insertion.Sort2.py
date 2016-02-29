import sys

def main():

    #list of result from searching
    resultList=user
    #list for prices to be sorted
    priceList=[]
    #final sorted list
    Sorted_Results_List=[]

    for n in resultList:
        priceList.append(n[6])

    def insertionsort( aList ):
        for i in range( 1, len( aList ) ):
            tmp = aList[i]
            k = i
            while k > 0 and tmp < aList[k - 1]:
                aList[k] = aList[k - 1]
                k -= 1
            aList[k] = tmp

    aList = priceList
    insertionsort( aList )

    for x in priceList:
        for y in resultList:
            if x!=y[6]:
                pass
            else:
                Sorted_Results_List.append(y)

    Sorted_Results_List.reverse()
    print(Sorted_Results_List)


if __name__ == '__main__':
    sys.exit(main())    
