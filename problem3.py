#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234

1       1
2       11 + 1 = 12
3       111 + 11 + 1 = 123
4       1111 + 111 + 11 + 1 = 1234

"""

n = input("Enter an interger that is smaller than 10 => ")
n = int(n)
n = n+1

b = 0
b = int(b)

for i in range(1,n):
    a = i*"1"
    a = int(a)
    c = a + b
    b = c 

print(f"The sum of the series is {c}.")
