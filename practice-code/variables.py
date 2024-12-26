myint=5
myfloat=9.8
mystr="ash"
mybool=True
mylist=[0,1,"two",7.4,False]
mytuple=(0,1,2)
mydict={"one":1,"two":2}

# # print(myint)
# # print(myfloat)
# # print(mystr)
# # print(mybool)
# # print(mylist)
# # print(mytuple)
# # print(mydict)

myint=123

# print(mylist[1:5])
# print(mylist[1:5:2])
# print(mylist[::-1])
# print(mydict["one"])
# print("string type"+ str(123))

def someFunction():
    global mystr
    mystr="def"
    print(mystr)

someFunction()
print(mystr)
