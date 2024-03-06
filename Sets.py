# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

# Sets don't care about order
# removes duplicate values
# useful for finding if something exists in a set
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print('Math' in cs_courses)

# Shows items that exist in both sets
print(cs_courses.intersection(art_courses))

# Shows items that only exist in cs_courses
print(cs_courses.difference(art_courses))

# Shows items that are included in either set
print(cs_courses.union(art_courses))

