

try:
	f = open('test.txt')
	# var = bad_var
	if f.name == 'test.txt':
		raise Exception
		# this manually raises an Error
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print('Error!')
# else only executes if the try properly executes
else:
	print(f.read())
	f.close()
# finally executes regardless of if any errors were triggered
finally:
	print('Executing Finally...')