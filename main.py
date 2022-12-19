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