
import math


#lists
""""
marks = []

marks.append(19)
print(marks)
marks.append(30)
print(marks)

print(marks[0])

for i in marks:
    print(i)

history = ["mughal","british"]
history.append("maratha")
print(history)
history[0] = "gupta"
print(history)

def square(num):
    return num*num

print(square(6))

def square_root(num):
    return math.sqrt(num)

print(square_root(49))

 

try:
    my_variable = float(input("enter a num"))
    print(f"you entered {my_variable}")
    print(f"square is {my_variable*my_variable}")

except:
    print("error enter a valid num")
"""

#dictionaries
student = {
}
student["name"]= "Bhumika"
student["name"]= "Anish"
print(student["name"])
student["age"]=20

if  "name" in student:
    print("name exists")

for key in student:
    print(key)

for value in student.values():
    print(value)


dataset = {
    "age":[20,21,22],
    "marks":[90,80,70],
    "passed":[True,False,True],

    }

book = {
    "title":"anish is a retard",
    "author":"Bhumika",
    "price":0,

}

book["price"]= "20"

print(book["price"])