

names = [
    {"name": "Ramen", "number":9996986997, "address":"Hattigauda", "distance":1.98},
    {"name": "Ramyun", "number":898687587, "address": "Bansbari", "distance": 1.9},
    {"name": "Samyung", "number":8986959598, "address":"Chakrapath", "distance":2.7}
]

vista = {"name":"Shyam", "number": 707085868 , "address":"Gangalal", "distance":1.88}

names.append(vista)

list_of_distance = []

my_address = 0
for name in names:
    if "distance" in name:
        x = name.get("distance")
        list_of_distance.append(x)
        name_of_the_person = list_of_distance.index(x)


        print("The shortest distance is", min(list_of_distance))
        print(names[name_of_the_person])
        break
    else:
        pass








