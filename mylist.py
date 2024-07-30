# #Display 2 from the list.
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])

#Output James  from the list
print(trainees[1][1][0])

# Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)

# Using a method add the name Mike between James and Mary
train = trainees[1][1]
train.insert(1, "Mike")
print(train)

# Change the value of 2 to 8
trainees[1][0] = 8
print(trainees)

# Remove John and Mary from the list
trainees.remove("John")
trainees[0][1].remove("Mary")
print(trainees)

# Using a function, determine the length of the list
print(len(trainees))