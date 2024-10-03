def fact(n):
    if n==0:
        return 1
    return fact(n-1)*n

num = int(input("Enter the number: "))
print(f"Factotial of {num} is {fact(num)}")