

My_tuple=(10,20,30)
print(My_tuple)
print(type(My_tuple))


#creating a tuple:
#empty tuple
Et=()
#tuple with numbers:
n=(1,2,3,4,5,67)
#tuple with strings
s=("A","B","C")
#tuples with mixed datatypes
m=(24,2,3,"A","c",True,"false")

#tuple with single element:
a=11
print(type(a)) #int
a=(11)
print(type(a)) #int
a=(11,)
print(type(a)) #tuple
a=[11]
print(type(a)) #list

#accessing elements:
#tuples uses index values to access an element
A=(10,20,30,40,50,60,70)
#i 0, 1, 2 ,3 ,4 ,5, 6
#i -7 -6 -5 -4 -3 -2 -1
print(A[0]) #10
print(A[1]) #20
print(A[2]) #30
print(A[3]) #40
print(A[4]) #50
print(A[5]) #60
print(A[6]) #70
print(A[-6]) #20
print(A[-7]) #10


#slicing the tuple:
#extracts part of the tuple using start index and end index
#([start  index: end index])
A=(10,20,30)
#  0  1   2
# -3 -2  -1
print(A[1:2])  #20,
print(A[0:2]) #10,20
print(A[-3:-1]) #10,20
print(A[-1:-3]) #()


# #changing the values:
# #tuples are immutable.so, we cant change the values.
# A[1]=50
# print(A) #TypeError: 'tuple' object does not support item assignment

# #append
# A.append(50)
# print(A) #TypeError: 'tuple' object does not support item assignment 

# #length
# #max
# #min
# A=(10,20,30)
# print(len(A))
# print(max(A))
# print(min(A))

# #searching names 
# names=("max","eleven","will","nancy","steve")
# searching_names=(input("enter the name:"))
# found=False
# for i in names:
#     if searching_names==i:
#         found=True
# if found:
#     print("yes, they are cast member")    
# else:
#     print("they are not a cast member")
# print(len(names))


