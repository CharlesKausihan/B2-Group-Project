import sys
import sqlite3 as sql


def main():
    sqliteFile = 'Car_Database.sqlite'

    resultList=[]
    priceList=[]
    Sorted_Results_List=[]

    con =  sql.connect (sqliteFile)
    cur = con.cursor()

    cur.execute('''SELECT * FROM Cars''')
    for row in cur:
        resultList.append(row)
    con.close()

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

        

    

 
         
    con.close()



if __name__ == '__main__':
    sys.exit(main())    
