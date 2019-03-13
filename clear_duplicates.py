
# Creates a list with duplicates removed,
# names starting with underscore or dash or is 'unorganised' filtered
# and regex appended

cleared_list = filter(None, open('list.txt').read().split('\n'))
cleared_list = list(dict.fromkeys(cleared_list))
temp = []

for el in cleared_list:
	# don't add names that start with underscore or dash or is 'unorganised'
	if el.startswith('_') or el.startswith('-') or el == 'unorganised':
		# for whatever reason this didn't catch a few, so we're doing it the other way
		# cleared_list.remove(el)
		pass
	else:
		# replace _ with regex whitespace or dot
		el = el.replace('_', '[\. ]')
		temp.append(el)

try:
	f = open('filtered_list.txt', 'w')
	for l in sorted(temp):
		f.write("%s\n" % l)
except IOError as e:
	print(e)
