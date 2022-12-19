var1 = 'hello world this is a test'
var1List = var1.split() 
counter = 0 
result = ''

for i in range(len(var1List)-1, -1, -1):
    result += var1List[i] + ' '
print(result)
