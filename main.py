programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}


"""Dictionaries consist of set of keys and values in form of 
{Key: Values}, so in upper example, dictionary called programming_dictionary has two objects-> Bug is the key, and its value is definition of the key... same with FUNCTION and its definition. ALL SEPARATED WITH COMMA"""

popis_djelatnika={
  "Kruno":"Teacher of Mathematics and Informatics",
  "John":"Principle of School",
  "Mike":"Counselor",
  123: "Robot number",
}

#calling in dictionary elements:

print(popis_djelatnika["Kruno"])
print(popis_djelatnika[123], end="\n")

#adding items to dictionary

popis_djelatnika["Angela"]="Librarian"
print(popis_djelatnika)

#creating empty dictionary is like with list
empty_list=[]
empty_dictionary={}

#wipe the existing dictionary
programming_dictionary={}
print(programming_dictionary)

#edit an item in dictionary:
popis_djelatnika[123]="More data needed."
print(popis_djelatnika)

#Loop thrugh dictionary:
for item in popis_djelatnika:
  print(item)  #prints keys
  print(popis_djelatnika[item])