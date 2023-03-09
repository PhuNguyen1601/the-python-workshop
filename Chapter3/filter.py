 ## using a filter lambda
 
nums = list(range(1000))
#? filter (condition,list)
filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0,nums)

print(filtered)
print('-----')
print(sum(filtered))