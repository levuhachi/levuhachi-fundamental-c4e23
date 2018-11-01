#Question 5,6
sheep_list = [5,7,300,90,24,50,75]
print ("Hello, my name is Chi and these are my ship sizes:",'\n',sheep_list)

print("Now my biggest sheep has size", max(sheep_list),". Let's shear it")

max_size_index = sheep_list.index((max(sheep_list)))
default_sheep = 8
sheep_list[max_size_index] = default_sheep
print("After shearing, here is my flock:",'\n',sheep_list)

month = ["Month 1", "Month 2", "Month 3"]
for i in range (len(month)):
        print(month[i])

        for n,j in enumerate(sheep_list):
            sheep_list[n] += 50
        print("One month has passed. Now here is my new flock:",'\n',sheep_list)

        if month[i] != month[-1]:
            print("Now my biggest sheep has size", max(sheep_list),". Let's shear it")
            
            max_size_index = sheep_list.index((max(sheep_list)))
            default_sheep = 8
            sheep_list[max_size_index] = default_sheep
            print("After shearing, here is my flock:",'\n',sheep_list)
        else:
            total = 0
            for k in range (len(sheep_list)):
                total += sheep_list[k]
            print("My flock has size in total:", total)
            money = total * 2
            print("I will get", money,"$")


        
