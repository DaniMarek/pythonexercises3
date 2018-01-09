def lerst(ls):
	total = 0
	strerng = ""
	for value in ls:
		if isinstance(value, int) or isinstance(value, float):
			total+=value
			
		elif isinstance(value, str):
			strerng += value+" "
			# print strerng

	if strerng and total:
		print "Your list is all kinds of mixed up"
		print "String:", strerng
		print "Sum:", total

	elif strerng:
		print "Seems kinda stringy to me..."
		print "String:", strerng

	else:
		print "What's with all the integers?"
		print "Sum:", total
 
	# print strerng
	# print total


lerst(['roses', 'daisies', 'lillies', 'toast'])

lerst([98, 2, 13.5, 72])

lerst(['magical unicorns',19,'hello',98.98,'world'])