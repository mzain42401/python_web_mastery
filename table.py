# find Table of any integer
try:
    usernum=int(input("Enter your number"))
    tablestart=1
    while tablestart <=10:
        if isinstance(usernum,int):
            result=usernum* tablestart
            print(f"{usernum} x {tablestart} = {result}")
            tablestart +=1
except :
        print("Please enter a valid integer.")
        

# Output (Suppose user type 3)

# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30