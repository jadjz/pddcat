
# Creates a list with duplicates removed

cleared_list = filter(None, open('list.txt').read().split('\n'))
cleared_list = list(dict.fromkeys(cleared_list))

# TODO: remove if starts with underscore or is 'unorganised'
# TODO: also put append_regex.py here so there won't be 2 different files

try:
	f = open('filtered_list.txt', 'w')
	for l in sorted(cleared_list):
		f.write("%s\n" % l)
except IOError as e:
	print(e)
