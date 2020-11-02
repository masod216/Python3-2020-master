## Link to good exams online
https://www.codequizzes.com/python
(Note: this part is not included: https://www.codequizzes.com/python/beginner-III/sets)

## Exercise
* Create a python program that gets from the user a number as an input and prints the first elements of the Fibonacci numbers

for example:
```
Enter a number: 4

0 1 1 2
```

```
Enter a number: 9

0 1 1 2 3 5 8 13 21
```

## Result
```python
def fibonacci(amount):
    first=0
    second=1
    print(first,second,end=" ")
    for x in range(2,amount):
        temp=second
        second+=first
        first=temp
        print(second,end=" ")




fibonacci(4)
print()
fibonacci(9)
print()
```

output:
```
0 1 1 2 
0 1 1 2 3 5 8 13 21 
```
