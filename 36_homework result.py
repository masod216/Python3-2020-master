id=input("Enter your id: ")

if(len(id)>9):
    print("Sorry - your id is to long")
else:
    id="0"*(9-len(id))+id
    sum=0
    for x in range(0,len(id)):
        temp= int(id[x])*(1+(x%2))
        sum+=temp%10 + temp//10
    if sum%10==0:
        print("your id is valid")
    else:
        print("your id is not valid")


