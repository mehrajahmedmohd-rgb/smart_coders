'''  🛠️ The Challenge
Write a program that loops through numbers from 1 to 20 using range(1, 21).
For each number:If the number is perfectly divisible by both 3 and 5, print "FizzBuzz".
Elif the number is divisible by 3, print "Fizz".
Elif the number is divisible by 5, print "Buzz".
Else, just print the number itself.
Two Quick Python Hints for You:The Loop: To loop from 1 to 20, use: for i in range(1, 21):
Divisibility: Just like in C, use the modulo operator %.
For example, i % 3 == 0 checks if a number is perfectly divisible by 3.   '''


n=int(input("enter the number :"))

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0 :
        print("FIZZBUZZ")

    elif i % 3 == 0 :
        print("FIZZ")

    elif i % 5 == 0 :
        print("BUZZ")

    else:
       print(i)         