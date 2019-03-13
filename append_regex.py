
# Replace _ with regex whitespace or dot

reg_list = filter(None, open('filtered_list_cleared.txt').read().split('\n'))
reg_list = list(dict.fromkeys(reg_list))
temp = []
for el in reg_list:
	el = el.replace('_', '[\. ]')
	temp.append(el)

try:
	f = open('regex_list.txt', 'w')
	for l in sorted(temp):
		f.write("%s\n" % l)
except IOError as e:
	print(e)
