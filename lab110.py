# ejercicio  1 tipo cadena
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# concatenacion
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

firstString = "ayuda"
secondString = "me"
thirdString = firstString + secondString
print(thirdString)

#cadema de entrada
name = input("What is your name? ")
print(name)

#dar formato a la cadena de salida
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))