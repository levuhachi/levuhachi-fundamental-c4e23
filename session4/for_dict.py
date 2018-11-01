person = {
    "name": 'Ha Chi',
    "age": 20,
    "city": 'Ha Noi',
}

# for k in person.key(): #tuple ~= list
#     print(k,person[k])
# for v in person.values():
#     print(v)

for k, v in person.items():
    print(k,v)