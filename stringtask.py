#quiz 1
name = ' JOHn .'
name = name.replace(".","")
name = name.strip().lower().capitalize()
print(name)

#quiz 2
sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:-32])

#quiz 3
dog = "The lazy dog; ran so fast; it hit the wall."
split_dog = dog.split(";")
print(len(split_dog))

#quiz 4
first_name="  Joh.n"
first_name = first_name.replace(".","")
last_name="   Do,e"
last_name = last_name.replace(",","")
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)

#quiz 5
r = '["E","W","C"]' 
r = ''.join(filter(str.isalpha,r))
print(r)

