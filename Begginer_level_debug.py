name = "Pratik"
age = 24
print("My name is "+ name)
print('I am'+ ' ' + str(age) + " " + 'years old') # error we have to put str before age
print(age + 1)



# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = num1+num2
# print(result)


age = 18
if age>=18: #error 
    print("Eligible to vote")
else:
    print("not eligible")

for i in range(1,6):
    print(i*2)

# numbers = [10,20,30,40,50,60]
# for i in range(len(numbers)):
#     # print(numbers[i+1]) #error


def add(a,b):
    result = a+b
    return result # have to return result 

print(add(10,20))

numbers = [10,25,5,40,15]

maximum = 0
for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)

numbers = [1,2,4,7,8,10,13]

count = 0

for num in numbers:
    if num % 2 == 0:
        count+=1 

print(count)


word = "python"
reverse = ""
for i in range(len(word)):
    reverse = word[i] + reverse
print(reverse)


numbers = [8,3,12,1,7]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)



