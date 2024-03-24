#element inside of list is a dictionary 
people = [
    
    {"name":"Harry", "house":"Gryffi"},
    {"name":"cho", "house":"Ravenclaw"},
    {"name":"Draco", "house":"Slytherin"},
]

# def f(person):
#     return person["house"]
# people.sort(key=f)


people.sort(key=lambda person: person["name"])

print(people)