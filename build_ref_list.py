import pickle
import urllib2
import json

code = ['category_groups','categories','locations']
additional = ['','','&level=metro']
for i in range(len(code)):
	request = urllib2.Request('http://reference.3taps.com/{0}/?auth_token=b49d0f32cd93c0a3102d96bf7841c0c5{1}'.format(code[i],additional[i]))
	response = urllib2.urlopen(request)
	read = response.read()
	dictionary = json.loads(read)

	my_list = [value['code'] for value in dictionary[code[i]]]

	pickle.dump(my_list,open(code[i],'w'))
