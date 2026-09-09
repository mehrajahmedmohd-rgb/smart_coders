marks = float(input("Enter your marks percentage : "))
attendance = float(input("Enter your attendance percentage : "))
income = float(input("Enter your annual family income: "))


req_marks = 60.0      
req_atten = 75.0   
mac_income = 300000    


if marks >= req_marks and attendance >= req_atten and income <= mac_income:
    print("Congratulations! You are ELIGIBLE for the scholarship.")

else:
    print("Sorry, you do NOT meet the eligibility criteria.")
