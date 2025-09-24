#Biodata
BioData={
    "name":"sridivya",
    "roll_no":"p0",
    "branch":"csm",
    "place":"jagathgirigutta"
}
print(BioData)

BioData=dict(name="sri", roll_no="p0",branch="csm",place="jagathgirigutta")

print
#loops for dictionary:

#loops using lists







#loops to iterate the keys(by default the dictionary's will store the key values)
BioData={
    "name":"sridivya",
    "roll_no":"p0",
    "branch":"csm",
    "place":"jagathgirigutta"
}
for i in BioData:
    print(i)
#loops to iterate the values using values() method:
for i in BioData.values():
    print(i)
#loops to iterate the items using items() method:
for i in BioData.items():
    print(i)
#loops to iterate the keys using keys() method:
for i in BioData.keys():
    print(i)


#nested tuple:
t=(10,(20,30),(40,50))
#i  0,    1   , 2
print(t[2][1])
print(t[1])


#nested dictionary

students={
    "S1":{"Name":"Sridivya","Rollno":"p0"},
    "S2":{"branch":"csm","place":"jagathgirigutta"}
}
print(students["S1"])
print(students["S1"]["Name"])

