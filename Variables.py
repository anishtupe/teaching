#basic varible types
age = 20 
height = 5.8
name = 'Bhumika'
is_student = True

print(age)
print(name)

#list
marks = [66,80,90,95]
print(marks[0])
marks.append(100)
marks[1]= 88
print(marks[1])
print(marks)
#tuple 
coordinates =  (20,5)

student = {
    "name": "Bhumika",
    "age":20,
    "branch":"Extc"
}
 
print(student["name"])

x = 10 #int
y = 4.9 #float

x = int(y)

print(x)

city = "Mumbai"  #string
city2 = "pune"

print(city.lower())
print(city.upper())
print(city.strip())
print(city + " " +city2)

 

a = float(input("enter num1"))
b = float(input("enter second num"))

print(a+b)

anish = "idiot"
print (f"nish is a {anish} ")