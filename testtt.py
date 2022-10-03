def mintosecs(min):
    return min * 60

def addition(num1,num2):
    return num1 + num2

def yearstoday(year):
    return year * 365


print(mintosecs(int(input("time in minutes: "))))
print(addition(int(input("number 1: ")), int(input("number 2: "))))
print(yearstoday(int(input("age: "))))
