#numpy
#numpy(numerical python) is a python library used for scientific and mathematical computing
#it provides:
##powerful array objects(more effective than python lists)
##vectorized operations (fast element wise calculations)
##support for linear algebra,statistics ,random numbers operations etc..


#importing numpy library
import numpy as np

#creating an array with numpy
#1d array
A1D=np.array([1,2,3,4,5])
print(A1D)                               # [1 2 3 4 5]

#2D array
A2D =np.array([[1,2,3],[4,5,6],[7,8,9]])
#[
#   1,2,3
#   4,5,6
#   7,8,9
#]
print(A2D)                                #[[1 2 3]
#                                         #[4 5 6]
#                                         # [7 8 9]]


#methods and operations in numpy arrays                                                              

#1. basic array information method
A=np.array([1,2,3,4,5])
#ndim:returns the number of dimensions of array
print(A.ndim)                  
print(A2D.ndim)                
#shape :returns a tuple showing the sizes of the array in each dimensions(rows,columns,etc)
print(A.shape)                 
print(A2D.shape)              
#size:returns the total no.of elements in the array
print(A2D.size)               
print(A.size)                   
#datatype:returns the datatype of the elements in the array
print(A2D.dtype)              

'''output
1
2
(5,)
(3, 3)
9
5
int64
'''
#2. creating an array with numpy
#zeros :creates an array with 7 zeros
print(np.zeros(7))    #
#ones :creates an array with 7 ones
print(np.ones(7))
#arange : creates an array from 1->10 based on range
print(np.arange(1,11,1))
print(np.arange(1,11,2))
print(np.arange(0,11,1))
print(np.arange(0,11,2))
print(np.arange(0,11,3))
#linspace:creates 3 numbers evenly space between 0 and 1
print(np.linspace(0,1,3))

'''output
[0. 0. 0. 0. 0. 0. 0.]
[1. 1. 1. 1. 1. 1. 1.]
[ 1  2  3  4  5  6  7  8  9 10]
[1 3 5 7 9]
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 0  2  4  6  8 10]
[0 3 6 9]
[0.  0.5 1. ]
'''


#mathematical operations
A=np.array([1,2,3,4,5,6,7])
L=[1,2,3,4,5,6,7]

print(A+0)
print(A+7)
print(A+5)

print(A-5)
print(A*5)
print(A/5)
print(A**5)
print(A//5)

''' output
[1 2 3 4 5 6 7]
[ 8  9 10 11 12 13 14]
[ 6  7  8  9 10 11 12]
[-4 -3 -2 -1  0  1  2]
[ 5 10 15 20 25 30 35]
[0.2 0.4 0.6 0.8 1.  1.2 1.4]
[    1    32   243  1024  3125  7776 16807]
[0 0 0 0 1 1 1]
'''

#aggregate functions
A=np.array([1,2,3,4,5,6,7])
#sum()
print(np.sum(A))
#mean()
print(np.mean(A))
#max()
print(np.max(A))
#min()
print(np.min(A))
#median
print(np.median(A))
#standard median
print(np.std(A))
#cumprod
print(np.cumprod(A))

'''output
28
4.0
7
1
4.0
2.0
[   1    2    6   24  120  720 5040]


'''


#matrix operations:
Mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# [
#   1,2,3
#   4,5,6
#   7,8,9
# ]
Mat2=np.array([[9,8,7],[6,5,4],[3,2,1]])
#   9,8,7
#   6,5,4
#   3,2,1
print(Mat1*Mat2)
print(Mat1+Mat2)
print(Mat1-Mat2)
print(Mat1/Mat2)

#dot()
print(np.dot(Mat1,Mat2))
#transpose
print(np.transpose(Mat1))


'''output
[[ 9 16 21]
 [24 25 24]
 [21 16  9]]
[[10 10 10]
 [10 10 10]
 [10 10 10]]
[[-8 -6 -4]
 [-2  0  2]
 [ 4  6  8]]
[[0.11111111 0.25       0.42857143]
 [0.66666667 1.         1.5       ]
 [2.33333333 4.         9.        ]]
[[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]
[[1 4 7]
 [2 5 8]
 [3 6 9]]

'''




