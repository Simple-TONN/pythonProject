number = int(input())

check1 = (number % 2 == 1)
check2 = (number % 2 == 0 and 2 <= number <= 5)
check3 = (number % 2 == 0 and 6 <= number <= 20)
check4 = (number % 2 == 0 and number>20)

print(f"{check2,check1,check3,check4}")
if check1 or check3:
    print("Weird")
elif check2 or check4:
    print("Not Weird")