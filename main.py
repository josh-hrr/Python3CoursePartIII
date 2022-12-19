var1 = 'hello world this is a test'
var1List = var1.split() 
counter = 0 
result = ''

for i in var1List: 
    counter = counter + 1 
    print(var1List[(counter - 1) - 1])
    result += var1List[(counter - 1) - 1] + ' '

print(result)