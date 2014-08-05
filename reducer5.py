import csv, sys, json
print sys.argv

old_id = None

old_entry = None

index = {}


for row in sys.stdin:
	data = row.strip().split("\t")
	
	if len(data) != 4:
		continue
		
	entry, node_id, author_id, node_type  = data
	
	
	if entry != old_entry:
		info = {'nodes': [], 'authors': [], 'types': []}
		old_entry = entry
		index[old_entry] = info
	
	old_entry = entry
	index[old_entry]['nodes'].append(node_id)
	index[old_entry]['authors'].append(author_id)
	index[old_entry]['types'].append(node_type)

with open('index.json', 'wb') as outfile:
	json.dump(index, outfile)

with open('index2.txt', 'wb') as outfile2:
	outfile2.write(str(index))	