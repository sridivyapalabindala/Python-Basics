# types of files():

# #1. read()

file=open("students.txt","r") 
content=file.read()
print(content)
file.close()

# #2. readline()

file=open("students.txt","r")
content=file.readline()   #1st line
content1=file.readline()   #2nd line
content2=file.readline()   #3rd line
print(content)
print(content1)
print(content2)
file.close()


# file= open("students.txt","w")
# #write,writelines
# file.write("Hello c++\n")
# file.write("Hello python\n")
# lines=["Hello sri\n","Hello sridivya\n","Hello world\n","Hello python\n"]
# file.writelines(lines)
# file.close()


file= open("students.txt","a")
file.write("Hello c++\n")
text=b"hello sri"
file.close()
