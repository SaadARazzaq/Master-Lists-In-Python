import os
import time as t
print()
print("\t\t***Python Program starting shortly...***")
print()
# There are mostly 11 types of list methods
t.sleep(1.5)
# 1) Append(): This method Adds a value to the end of the List. append() method takes exactly one argument

print()
print("<---------------1) append() method---------------->")
print()

append_list = [1,2,3,4] # append_list named List created
print("List created has values: ",append_list)
append_list.append(5) # Adds 5 to the end of the List
print("List after appending 5 is: ", append_list) # Prints the list

# if I write this syntax: print(list.append(5)) then it will print none as its not worth using this syntax

# using for loop to append as many values as I want
var = int(input("Enter How many more values you want to append: "))
for i in range(var):
    print("Enter element", end=": ") # end= ignores endline after print message
    a = int(input())
    append_list.append(a)

print("Final List after appending user values is: ", append_list)

# 2) Clear(): This method clears all the values previously entered in the list. 
# clear() method takes no argument i.e. must be empty inside the clear() parenthesis
t.sleep(3)
print()
print("<---------------2) clear() method---------------->")
print()

print("Previous list is: ", append_list) # Prints Previous list
append_list.clear()
print("Previous list after clearing: ", append_list)
append_list = [11,12]
print("New values inside list: ", append_list)

# 3) Copy(): This method copies all the values of one list 
# to the other list and deletes any values that are already 
# present inside that victim list(the one list in which we want to copy list values). 
# There must be no argument inside copy()
t.sleep(3)
print()
print("<---------------3) copy() method---------------->")
print()

copy_list = [1,2,3,4]
victim_list = [7,8,9]

print("Original List: ", copy_list)
print("Old values of victim List: ", victim_list)

victim_list = copy_list.copy()
print("New values of Victim list: ", victim_list)
print("*Notice all the prev values have been deleted and new values are copied to it")

# 4) count(): This method counts that how many times a certain element has come in a list. 
# There must be one argument passed to this method and that argument must be present inside 
# the list otherwise it will throw error.
t.sleep(3)
print()
print("<---------------4) count() method---------------->")
print()

count_list = [1,1,2,2,2,3,4]
print("List values are: ", count_list)
for i in range(4):
    print(f"Number of times {i+1} has come in list",end=": ")
    print(count_list.count(i+1))

# 5) extend(): Appends one list to the other list and not just deletes the previous list like the copy() method. 
t.sleep(3)
print()
print("<---------------5) extend() method---------------->")
print()

listToBeExtended = [5,6]
combined_list = [1,2,3]
print("List to be extended is: ", listToBeExtended)
print("List to which the other list will be extended is: ", combined_list)
combined_list.extend(listToBeExtended)
print("Combined List is: ", combined_list)

# 6) index(): This is used to find out location of a certain element in a given list.
#  Returns the index of that element in the list... 
# NOTE: The element you will pass in index() method must be present in the list otherwise
#  it will give error and also THERE MUST BE EXACT ONE ARGUMENT PASSED IN INDEX METHOD
t.sleep(3)
print()
print("<---------------6) index() method---------------->")
print()

listIndex = ["Saad","Taha","Wasif"]  # This list created for index method only
print("List has Values: ", listIndex)
var1 = listIndex.index("Saad")
print("Location of Saad in list is: ", var1)
var2 = listIndex.index("Taha")
print("Location of Taha in list is: ", var2)
var3 = listIndex.index("Wasif")
print("Location of Wasif in list is: ", var3)

# 7) insert(): This is used to insert an element on a specific index of a list. 
# If there is no argument passed to insert method then it will throw error.
t.sleep(3)
print()
print("<---------------7) insert() method---------------->")
print()

listInsert = ["car", "motorcycle", "train"]
listInsert.insert(1, "Bike") # insert(pos, value). Here 1 is the index where you want to insert and "Bike" is the element you want to insert so insert(1,"Bike") is written
print("\t--List with element Bike inserted on 'one' index--")
print("The new List is: ", listInsert)
print()
listInsert.insert(10000, "Helicopter") # If the number is too large than the length of list, then the element is inserted on the end of list
print("\t--List with element Helicopter inserted on last index--")
print("The new List is: ", listInsert)
print()
listInsert.insert(-10000, "Cycle") # If the number is too small than the length of list, then the element is inserted on the start of list. 
                                   # Here '-10000' is not a real index number and index number always starts with '0' so element will be inserted on '0' index regardless of what small value is.
print("\t--List with element Cycle inserted on 'zero' index--")
print("The new List is: ", listInsert)

# 8) pop(): Pops last element of list
t.sleep(3)
print()
print("<---------------8) pop() method---------------->")
print()

listPop = ["Saad", "Abdur", "Razzaq", "has", "writen", "this", "code"]
print("Original list is: ", listPop)
listPop.pop() # Pops last element "code" because no index passed to it
print("List after popping last element: ", listPop)
listPop.pop(0) # Pops element present at zero index. Can pop elements at any index. 
               # Cannot pop elements that are out of range of list i.e. element at index '82732738' 
               # can not be popped as the list has no such length.

print("List after popping first element: ", listPop)
print("The element that was recently popped is: ", listPop.pop(0)) # printing listPop.pop(0) will print the element that is popped
print("Final List is: ", listPop)

# 9) remove(): Removes a specific element from the list. 
# THERE MUST BE ONLY ONE ARGUMENT INSIDE THE remove() 
# AND THAT ARGUMENT MUST BE THE ELEMENT THAT IS PRESENT IN THE LIST.
t.sleep(3)
print()
print("<---------------9) remove() method---------------->")
print()

listRemove = ["This", "is","a","remove","list"]
print("List before removal: ", listRemove)
listRemove.remove("remove")
print("List after removal: ", listRemove)

# 10) Reverse(): This method Reverses the whole list. There must be no argument passed inside this method
t.sleep(3)
print()
print("<---------------10) reverse() method---------------->")
print()

listReverse = [1,2,3,4,5]
print("Original list: ", listReverse)
listReverse.reverse()
print("Reversed list: ", listReverse)

# 11) Sort(): This method sorts list in asscending to descending order or in alphabetical order
t.sleep(3)
print()
print("<---------------11) sort() method---------------->")
print()

listSort = [9,2,4,1,7]
print("Original list: ", listSort)
listSort.sort()
print("Sorted list: ", listSort)

print()
listSort2 = ["zahid", "ghazal", "babar", "afzaal", ]
print("Original list: ", listSort2)
listSort2.sort()
print("Sorted list: ", listSort2)