#VARIABLES
name = "John Cena"
number = 12

#LOOPS
#FOR LOOP
for i in range(4):
    number += 1
    print(number)

print("******************")

#WHILE LOOP
while number < 20:
    number += 1
    print(number)
    #CONDITIONALS
    if number%2 == 0:         
        print("even!")
    else:
        print("odd!")

#FUNCTIONS
def greeting():
    print("Hello!")

greeting()

def addition(n1, n2):
    return n1+n2

print(addition(number, number))    

sum = addition(number, number)
print(sum)