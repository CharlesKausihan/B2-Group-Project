import sys
import sqlite3 as sql


def main():
    sqliteFile = 'Car_Database.sqlite'
    
    resultList=user
    priceList=[]
    Sorted_Results_List=[]
    #connecting to car database
    con =  sql.connect (sqliteFile)
    cur = con.cursor()
    
    #selecting results from Cars table and appending resutlts to an empty list
    cur.execute('''SELECT * FROM Cars''')
    for row in cur:
        resultList.append(row)
    con.close()
    
    #putting prices for individual car in seperate list
    for n in resultList:
        priceList.append(n[6])
    
    def swaping(i, j):                    
        rList[i], rList[j] = rList[j], rList[i] 

    def heap(end,i):   
        l=2 * i + 1  
        r=2 * (i + 1)   
        max=i   
        if l < end and rList[i] < rList[l]:   
            max = l   
        if r < end and rList[max] < rList[r]:   
            max = r   
        if max != i:   
            swaping(i, max)   
            heap(end, max)   

    def heapSort():     
        end = len(rList)   
        start = end // 2 - 1 # use // instead of /
        for i in range(start, -1, -1):   
            heap(end, i)   
        for i in range(end-1, 0, -1):   
            swaping(i, 0)   
            heap(i, 0)

    rList = priceList
    heapSort()
    '''comparing resultList and priceList and adding results in asending order to
    sorted_Results_List'''
    for x in priceList:
        for y in resultList:
            if x!=y[6]:
                pass
            else:
                Sorted_Results_List.append(y)

                
    con.close()



if __name__ == '__main__':
    sys.exit(main())    
