# Task3
# x=11
# y=3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**y)

# Task4
# find the area of a rectangle ,where
# l=20
# b=30
# print(l*b)

# check wheather the given number are odd/even by using modules
# numbers=(78,13,99,1,161,4)
# for n in numbers:
#     if n % 2 == 0:
#        print (f"(n) is even")
#     else:
#        print (f"(n) is odd")

# print(78%2)
# print(13%2)
# print(99%2)
# print(1%2)
# print(161%2)
# print(4%2)

# task 6
# copmparison operator
# x=10
# y=20
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)

#Task 7
# a=5
# b=30
# c=5
# print(a>b)
# print(a>=b)
# print(a<=b)
# print(a==b)
# print(a!=b)
# print(b<c)

# Task 8
# num1=15
# num2=30
# num3=20
# num4=(num1<num3 and num2>num3)
# num5=(num1==num2 and num3!=num1)
# num6=(not(num1!=num3))
# num7=(num3!=num2 or num1!=num3)
# print(num4)
# print(num5)
# print(num6)
# print(num7)

# task9
# num=2
# num+=10
# print(num)
# num-=10
# print(num)
# num*=10
# print(num)
# num/=5
# print(num)
# num//=2
# print(num)
# num**=2
# print(num)
# num%=3
# print(num)

# task8
# food=['chicken','fish','mutton','chapathi','dosa']
# print(food)
# print(food[0])
# print(food[-1])
# print(len(food))

# task9
# bag=['pen','notebook','eraser','ruler']
# print('pen'in bag)
#print('phone'in bag)

# task10
# tiffen=['milk','eggs','bread']
# print(tiffen)
# tiffen.append('butter')
# print(tiffen)
# tiffen.insert(1,"sugar")
# print(tiffen)
# tiffen.remove('eggs')
# print(tiffen)

# task11
#  score=[45,78,23,90,56]
# score.sort()
# print(score)
# score.reverse()
# print(score)
#  print(score[0:3])

# task12
# fruit=['mango','apple','banana','cherry','grape']
# print(fruit.pop())
# print(fruit.pop(1))
# print(fruit)
# fruit.clear()
# print(fruit)

# task13
# temperatures=(34,28,31,29,35,27,33)
#print(temperatures[2:6])
# print(35 in temperatures)
# print(40 in temperatures)

# task14
# color=('red','blue','green')
# color.append('yellow')

# task15
# employee=('kiran','developer',75000,'chennai')
# w,x,y,z=employee
# print(w)
# print(x)
# print(y)
# print(z)

#task16
# score=(55,82,91,76,82,65,91,91)
# print(score.count(91))
# print(score.index(82))
# score.append(88)

#task17
# city=('chennai')
# print(type(city))


# Task18
# employee={
#     'name':'meena',
#     'dpartment':'hr',
#     'salary':40000
# }
# print(employee)
# employee['experience']=3
# print(employee)
# employee['salary']=45000
# print('after change',employee)
# employee.update({'department':'finance',
#                  'city':'madurai'
# ''})
# print(employee)

# task19
# original={
#     'x':10,
#     'y':20,
#     'z':30
# }
# backup=original.copy()
# original.clear()
# print(original)
# print(backup)
#backup still have data because we already create a copy 
# of the orginial so it create a new pairs with same data so it doesnt
# affect the seperate data

# task20
# cart= {
#     'rice':100,
#     'oil':180,
#     'sugar':200
# }
# print(cart)

# task21
# book={
#     'title':'wings of fire',
#     'author':"APJ A bdul Kalam",
#     'page':320,
#     "available":True
#  }
# print(book)
# print(len(book))

# task22
# print(book.keys())
# print(book.values())
# print(book.items())

# task23
# amount=float(input('enter the amount: ' ))
# if amount>500:
#     discount=amount*0.10
#     print(discount)
#     final=amount-discount
#     print(final)
#     print("the final amount to be paid:",final)
# else:
#     print("no discount.amount to be paid:",amount)    
     
# 
# task24
# num1=int(input('enter first number'))
# num2=int(input('enter second number'))
# if num1>num2:
#     print('num1 is larger')
# elif num2>num1:
#     print('num2 is larger')
# else:
#     print('both number are equal')    

# # task25
# num=int(input('enter a number'))
# if num>0:
#     print('positive')
# elif num<0:
#      print('negative')
# else:
#      print('zero') 

# age=int(input("enter age"))
# if age<0:
#    print('not born')
# elif age<=2:
#    print('infant')
# elif age<=12:
#    print('child')
# elif age<=17:
#    print('teenager')
# elif age<=59:
#    print('adult')
# else:
#    print('senior')               

# num=int(input('enter an number'))
# if num%3==0 and num%5==0:
#     print('the number is divisible by 3 & 5')
# elif num%3==0:
#     print('the number i divsible by 3') 
# elif num%5==0:
#     print('the number is divisible by 5')
# else:
#     print('the number is not divisible 3 & 5 ')



# vegetables = ["tomato", "onion", "carrot", "spinach", "potato"]
# for veg in vegetables:
#     print(veg)



# prices = [45, 120, 89, 200, 55, 150, 30, 180]
# count = 0
# for price in prices:
#     if price > 100:
#         count += 1
# print(count)
 

# for i in range(2, 21, 2):
#     print(i)


# num = 5
# while num >= 1:
#     print(num)
#     num -= 1
# print('Done!')

# items = [120, 80, 200, 150, 60, 90, 110]
# total = 0
# for price in items:
#     total += price
#     if total >= 500:
#         print(total)


# def show_banner():
#     print("Welcome to our store!")
#     print("Quality you can trust.")
#     print("Open 24/7.")
# show_banner()

# def show_shop_info():
#     print("Shop: SM Veg Mart")
#     print("Location: Puducherry")
#     print("Delivery: Same day")
# show_shop_info()


# def greet_customer(name, city):
#     print(name)
#     print(city)

# greet_customer("Meena", "Chennai")
# greet_customer("Ravi", "Puducherry")
# greet_customer("Anitha", "Coimbatore")


# def show_delivery_charge(order_amount):
#     if order_amount >= 300:
#         print("Free delivery!")
#     else:
#         print("Delivery charge: Rs 40")
# show_delivery_charge(450)
# show_delivery_charge(150)
# show_delivery_charge(300)

# def calculate_bill(price, quantity):
#     return price * quantity

# bill1 = calculate_bill(45, 3)
# print(f"Total bill: Rs {bill1}")

# bill2 = calculate_bill(120, 2)
# print(f"Total bill: Rs {bill2}")

# def calculate_bill(price,quantity):
#     total=price*quantity
#     return total
# bill1=calculate_bill(45,3)
# bill2=calculate_bill(120,2)

# print('total bill:Rs',(bill1))
# print('total bill:Rs',(bill2))
