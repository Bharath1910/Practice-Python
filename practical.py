import math as m

#Write a simple Python program to print a message.
print("Hello World")


#Write a program to find the sum of two numbers
a = int(input("Enter 1st digit: "))
b = int(input("Enter 2nd digit: "))

print("Sum of two digits is",a+b)


#Write a program to calculate average of n numbers.
digits = int(input("How many digits you want to enter?: "))

count = 0

for i in range(0,digits):
    inp = int(input("Enter digit: "))
    count += inp

print("The average is", count/digits)


#Write a program to find greater number.
inp = int(input("How many numbers you want to enter: "))

lis = []

for i in range(0,inp):
    inp1 = int(input("Enter digit: "))
    lis.append(inp1)

lis.sort()

print("The greatest number is",lis[-1])


#Write a program to find the greatest number among three numbers
lis1 = []

for i in range(0,3):
    digi = int(input("Enter the digit: "))
    lis1.append(digi)

lis1.sort()

print(lis1[-1],"Is the greatest number")

#Write a program to check a number whether it is even or odd.
digit = int(input("Enter a digit: "))

if digit % 2 == 0:
    print("The digit is even")

else:
    print("The digit is odd")

#Write a python program that accepts radius of a circle and prints its area.

radius = float(input("Enter the radius of the circle (In cm): "))

print("The area of the circle is", 3.14*(radius**2))

#Write a program in python to check a number whether it is prime or not.
digit = int(input("Enter a digit: "))

for i in range(2,digit):
    if digit % i == 0:
        print(f"The number {digit} is not a prime number")
        break
    
else:
    print(f'the number {digit} is a prime number')

#Write a program to check a year whether it is leap year or not.
year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"The year {year} is a leap year")

else:
    print(f'The year {year} is not a leap year')

#Write a program in python to convert °C to °F and vice versa.
def CtoF(temp):
    return (temp * 9/5) + 32

def FtoC(temp1):
    return (temp1 − 32) × 5/9


evaluater = input("Enter which value you have (answer with C or F): ")

if evaluater.lower == f:
    temp_tobe_converted = float(input("Enter temperature in °F: "))
    print(FtoC(temp_tobe_converted))

elif evaluater.lower == c:
    temp_tobe_converted1 = float(input("Enter temperature in °C: "))
    print(CtoF(temp_tobe_converted1))

else:
    print("what are you thinking about yourself?.. enter C or F")

#Write a program to check a number whether it is palindrome or not.
word = input("Enter a word: ")

reversed_word = word[::-1]

if reversed_word == word:
    print("The word is palindrome")

else:
    print("The word is not a palindrome")

#12.Write a program to calculate simple interest.
principle_amount = int(input("Enter Principle amount: "))
rate_of_interest = int(input("Enter the rate of interest: "))
time = int(input("Enter time in years: "))

SI = (principle_amount*rate_of_interest*time)/100

print(f"The Simple interest is {SI}%")

#13.Write a program to calculate compound interest.

def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result.

p = float(input("Enter the principal amount: "))

r = float(input("Enter the interest rate: "))

t = float(input("Enter the time in years: "))

amount = compound_interest(p, r, t)

interest = amount - p

#14.Write a program to swap two numbers.
first_digit = int(input("Enter 1st digit: "))
second_digit = int(input("Enter 2nd digit: "))


first_digit,second_digit = second_digit,first_digit

print(first_digit)
print(second_digit)

#Write a program to display ASCII code of a character and vice versa.

inp = input("Enter a digit: ")

print(f"ASCII value of {inp} is {ord(inp)}")

#Write a program to input a character and to print whether a given character is an alphabet, digit or any other character.
inp = input("enter a value: ")

if inp.isdigit == True:
    print("the value is a digit")

else:
    print("the value is not a digit")

#Write a program to convert lowercase alphabet into uppercase and vice versa.
inp = input("Enter a word: ")

if inp.islower == True:
    print(inp.upper())

elif inp.isupper == True:
    print(inp.lower())

else:
    pass

#Write the code using loop to display the following pattern:
#1
for i in range(4):
    for j in range(i + 1):
        print("*", end="")
    print("")

#3
for i in range(4):
    for j in range(i+1):
        print(i+1,end="")
    print("")

#21.Write a program in python to find largest and smallest number in a list.
lis = []

numbers = int(input("How many elements you want to enter: "))

for i in range(numbers):
    ask = int(input("Enter digit: "))
    lis.append(ask)

lis.sort()

print(" ")
print(f"The greatest digit is {lis[-1]}")   

#Write a program to compute GCD and LCM of two numbers
var1 = int(input("Enter 1st digit: "))
var2 = int(input("Enter 2nd digit: "))

print(f"The GCD of {var1} and {var2} is {m.gcd(var1,var2)}")
print(f"The LCM of {var1} and {var2} is {m.lcm(var1,var2)}")