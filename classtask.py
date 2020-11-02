num=0

while num<=3 or num>=9:

    num=int(input("Please enter a number : "))

mat=[ [" " if (j<=num-i-1) else(i+1) for j in range(num)] for i in range(num)]

for row in mat:
    for col in row:
        print(col,end="")
        print()