'''
var1 = 'hello world this is a test'
var1List = var1.split() 
counter = 0 
result = ''

for i in range(len(var1List)-1, -1, -1):
    result += var1List[i] + ' '
print(result)


#reverse characters
test1 = 'test'
print(test1[::-1])

#reverse characters in array without changing the order
myString = 'Python is cool'
splitedArray = myString.split()
newResult = []
i = 0

while i < len(splitedArray):
    newResult.append(splitedArray[i][::-1])
    i = i + 1
 
print(newResult)
result3 = ' '.join(newResult)
print(result3)



#count the characters in a string

myNewString = 'aaabbccccccccasdfjsadfl'
dic = {} 
for i in myNewString:
    if i in dic.keys():
      dic[i] = dic[i] + 1
    else:
      dic[i] = 1
    print(dic) 

for k, v in dic.items():
    print('{}={} times '.format(k,v)) 
#tree

rows = 6 
for i in range(1, rows):
    print(' ' * (rows - i), end='')
    print('* ' * i)

#find a substring

StringTest = 'Take up one idea and make that idea your life'
subString = 'idea'
StringToArray = StringTest.split()
counter = 0
print(StringTest.find('idea'))

for i in StringToArray:
    if i == subString:
        counter = counter + 1


print('Substring is found in: ', counter, ' times')
'''

#challenge

accBalance = 10000

print('1. Check Balance')
print('2. WithDraw')
print('3. Deposit Cash')
print('4. Deposit Check') 

chosen = int(input('choose an option: '))  

if chosen == 1:
  print('1. Check Balance')
  print(accBalance) 
elif chosen == 2:
  print('2. WithDraw')
  withdraw = int(input('enter how much: '))
  accBalance = accBalance - withdraw
  print('withdrawing...', withdraw)
  print('new Balance: ', accBalance)
  
elif chosen == 3:
  print('3. Deposit Cash')
  deposit = int(input('enter how much: '))
  accBalance = accBalance + deposit 
  print('depositing...', deposit) 
  print('new Balance: ', accBalance)
elif chosen == 4:
  print('4. Deposit Check') 
  print('you need to go to the bank for this request')

#function

def testing(a, b):
    return "sum: ", (a+b) 

newSum = testing(1,2)
print(testing(1,2))