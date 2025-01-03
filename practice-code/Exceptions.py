


# try:
#     x=10/0
# except:
#     print("That didn't work yaar")

try:
    answer= input("What should I divide 10 by?")
    num= int(answer)
    print(10/num)
    
except ZeroDivisionError as e:
    print("You can't divide by zero!")
    
except ValueError as e:
    print("You can't give me a valid number!0")
    print(e)
    
finally:
    print("This code always runs")