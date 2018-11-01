#person = ["H.Chi", "Ha Noi", "BA", 20, 8, 198, False]
# person = {}
# print(person)
# print(type(person))

# person = {
#     "name":"H.Chi"
# }
# print(person)
# print(type(person))

person = {
    "name":"H.Chi",
    "location":"Ha Noi",
    "age":20,
}
# print(person)
# person["friend_count"] = 257 #[<key>]=value
# print(person)  
# person["age"]+=1 -- update
# del person["age"] -- delete
key = "school"
if key in person: #if the key user inputted is within person dict
    print(person[key])
else:
    print("Not found")