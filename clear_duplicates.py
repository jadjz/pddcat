
# Creates a list with duplicates removed

cleared_list = filter(None, open('list.txt').read().split('\n'))
cleared_list = list(dict.fromkeys(cleared_list))

try:
	f = open('filtered_list.txt', 'w')
	for l in sorted(cleared_list):
		f.write("%s\n" % l)
except IOError as e:
	print(e)
