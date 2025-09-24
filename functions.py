#functions
#A function is a block of  code that performs a specific task
#it allows us to group instructions together and reuse them whenever needed
#instead of writing the same code again and again, we can just define a function once and call it whenever needed
#SYNTAX:
# def function_name(parameters):
#     #function body code
#     return value #optional
# function_name()





#example
def greet():
    print("hello world!")    
#calling a function:
# calling a function means telling python to run the code inside a function by using its name followed by the parantheses()
#if the function needs input(parameter) ,we provide values (arguments) inside the parantheses
#when we call a function ,python jumps to the function, executes its code, and then comes back to continue the program
def greet():
    print("hello world!") 
greet()
greet()
greet()
def greet(name,branch):  #function name
    print("hello world!",name,branch) #
greet("sri","cse-aiml")                 #calling a function


#passing parameters and arguments
#parameters:A variable declared  inside the function definition
#it acts like an empty container waiting to receive a value
#arguments: the actual value we pass into  the function when calling it.it falls the empty container(parameter).
#example
def greet(name):  #name=parameter
    print("hello",name)
greet("sri")

#same task without function
name="sri"       #here name is input variable (parameter),and"sri" is value to the parameter(argument)
print("hello",name)

#types of functions arguments
# A.positional arguments:
#when we pass arguments in the same order as the function parameter,they are called positional arguments.
#here the order (position) is very important

def greet(rollno,name):  #step2:values store
    print("hello",name,",","your rollno is",rollno)
greet("p0","sri")        #step1:function calling


# B.keyword arguments:
#when we pass values or arguments by writing the parameter (variable=value),they are called as keyword arguments.
def greet(rollno,name):
    print("hello",name,",","your rollno is",rollno)
greet(name="sri",rollno="p0")

#C.default arguments
#when a parameter has default value(assigning the value in the parameter) in the function definition, it becomes a default argument
#argument.
def greet(name="student"):
    print("hello",name)
greet()
greet(name="sri")


#D.variable-length arguments
#sometimes we dont know how many arguments will be passed to a function
#python provide two special ways to handle this:
#1.*args:(variable-length arguments):
#collect multiple values in tuple

#L=10,20,30,40,50,60,70
def sum1(*list1):
    sum2=0
    for i in range(len(list1)):
        sum2=sum2+list1[i]
    print(sum2)           #280
    print(type(list1))     #tuple
sum1(10,20,30,40,50,60,70)
#2.**kwargs : (keyword variable-length arguments)
#collects multiple key-value pair into  a dictionary
def details(**info):
    for i,j in info.items():
        print(i,":",j)
details(name="sri",rollno="p0",branch="csm")





#scope of the variable
x=10 #global variable
def var1():
    x=5 #local variable
    print("inside var1 function",x)
var1()
def var2():
    print("inside var2 function",x)
var2()





