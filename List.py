#--------------------------------------------------------LIST-------------------------------------------------------------------------
#difference between list and arrays
# 1. Lists are built-in data structures in Python, while arrays are provided by the array module.
# 2. Lists can hold items of different data types(hetrogeneous), whereas arrays are typically of a single data type(homogeneous).
# 3. Lists are more flexible and easier to use but slow, while arrays are more efficient and fast for numerical operations.
# 4. Lists store data as references, while arrays store data in a contiguous block of memory.
L1 = []                                     #empty list
L2 = [1, 2, 3, 4, 5]                        #homogeneous list, 1D list
L3 = [1, "two", 3.5, 3+5j, True]            #heterogeneous list
L4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]                                       #2D list
L5 = [1, [2, 3], [4, [5, 6]]]               #3D list
L6 = list("Holaaa")
print("empty matrix:", L1)
print("1D list:", L2)
print("heterogeneous list:", L3)
print("2D list:", L4)
print("3D list:", L5)
print("list from string:", L6)
#list can be use as same as string
print("extract 1st data:", L2[0])
print("extract last data:", L2[-1])
print("extract data:", L2[::-2])

#for 2D list, using another variable, using matrix concept
x = L4[1]
print("extract data in 2d list using variable:", x[2])
print("extract data using matrix:", L4[1][2])

#for 3D list, using another variable, using matrix concept
y = L5[2]
z = y[1]
print("extract data in 3d list using variable:", z[0])
print("extract data using matrix:", L5[2][1][0])

#Edit list
L2[0] = 10                                      #update first element
L2[1:4] = [20,30,40]                            #update last element
L2[-1] = 50                                     #update last element
print("updated list:", L2)
L2.append(60)                                   #add data at last
L2.extend([70,80,90])                           #add multiple data at last
print("after append and extend:", L2)
L2.append([100,110])                            #add list at last
L2.extend("Dhaka")                              #add multiple data at last
print("after append and extend:", L2)
L2.insert(2, "City")                            #add data at anywhere
print("after insert:", L2)
del L2[3]                                       #delete data from anywhere
print("after one data delete:", L2)
del L2[5:8]                                     #delete multiple data
print("after multiple data delete:", L2)
#for getting next outputs make line 57 into a comment
#del L2
print("after delete list:", L2)                 #error, because list is deleted
L2.remove('City')                               #remove data by value, position jani na but delete korte chai
print("after remove 'City':", L2)
print("popped data:", L2.pop())                 #remove last data and return it
print("popped from anywhere:", L2.pop(1))       #remove data from anywhere and return it
print("clear:", L2.clear())                     #remove all data, not delete but empty a list

#operation of lists
L2=[10, 20, 30, 40, 50, 60]
L1.extend([1,2,3,4,5,6])
print("l1+l2:", L1+L2)                          #addition of two list
print("l1*3:", L1*3)                            #repetition of list
print("add of two diff. D list:", L2+L5)        #addition of two different dimensions list
for i in L2:
    print(i)                                    #print 1D list element wise
for i in L4:
    print(i)                                    #print 2D list row wise
for i in L5:
    print(i)                                    #print 3D list row wise

#Functions with Lists
print('length of l2:', len(L2))                 #length of list
print('minimum value of l2:', min(L2))          #minimum value of list
print('maximum value of l4:', max(L4))          #maximum value of list
print('sum of l2:', sum(L2))                    #sum of all elements in list
print('sorted l2:', sorted(L2))                 #sorted list
print('reversed l2:', list(reversed(L2)))       #reversed list
L2.sort()
print("permanent sort:", L2)                    #permanent sort list
L2.reverse()                                    #permanent reverse list
print("permanent reverse:", L2)
print("index of 50 in l2:", L2.index(50))       #index of an element


#Write a code which will capitalize the 1st alphabet in a word
sample = input("Enter a sentence: ")
sample.split()

# Initialize an empty list to store capitalized words
L = []

for i in sample.split():
    # Append the capitalized word to the list L
    L.append(i.capitalize())

# Join the words in the list L back into a single string, separated by a space
print(" ".join(L))