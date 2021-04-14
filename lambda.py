

people = [
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Ginny", "house": "Gryddindor"},
    {"name": "Dumbledore","house":"Gryffindor"}
]

#def f(person):
    #return person["house"]

#people.sort(key=f)

people.sort(key=lambda person:person["name"])

print(people)