data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_sum(data_structure):
    summa = 0
    if isinstance(data_structure, (list, set, tuple)):
        for i in data_structure:
            summa += calculate_sum(i)


#def listsum(numList):
   #if len(numList) == 1:
        #return numList[0]
   #else:
        #return numList[0] + listsum(numList[1:])

#print(listsum([1,2,3,4,5,6,7,8,2,35,26]))

#def sum():
    #theSum = 0
    #for i in data_structure:
        #theSum = theSum + i
    #return theSum


#sum = 0
#for i in data_structure:
    #sum += i
    #print(f"Сумма цифр числа"[sum])



#print(data_structure)
#print(len(data_structure))
#print(sum(data_structure[0]))

