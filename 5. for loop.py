#loop is a program
#for  variable in seq
#code block
#range(start v(0 by default if we dont take) ,end v, step v)
for i in range(1,4):
    print("hello")
for i in range(0,4):
    print("hello")
for i in range(0,6):
    print("i")
for i in range(1,6):
    print(i)
for i in range(9,28):
    print(i)
for i in range(16):
    print(i)
    
for i in range(10,0,-1):
    print(i)
for i in range(0,22,2):
    print(i)
#print squares of a number upto 6
for i in range(0,7):
    print("square of" ,i,"is",i*i)

fruits= ("apple","mango","banana")
for fruit in fruits:
    print(fruit)
fruits="apple"
for i in fruits:
    print(i)

#5th table
for i in range(1,11):
    print("5*",i,"=",5*i)
for i in range(1,11):
    print("8*",i,"=",8*i)
    
#1+2+3+.......+25=? #326
sum=1
for i in range(1,26):
    sum =sum +i
print(sum)

#10 to 6

a=777
for i in range(1,10):
    if i%2 ==0:
        pass
    else:
        print(i)
    

 

