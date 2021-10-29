n = int(input("Enter the element: "))
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(2,n):
    result = num1 + num2
    num1 = num2
    num2 = result
    print(result)
