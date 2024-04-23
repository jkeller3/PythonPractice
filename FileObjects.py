# File Objects

# 'r' = file for reading
# 'w' = file for writing
# 'a' = file for appending
# 'r+' = file for reading and writing

# f = open('test.txt', 'r')
# f.close()


# same as above except only executes within the block, and closes at the end on its own.
with open ('test.txt', 'r') as f:
	
	# for line in f:
		# print(line, end='')


	size_to_read = 100
	f_contents = f.read(size_to_read)
	

	while len(f_contents) > 0:
		print(f_contents, end='')
		# print(f.tell())
		# f.seek(0) causes infinite loop
		f_contents = f.read(size_to_read)

# print(f.name)
# print(f.mode)

with open('test2.txt', 'w') as f:
	f.write('Test')
	f.seek(0)
	f.write('R')
	# this overwrites the T from Test with R.

with open('test.txt', 'r') as rf:
	with open('test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

