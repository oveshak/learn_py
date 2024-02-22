print("'hello world'")
'''print("hello world")
print("hello world")
print("hello world")'''
# print("hello world")
# print("hello world")

#variable in python

a=3
a=6
b=a
b=8
print(a)
print(b)
a=6.4
print(a)

c=True #false -->thsese are boolean variable

d= "ove" #string lakhar somay " " dita hoba 
print(d)

e=None #None is a datatype
print(e)

#module 2 type 1 built-module 2 user-defined module
#PIP holo package install process
he_11="hi"
print(he_11)

# int type data

# type use kora variable ta kon data type aca sata buja jaba 

hablu =420
print (type(hablu))

x = 20.5
print(type(x))

x = 20.5j
print(type(x))


# str type data

# python use kora user kach thaka data naor somay oi ta by defalt string hoy

yourName="ove"
print(type(yourName))

MyName="Eshan"

print("My Name is "+ MyName)

# bool data type
x = False

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x=8
y=10
print(x>y)

# string formatting

num1=30
num2=40

print(f"this is my supper number {num1+num2}")

MyName="Eshan"

print(f"My Name is {MyName} & my class roll is {num1}")

# binary type data

# memory view
# byte 
# byte rage 0-255
# byte always cannot change
# image niya kaj korar jono byte use kora hoy
habluList=[1,2,3,4,5,6,255]
b= bytes(habluList)
print((b))
print(type(b))

# ai vaba change kora jaba na
# b[0]=10 
# print(())

# bytearray
# bytearray always can change
# bytearray rage 0-255
habluList=[1,2,3,4,5,6,144]
b= bytearray(habluList)
print((b))
print(type(b))
b[1]=100;
print(b);
print(b[1]);

# none type data
# the None keyword is used to define a null value or no value at all. None is not same as 0 or an empty string

x=None
print(x)
print(type(x))
x=" " # this is not a none type
print(type(x))

# Sequence Types:

# list type data
# list is always can be change
li=["ove","toton","raj"]
li[0]="dipto"
print(li)
print(type(li))

# tuple type data
# tuple can not be change
x = ("apple", "banana", "cherry")
# x[0]="ove"  tuple can not be change
print (x)
print (type(x))

# range type data
ran =range(6)
for i in ran:
    print(i)

# operator

# floor division
    # floor division use kora vag fol ar por ja dosomik sonkha ta kata fala
    sum1=15
    sum2=7
    print(sum1//sum2)


#swapping
    c=60
    d=50
    c,d=d,c
    print(c)
    print(d) 

    # user input

    # username = input("Enter username:")
    # # passwoard=input("enter your passworad  " )

    # print(username)


# list data add
    # append
    hablu1=[1,3,54,6,7,8,9]
hablu1.append(10)
print(hablu1)
# insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i)
# Using a While Loop
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#   List Comprehension
  
  list=[1,2,3,4,5,6]
  double=[i*2 for i in list]
  print(double)

  thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)