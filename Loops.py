
nums = [1, 2, 3, 4, 5]

for num in nums:
	if num == 3:
		print('Found!')
		# break
		# forces out of loop
		continue
		# skips to next iteration of loop
		# print(num) line does not activate
	print(num)

for num in nums:
	for letter in 'abc':
		print(num, letter)

for i in range(1,11):
	print(i)

x = 0

while x<=10:
	if x == 5:
		break
	print(x)
	x +=1 

while True:
	# if x == 5:
	#    break
	print(x)
	x += 1
# creates endless loop. must use ctrl + break to escape