first_name = "  lenox"
last_name = "bett  "
email = "   KERINGLENOX@gmail.com  "
print(len(first_name))
first_name = first_name.title() 
full_name = first_name.title().strip() + ' ' + last_name.title().strip()
email = email.lower().strip()
print(full_name, email,)

#Indexing - To access one character in a string.
print (full_name[4])

# #Slicing - To access multiple characters.
# #First part - index where you want to stop.
# #Second part - index + 1 where you want to stop.
# print(full_name[1:3])

# #Split
split_email = email.split("@")
print(split_email)