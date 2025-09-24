#Error_Handling
#1.Zero_divisions error
# try:
#     a=int(input("enter the numerator:"))
#     b=int(input("enter the Dinominator:"))
#     c=(a/b)
#     print(c)
# except ZeroDivisionError:
#     print("Error:division by zero in the dinominator is not possible ")
    


# try:
#     i=25
#     n=int(input("enter the n value:"))
#     if i%n==0:
#         print("yes,number is multiple of",n)
#     else:
#         print("No,number is not multiple of",n)
# except ZeroDivisionError:
#     print("Error:division by zero in the dinominator is not possible ")    

# # 2.ValueError
# try:
#     rollno=int(input("enter your rollno:"))
# except ValueError:
#     print("Error:Given value is not in the integer datatype")

#3.IndexError
# try:
#     list=[10,20,30,40,50,60,70]
#     n=int(input("enter the index value:"))
#     print(list[n])
# except IndexError:
#     print("Error:the given index is not in the list")

# #keyError:
# try:
#     Dict={"name":"sri","rollno":"p0"}
#     print(Dict["name"])
#     print(Dict["age"])
# except KeyError:
#     print("Error:the given key is not in the list")

# #TypeError:
# try:
#     list=[10,20,30]
#     sum="5"+5
#     print(sum)
# except TypeError:
#     print("invalid type operation")

# #nameError:
# try:
#     print(Mult)
# except NameError:
#     print("variable not declared")


#FileNotFoundError:
#example1
try:
    file=open("details.txt")
    print(file.read())
except:
    print("file not found in the system")
finally:
    print("program is executed")


#example2
try:
    file=open("students.txt")
    print(file.read())
except:
    print("file not found in the system")
finally:
    print("program is executed")






