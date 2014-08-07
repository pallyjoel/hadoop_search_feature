import sys, csv, re, json
reader = csv.reader(sys.stdin, delimiter='\t')

for row in reader:
		if len(row) != 19:
			continue
		#print len(row)
		if row[0] == "id" :
			continue
		
		#print len(row)
		if row[3] == "\\N":
			author_id = 0
		else:
			author_id = (row[3])
		if row[0] == "\\N":
			forum_id = 0
		else:
			forum_id = (row[0])
		
		if row[2] == "\\N":
			tag = None;
		else:
			tag_full = row[2]
			tags = tag_full.split(" ")
			
		
		if row[6] == "\\N":
			parent_id = 0
		else:
			parent_id = (row[6])
		
		if row[7] == "\\N":
			abs_parent_id = 0;
		else:	
			abs_parent_id = (row[7])		
		body_temp = row[4].replace('</p>', "?").replace('\n', '?').replace('\N', '?').replace('<p>', '?').replace('<ul>', '?').replace('</ul>', '?').replace('<li>', '?').replace('</li>', '?')
		chars = [',','!','.',';','?','[',']','<','>','/','-','\t','\\','"',"(",")","_",'*',':','&', '%']
			
		body = body_temp.translate(None, ''.join(chars)).strip().split()
		
		
		node_type = row[5]

		time = row[8]
		hour = time[11:13]
		
		
		for i in range(0,len(body)):
			if len(body[i]) > 3 and not "=" in body[i] and not "+" in body[i]:
				if node_type == "question":
					print "{0}\t{1}\t{2}\t{3}".format(body[i].lower(), forum_id, author_id, node_type)
				else:
					print "{0}\t{1}\t{2}\t{3}".format(body[i].lower(), abs_parent_id, author_id, node_type)
		for i in range(0,len(tags)):
			if node_type == "question":
				print "{0}\t{1}\t{2}\t{3}".format(tags[i].lower(), forum_id, author_id, "tag")
				
		
		"""
		print '{0}\t{1}\t{2}\t{3}'.format(forum_id, parent_id, abs_parent_id, node_type,)
		#print '{0}\t{1}\t{2}\t{3}'.format(forum_id, node_type, parent_id, abs_parent_id)
		"""
		