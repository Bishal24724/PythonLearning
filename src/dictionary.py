thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(x)

#this is also can be used using .get() method

print(thisdict.get("model"))

#to get all keys
print(thisdict.keys())

#to change dictionary value

thisdict["year"] = 2019
print(thisdict.get("year"))

#we can update by

thisdict.update({"year":2020})
print(thisdict.get("year"))


#add new item
thisdict["color"] = "red"

print(thisdict)


#remove 
thisdict.pop("model")
print(thisdict)

a = 200
b = 33
if b > 20:
  print("b is greater than a")

else:
  print("a is greater than b")
     
day=4
 
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  def myfunction():
    print("THis is function")

myfunction()
# Python, mutability refers to the ability of an object to be modified after it is created without changing its unique identity
#  (memory address). 
# Objects whose value can be changed in place are called mutable,