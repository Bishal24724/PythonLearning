import json

#if you have json item then you can prase it in python using json.loads()
x =  '{ "name":"Bishal", "age":26, "city":"Butwal"}'

y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

#if we want to convert dict into json then

a=json.dumps(y)

print(a)