# Input coefficients
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation ('a' cannot be 0).")
else:

    d = (b**2) - (4*a*c)
    print(f"\nDiscriminant = {d:.2f}")

   
    if d > 0:
        print("Nature: Roots are Real and Distinct (Different)")
        root1 = (-b + (d ** 0.5)) / (2*a)
        root2 = (-b - (d ** 0.5)) / (2*a)
        print(f"Root 1 = {root1:.2f}")
        print(f"Root 2 = {root2:.2f}")

    elif d == 0:
        print("Nature: Roots are Real and Equal")
        root = -b / (2*a)
        print(f"Root 1 = Root 2 = {root:.2f}")

    else:
        print("Nature: Roots are Imaginary (Complex)")
        real_part = -b / (2*a)
        imag_part = (abs(d) ** 0.5) / (2*a) 
        print(f"Root 1 = {real_part:.2f} + {imag_part:.2f}i")
        print(f"Root 2 = {real_part:.2f} - {imag_part:.2f}i")
