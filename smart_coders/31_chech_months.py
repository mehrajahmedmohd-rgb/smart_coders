months = int ( input ("enter the month to check days :") )

match months :
    case 1 | 3| 5 |7|8|10|12 :
        print(f"in {months} they are 31 days ")

    case 4|6|9|11:
        print(f"in {months} they are 30 days ")

    case 2:
        print(f"in {months} they are 28 days and 29 in leap year")

    case _:
        print("invalid")
        