import time
print("Quiz will start in...")

time.sleep(0.5)
print("3")

time.sleep(0.5)
print("2")

time.sleep(0.5)
print("1")

time.sleep(0.5)
print("START!")

score=0
Q1=input("1. when python is develop in which year? ")
if Q1=="1991":
    print("correct..!!")
    score=score+1
else:
    print("wrong try again") 

Q2=input("2. when c++ is develop in which year? ")
if Q2=="1983":
    print("correct..!!")
    score=score+1
else:
    print("wrong try again")       

Q3=input("3. What is the most consumed manufactured drink in the world after water?")
if Q3.lower()=="tea":
    print("correct..!!")
    score=score+1
else:
    print("wrong try again")  

Q4=input("4. Which is the deepest ocean in the world?")
if Q4.lower()=="the pacific ocean" :
    print("correct..!!")
    score=score+1
else:
    print("wrong try again")
     

Q5=input("5. Which is the best-selling book series of the 21st century?")
if Q5.lower()=="harry potter" :
    print("correct..!!")
    score=score+1
else:
    print("wrong try again")

print("-------RESULT------")
print("your score is:--", score,"/5")   

percentage=(score/5)*100
print("your pecentage is:--" ,percentage ,"%")