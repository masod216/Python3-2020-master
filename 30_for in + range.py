start=4
end=8


# range - is function that returns an object that produces a sequence of integers 
# from start (inclusive) to stop (exclusive)
for x in range(start,end):
    print("for-in",x)
else:
    print("after loop")


"""
OUTPUT:
________________
for-in 4
for-in 5
for-in 6
for-in 7
after loop
"""