n = int(input())
y=0
x=0
for i in range(1,n+1):
    a,b=input().split()
    a=str(a)
    b=int(b)
    if a=="север":
        y=y+b
    elif a=="юг":
        y = y - b
    elif a == "восток":
        x=x+b
    elif a == "запад":
        x = x - b
print(f"{x} {y}")

 #   print(f"это {a} -- это {b}")