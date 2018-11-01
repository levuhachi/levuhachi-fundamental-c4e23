s_list = [
    {
        'name':'Huy',
        'hours':30,
        'salary':50,
    },
    {
        'name':'Quan',
        'hours':20,
        'salary':40,
    },
    {
        'name':'Duc',
        'hours':15,
        'salary':35,
    }
]
print(s_list)
# for i in s_list:
#     print(i)
allbudget = 0
for j in range(3):
    sumofsalary = s_list[j]['hours'] * s_list[j]['salary']
    print(sumofsalary)
    allbudget += sumofsalary 
    print(allbudget)
    
