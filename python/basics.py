#variables
#they are used to store information
rent = 190000
groceries = 50000

print(rent+groceries)

#numbers: int, double: float
number = 7.890009
off = round(number, 2)
print(off)


#string
name= "Favour Adetayo"
age= "23"

#cocantination 
result = name+age
print(result)

details = '''favour is a girl
she works as a developer
she loves God'''

print(details)

#List
items = ["bread", "egg", "Lion", "Matte"]
print(items)

items.append("Goldenmorn")

items.insert(1, "Soda")

items in "baker"


#Conditional Statement 
#write a program that asks user to enter a number. Program should tell them if the is odd or even
num = input('Emter a number: ')
#convert the number entered to an integer
num = int(num)

if num%2 ==0:
    print('Number is even')

else: 
    print('number is odd')

#write a program that asks user to enter dish name and it should print which cusine is that dish
yoruba  = ["Semo", "iyan", "Amala", "Eba"]
english = ["Rice", "Beans", "Egg", "Fried rice"]
italian = ["Egg roll", "Pasta", "Buns", "Macossa"]
dish = input('Enter a dish: ')
if dish in yoruba:
    print ("Yoruba")
elif dish in english:
    print ("English")
elif dish in italian:
    print("itallian")
else:
    print("Based on my knowledge, i have no idea what type of dish is this")



#For statement
#problem: Store monthly expenses in a list and find out total expenses for all months
exp = [1020, 2030, 4040, 5050]
total = 0
for item in exp:
    total = total + item
print(total)

#print month number and expense and then in the end print total expense
for i in range(len(exp)):
    print('Month:', (i+1), 'Expense:', exp[i]),
total = 0
total = total +exp[i]
print('Total expense is:', total) 
#print no 1-10

for i in range(1,11):
    print(i)