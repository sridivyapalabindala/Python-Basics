#sets
#syntax:
#My_set={element1,element2,element3}

My_set={10,20,30}

#characteristics of sets
#unordered
#example: {1,2,3} and{3,2,1} are considered same sets
#un indexed:
#you cannot access set elements by the index like lists or tuple.set[1]
#example:
'''print(My_set[1])'''                           #TypeError: 'set' object is not subscriptable

#unique values only:
a={1,2,3,3,4,4,5,6,7,8,9}
print(a)                                          #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(len(a))                                     #9

#creating a set:
s1={1,2,3}
s2={1,23,6,7,True,"false"}
#empty
s3={}
s4=set()
print(type(s3))
print(type(s4))

#accessing elements
#we cannot directly access an element using index but we can access an elements using loops
A={"dogs","cats","pigeon"}
for Role in A:
    print(Role)
#adding an element in sets
s={1,2,3,4,5,6,7}
s.add(23)                  #adding only one element in any position
s.update([2,74,8])         #adding multiple elements in the set
print(s)                   #{1, 2, 3, 4, 5, 6, 7, 8, 74, 23}



#deleting the elements in the set
s={1,2,3,4,5,6,7,8,9,9,9}
s.remove(9)                                     #gives key error if we give the element which is not in the set
print(s)    #{1, 2, 3, 4, 5, 6, 7, 8}


#discard
s={1,2,3,4,5,6,7,8,9,9,9}
s.discard(9)                                  # does not gives key error even if we give the element which is not in set
print(s)      #{1, 2, 3, 4, 5, 6, 7, 8}

#pop                                           #removes random element from the set
s={1,2,3,4,5,6,7,8,9,9,9}
s.pop()                                     
print(s)   

#clear              #removes every elements from the set
s={1,2,3,4,5,6,7,8,9,9,9}
s.clear()                          
print(s)            #set()

#mathematical  operations in set         
# #using symbols
#union : prints all elements from both a and b except for the common ones

a={1,2,3,4,5} 
b={5,6,7,8,9,10}
print(a|b)                  #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#intersection :  prints only the common ones

a={1,2,3,4,5} 
b={5,6,7,8,9,10}
print(a&b)               # {5}

#difference           

a={1,2,3,4,5} 
b={5,6,7,8,9,10}
print(a-b)                    #{1, 2, 3, 4}
print(b-a)                    #{6, 7, 8, 9, 10}

#symmetric difference

a={1,2,3,4,5,10} 
b={6,7,8,9,10}
print(a^b)                   #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#using methods
#union
a={1,2,3,4,5} 
b={5,6,7,8,9,10}
print(a.union(b))
#intersection
a={1,2,3,4,5} 
b={5,6,7,8,9,10}
print(a.intersection(b))
#difference
a={1,2,3,4,5} 
b={5,6,7,8,9,10}
print(a.difference(b))
print(b.difference(a))
#symmetric difference
a={1,2,3,4,5,10} 
b={6,7,8,9,10}
print(a.symmetric_difference(b))



a={1,2,3,4,5} 
print(len(a))
print(sum(a))
print(max(a))
print(min(a))


a={1,2,3,4,5,10} 
