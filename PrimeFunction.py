def isPrime(num):
	## for(int i = 0, i<num, i++):
	prime = True
	factors = []
	if(num == 1):
		factors.append(num)
		prime = False
	halfNum = int(num / 2)
	for i in range(2, halfNum + 1):
		## print(i,num,'remainder is ',num % i)
		if(num % i == 0):
			factors.append(i)
			prime = False
	##if(prime == False):
		##statement = str(num) + ' is not prime.'
	##else:
		##statement = str(num) + ' prime.'
	return(num, prime, factors)


numList = {}
for i in range(1, 26):
	numList[i] = isPrime(i)

print('Number:','Prime:','Factor List:')
print(numList[20])




