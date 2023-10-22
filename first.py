#!/bin/python3

def nl():
	print("\n")

#MATH
print (50%6) #modulo - for remainder
print (50/6) #division- may give float values
print (50//6) #gives integer ans and trims decimal and values after decimal

nl()

#VARIABLES AND METHODS
st = 'tEst sTrINg'

print(st)
print(st.upper()) #uppercase
print(st.lower()) #lowecase
print(st.title()) #titelcase (first letter capital of every word)
print("len(string): " + str(len(st))) #we can't concatenate an int with string so convert the int to string with str() method and then concatenate

nl()

#TUPLES
t = ("a","b","c","d")
print(t[1])

nl()

#LOOP
l = ["a","b","c","d"]
for i in l:
	print(i,end=" ")
	
nl()

#ADVANCED STRING
sen = "This is a sentence"
sen2 = ["Hola","amigos","!"]
sen3 = "This is a sentence"

print(sen.split()) #delimeter - default is space
print(' '.join(sen2))
print(sen3.split("s"))

too_much_space = "         hello        "
print(too_much_space.strip())
print(too_much_space.lstrip())
print(too_much_space.rstrip())
print(sen[:6])

name = 'arb'
age = 23
print("The name is {} and the age is {}.".format(name,str(age)))
print("The name is %s and the age is %d." %(name,age))
print(f"The name is {name} and the age is {age}.")

nl()

#DICTIONARY
d1 = {"sad":1,"df":2,"dfcvcv":3}
d2 = {"Movie":["Spiderman","Iron Man"], "Series":["Mr.Robot","The Witcher"], "Shows":["Larva","HIMYM"]}

print(d1)
print(d2)

print(d1.get("sad"))

d1["legal"] = "not"
print(d1)

d2.update({"Anime":["Mha","One piece"]})
d1.update({"Anime":["Mha","One piece"]})
print(d1)
print(d2)

d1["df"] = 8
print(d1)
	
	
	
	
	
	
	
	
	
