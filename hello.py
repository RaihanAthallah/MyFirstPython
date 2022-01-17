import math

# name = input('What is your name ')
# weight = input('Weight(pounds) ')
# toKilograms = float(weight) * 0.453592
# msg = f'{name[0:7]} {weight} lbs {toKilograms} kg'
# print(msg.upper())
# print(len(name))
# print(math.ceil(toKilograms))

# price = 1000000
# credit = True
# if credit:
#      price = price + (price*0.1)
# else:
#     price = price + (price*0.2)
# print(price)

# name = input('What is your name ? ')
# if len(name) < 3:
#     print('name must be at least 3 characters')
# elif len(name) > 50:
#     print('name must be at least 50 characters')
# else:
#     print('name looks good!')

# weight = input('Weight: ')
# weight = float(weight)
# coms = input('(L)bs or (K)g: ')
# if coms.upper() == 'K':
#     # msg = 
#     print(f'You are {weight/0.45} pounds')
# elif coms.upper() == 'L':
#     # msg = 
#     print(f'You are {weight*0.45} kg')

# number = 9
# i = 0
# while i < 3:
#     answer = float(input('Answer: '))
#     if answer != number:
#         print('incorrect')
#         i+=1
#     else:
#         print('correct !')
#         break
# else:
#     print('Sorry you Failed :(')
# print('Game Over !')
    
# coms = ''
# start = False
# while True:
#     coms = input('Coms:').lower()
#     if coms == 'help':
#         print('''
#     start - to start the car
#     stop - to stop the car
#     quit - to exit
#         ''')
        
#     elif coms == 'start' and start == False:
#         start = True
#         print('Car started...Ready to go!')
#     elif coms == 'stop' and start == True:
#         start = False
#         print('Car stopped.')
        
#     elif coms == 'quit':
#         break
#     else:
#         if start == False:
#             print('The car is already stopped')
#         elif start == True:
#             print('The car is already Started')
#         else:
#             print("I don't understand the commands")


# for item in range(3,10,2): #range(start,total,diff)       
#     print(item)

# prices = [10,20,30]
# total = 0
# for items in prices:
#     total += items
# print(f'Total Prices {total}')

# for x in range(5):
#     for y in range(4):
#         print(f'({x},{y})')

# numbers = [1,1,1,1,5]
# for i in numbers:
#     for y in range(i):
#         print('x',end="")
#     print(' ')

# numbers = [1,2,4,2,5,6,1,2,7,2,8,2,8,9,10,9,11,5,2,14]
# largest = 0
# for i in numbers:
#     if largest < i:
#         largest = i
# print(f'largest: {largest}')

# numbers = [5,2,1,5,7,4]
# numbers.sort()
# numbers.clear()
# print(numbers)

# numbers = [2,2,4,6,3,4,6,1]
# unique = []
# for i in numbers:
#     if i not in unique:
#         unique.append(i)
# unique.sort()
# print(unique)

# numbers = (1,2,3,3,1)
# print(numbers.count(3))

# customer = {
#     'name': 'Raihan',
#     'age': 29,
#     'verified':True
# }

# print(customer.get('birthdate','19 august 2002'))

# numbers = {
#     '1':'one',
#     '2':'two',
#     '3':'three',
#     '4':'four',
#     '5':'five',
#     '6':'six',
#     '7':'seven',
#     '8':'eight',
#     '9':'nine',
#     '0':'zero'
# }
# phone = input('Phone: ')
# output = ''
# for i in phone:
#    output += numbers.get(i,'!') + ' '
# print(f'{output}')


# emojis ={
#     ':)':'🙂',
#     ':(':'☹️',
#     ':D':'😃'
# }
# message = input('Message: ')
# words = message.split(' ')
# output = ''
# for i in words:
#     output += emojis.get(i,i) + ' '
# print(output) 

# EXERCISE 1 INDEX OF CAPITAL LETTER
    # def capital_index(word):
    #     list = []
    #     index = 0
    #     for i in word:
    #         if i.isupper():
    #             list.append(index)
    #         index += 1
    #     print(list)
            
    # words = input('>')
    # capital_index(words)
    
# EXERCISE 2 MIDDLE LETTER
    # def mid(words):
    #     length = len(words)
    #     if length%2 == 1:
    #         return words[int(length/2)]
    #     else:
    #         return ''
    # print(mid('abc'))
    
#  EXERCISE 3 ONLINE STATUS
    # statuses = {
    #     "Alice": "online",
    #     "Bob": "offline",
    #     "Eve": "online",
    # }
    # def online_count(list):
    #     count = 0
    #     for i in list:
    #         if list.get(i) == 'online':
    #             count += 1
    #     return count
    # print(online_count(statuses))
    
#  EXERCISE 4 RANDOM NUMBERS
    # import random 
    # def random_number():
    #     return random.randint(1,100)

    # print(random_number())
    # print(random_number())
    # print(random_number())
    
    
#  EXERCISE 4 RANDOM NUMBERS
def only_ints(a,b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False
    
print(only_ints(1,"a"))
    
