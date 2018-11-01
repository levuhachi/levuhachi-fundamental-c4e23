#Question 1,2,3,4
sheep_list = [5,7,300,90,24,50,75]
print ("Hello, my name is Chi and these are my ship sizes:",'\n',sheep_list)
print("Now my biggest sheep has size", max(sheep_list),". Let's shear it")

max_size_index = sheep_list.index((max(sheep_list)))
default_sheep = 8
sheep_list[max_size_index] = default_sheep
print("After shearing, here is my flock:",'\n',sheep_list)

for n,i in enumerate(sheep_list):
    sheep_list[n] += 50
print("One month has passed. Now here is my new flock:",'\n',sheep_list)
