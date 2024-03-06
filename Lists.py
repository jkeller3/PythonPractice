# Empty Lists
empty_list = []
empty_list = list()

# working with strings

# creates a list of 4 entries
courses = ['History', 'Math', 'Physics', 'CompSci']

# adds Art to the end of courses
courses.append('Art')

# inserts P.E. at position 1, and slides the rest of the list over
courses.insert(1, 'P.E.')

courses_2 = ['Art','Education']

# adds the entirity of courses_2 to spot 0
# courses.append(0, courses_2)
# adds the courses of courses_2 to the end of courses as it would be normally.
courses.extend(courses_2)

# only removes 1 of the 2 Art classes
courses.remove('Art')

# removes the last spot of the list and places it into popped
popped = courses.pop()

# removes the last spot of the list and it disappears
courses.pop() 

print(popped)

# reverses the list back to front
courses.reverse()

print(courses)
print(len(courses))
# prints position 2 to 4 not counting 4.
print(courses[2:4])
# prints the last item on the list
print(courses[-1])

# will fail if index does not find item
print(courses.index('Physics'), 'is the location of the Physics course.')

# true/false return
print('Math' in courses)

# loops through list until end, enumerate lists current index
for item in enumerate(courses):
	print(item)

# turns a list into a string
course_str = ', '.join(courses)
print(course_str)

# separates string into a list using designated split point
new_list = course_str.split(', ')
print(new_list)



# working with numbers
nums = [1, 7, 3, 10, 2]
# sorts in alphabetical or numerical order
nums.sort()
# sorts in reverse order
nums.sort(reverse=True)
print(nums)

# method to print sorted numbers without saving it to a variable
print(sorted(nums))

# method to save sorted numbers to a new variable and keep original
sorted_nums = sorted(nums)
print(sorted_nums)

# function to print minimum number in a set
print(min(nums))
# max function
print(max(nums))
# sum function
print(sum(nums))

