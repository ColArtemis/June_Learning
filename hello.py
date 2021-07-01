#The first code a simple Hello
print ("Hello, world!")
#input function
name = input("Name: ")

print ("Hello, " + name)
#formatted strings
print (f"Hello, {name}")
#conditions
n = int (input ("Number: ")) #make sure to call an integer or you'll have an error
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is Zero")

m = input("Are you done? Y/N: ")
#sequencing
name = "Harry"

print(name[0])

name2 = ["Harry", "Hermione", "Ron"]
print(name2)
print(name2[0])
m = input("Are you done? Y/N: ")

coordinatex = 10.0
coordinatey = 20.0
coordinate = (10.0, 20.0)
