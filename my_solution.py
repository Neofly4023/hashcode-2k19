import operator

with open("a_example.txt") as album:
    #get the size of dataset
    data_size = int(album.readline())
    #convert lines to list
    mylist = []
    id = 0
    for photo in album:
    	item = []
    	item.append(id)
    	id+= 1
    	item.extend(photo.strip('\n').split(' '))
    	used = [0]
    	item.extend(used)
    	mylist.append(item)
    mylist.sort(key=lambda item: int(item[2]) , reverse=True)
    #print(mylist)

    mydict = {}
    #process every line
    for photo in mylist:
    	orientation = photo[1]
    	size = int(photo[2])
    	tags = set()
    	#get tags
    	for i in range(3,size+3):
    		tags.add(photo[i])
    		if not photo[i] in mydict:
    			mydict[photo[i]] = 1
    		else:
    			mydict[photo[i]] += 1
    	#print(tags)
    #print(mydict)
    sorted_dict = sorted(mydict.items(), key=operator.itemgetter(1), reverse=True)
    #print(sorted_dict)

    ori_count = 0
    slideshow = []
    for index in range(data_size):
    	if (mylist[index][-1] == 0):
	    	if (mylist[index][1] == 'H'):
	    		slideshow.append(str(mylist[index][0]))
	    		mylist[index][-1] = 1
	    	elif (mylist[index][1] == 'V'):
	    		counter = 1
	    		while ( index + counter < data_size):
	    			if (mylist[index + counter][1] == 'V' and mylist[index + counter][-1] == 0):
	    				photo_index = index + counter
	    				mylist[index][-1] = 1
	    				mylist[photo_index][-1] = 1
	    				break
	    			counter+=1
	    		output = ''.join([str(mylist[index][0]),' ',str(mylist[photo_index][0])])
	    		slideshow.append(output)


with open('submission_a.txt', 'w+') as submit:
	length = len(slideshow)
	submit.writelines(str(length))		
	submit.writelines('\n')
	
	for item in slideshow:
		submit.writelines(item)
		submit.writelines('\n')