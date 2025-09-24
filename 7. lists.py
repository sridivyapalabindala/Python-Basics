# #collection datatypes
# #list
# list1=[1,3,5,7,9]
# list2=[1,2,3,4,5]
# list3=[10,20,30,40,50,60,70]
# fruits=["apple","banana","mango"]
# list4=[True,False,True,False]
# print(list1)
# #indexing
# print(list4[1])
# #by negative values
# print(list3[-1])
# print(list3[-2])

# #slicing

# slc1=["kajal","samantha","anushka"]
# print(slc1[:2])
# print(slc1[1:2])
# print(slc1[-1])

# #adding elements in the list
# #append
# names=["sriivya","tanuu","varuu",]
# names.append("yvvainy")
# print(names)

# #insert
# tvd=["elena gilbert","damon salvatore","stefan salvatore","caroline forbes","klaus mikaelson"]
# tvd.insert(2,"bonnie bennet")
# print(tvd)

# #extending
# st=["steve","max","eleven","lucas","jonathan"]
# st.extend(["mike"])
# print(st)
# #removing elements from the list
# #removing items in the list in different ways
# # 1. remove():removes or deletes the first occurance of specific 
# # 2.pop(): deletes the items from the list at the particular position
# # 3.clear():deletes all items from the list



# #changing the elements

# st=["steve","max","eleven","lucas","jonathan","max"]
# st.remove("max")
# print(st)

# st=["steve","max","eleven","lucas","jonathan","max"]
# st.pop(4)
# print(st)

# st=["steve","max","eleven","lucas","jonathan","max"]
# st.clear(st)
# print(st)



# cars=["thar","audi","jaguar","bmw","l"]

# #index  0   1   2   3   4   5
# for car in range(0,5):
#     print("cars=",car)
    
    
# #using index with for loop:
# a= len(cars) #4
# for i in range(0,a):
#     print("cars",i,car)




# #adding elements using for loop :


# list1=[]
# n=int(input("enter the number of list values:"))
# for i in range(0,n):
#     a=input("enter the list values:")
#     list1.append(a)
# print(list1)

# #give the input values to the list 0 to 10

# for i in range(0,11):
#     list1.append(i)
# print(list1)



# #sum of the list items =10,20,30,40,50 without using sum()

# nums=[10,20,30,40,50]
# sum=0
# for i in nums:
#     sum=sum + i
# print(sum)

# numbers=[10,20,30,40,50]
# product=1
# for i in numbers:
#     product=product*i
# print(product)

# #covert ["p","y","t","h","o","n"] to python

# letters=['y','t','h','o','n']
# sum='p'
# for i in letters:
#     sum=sum+i
# print(sum)

# #find the max and min numbers from list without using max() and min()
# list=[1,2,3,4,5,6,77]
# list.sort()
# print(list)
# print("maximum number from the list",list[6])
# print("minimum number from the list",list[0])

# # using min() and max()
# print(max(list))
# print(min(list))

# #without using above
# for i in range(0,6):
#     max=list[6]
#     min=list[0]
# print("maximum number from the list is",max)
# print("minimum value from the list is",min)

# list=[111,2,3,4,5,6,777]
# max1=list[0]
# min1=list[0]
# for num in list:
#     if num>max1:
#         max1=num
#     if num<min1:
#         min1=num
# print( "max num from list",max1)
# print("min num from list",min1)




# #searching for the element in the list
    
# names=["steve","max","eleven","lucas","jonathan"]
# searching_names=input('enter the name to see if they are in cast:')
# found=False
# for i in names:
#     if searching_names==i:
#         found=True
# if found:
#     print('yes , they are a cast member')       
# else:
#     print("they are not a cast member")

    
    
# numbers=[1,3,5,7,89,0,70]
# #o=5
# #e=2
# even_num=0 #2
# odd_num=0 #1

# for i in range(len(numbers)):
#     if numbers[i]%2==0:
#         even_num+=1
#     else:
#         odd_num+=1
# print("number of even numbers are",even_num)
# print("number of odd numbers are",odd_num)


# # reversing numbers without reverse
# list1=[1,2,3,4,5,6,7,8,9] #l=9
# l=len(list1)
# r_list=[]
# for i in range(l-1,-1,-1):
#     r_list.append(list1[i])
# print(r_list)

# #removing all negative numbers using loop




# #multiply each element in the list
# numbers=[1,2,3,4,5,6,7]
# for i in range(len(numbers)):
#     print("multiple of",i,"is",i*i)
    
# numbers=[1,2,3,4,5,6,7,8,9,10]
# n=int(input("enter the number to be multiplied:"))
# After_multiplication=[]
# for i in numbers:
#     After_multiplication.append(i*n)
# print(After_multiplication)


#count how many positive,negative and zero values are in the list

numbers=[0,1,2,-3,4,-5,6,7,-8,9,10,-11]
positive_num=0 #8
negative_num=0 #4
zero_values=0 #1

for i in range(len(numbers)):
    if numbers [i]>0:
        positive_num+=1
    if numbers [i]<0:
        negative_num+=1
    if numbers [i]==0:
        zero_values+=1
print("number of positive numbers are",positive_num)
print("number of negative numbers are",negative_num)
print("number of zero values are",zero_values)

# list1=[1,2,2,3,4,55,5,6,67,6,7,8,9,5,]
# for i in range(len(list1)):
#     list1.append(list1[i])
# list1.remove([i]==list1)
# print(list1)

'''#writing a program to separate even and odd number into two new lists
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list1=[]
list2=[]
for i in range(len(numbers)):
    if numbers[i]%2:
        
    else:
        list2+=1
print(list1)
print(list2)'''