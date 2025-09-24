#arrays in python
#an array is collection of elements of the same datatype stored in continuos memory location.
#arrays are used to store multiple values in a single variable
#why arrays...?
#easy to manage multiple values
#allow faster operations like searching and sorting
#useful in mathematics and scientific problems
#saves memory
#array VS lists


#import array as module
import array as arr


#creating an array
Numbers=arr.array('i',[1,2,3,4,5,6])
print(type(Numbers))
print(Numbers)

#integer=i
#float=f
#string=u

#accessing array elements
print(Numbers[0])
print(Numbers[4])
print(Numbers[-1])

#adding an element in array
Numbers=arr.array('i',[1,2,3,4,5,6])
#append():
Numbers.append(7)
print(Numbers)

#insert():
Numbers.insert(8,2)
print(Numbers)

#extend();
Numbers.extend([1,2])
print(Numbers)


#deleting an element
Numbers=arr.array('i',[1,2,3,4,5,6])


Numbers.remove(6)
print(Numbers)
Numbers.pop(3)
print(Numbers)
# Numbers.clear()  
# print(Numbers)

#looping through arrays
for i in Numbers:
    print(i)
    
#basic operations in array
print(len(Numbers))
print(max(Numbers))
print(min(Numbers))



