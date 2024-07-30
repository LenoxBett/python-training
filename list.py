my_list = ["bett", "pauline",18, 20, 30.69, 35.6, True, False, ['kevin', 'brian',[1,2,3,4], 'lenox', 'ropy'], "kashkid"]
print(my_list[9])

#accessing elements in a list
#we use indexing
print(my_list[-1])

list1 = [1,2,3,4]
num = [5,6,7,8]
list1.append(5)
print(list1)
list1.copy()
print(list1)

#removing elements
#remove, pop, del
list1 = [1,2,3,4]
list1.remove(3) #remove a specific element
list1.pop(0) #remove a specific index
del list1(2) #delete
list1.clear() #clears elements in a list
list = list1.copy() #copies the specified list
list = [5,6,7,8] 
print(list.count(1))
list1.extend(list) #extends the list with another
list1.index(4) #display the index of an element
list1.insert(0, 122) #inserts an element to a specified index
list1.sort() #sorts elements in order
list1.reverse()#reverses a list
print(list1)