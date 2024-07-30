#creatina a dictionary
my_dictionary = {
    "name": "Lenox",
    "age":20, 
    "city": "Nairobi",
    }
#accessing values using keys

print(my_dictionary["name"])
print(my_dictionary["age"])
print(my_dictionary["city"])

#modifying values
my_dictionary["name"] = "bett"
my_dictionary["age"] = "21"
my_dictionary["city"] = "nakuru"
my_dictionary["address"] = [101, "kiambu"]

#display kiambu
print(my_dictionary["address"][1])

#adding elements to a dictionary
my_dictionary["occupation"] = "doctor"
my_dictionary["email"] = "keringlenox@gmail.com"
print(my_dictionary)

#used to display keys in the dictionary
print(my_dictionary.keys())

#used to display values in the dictionary
print(my_dictionary.values())

#used to display all
print(my_dictionary.items())

#checking if a key is in a dictionary we use the in operator
print("city" in my_dictionary)
print("occupation" in my_dictionary)

