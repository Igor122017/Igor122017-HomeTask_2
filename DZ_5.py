#  5 Реализовать алгоритм перемешивания списка.
spisok = [4,56,12,14,32,51,2,1,7,3,77,44,24,90,9,5,3]

sort=[]
sort1=[]

for i in spisok:
    if i % 2 == 0:
        sort.append(i)
    if i %2 !=0:
        sort1.append(i)        
sort.sort()
sort1.sort()    
sort.extend(sort1)    
   
print(sort)