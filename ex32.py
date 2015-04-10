the_count = [1, 2, 3, 4, 5] #we just created the variable 'the_count' and it points at the list [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] #a list can have integers, strings, lists, and None

#this first kind of for-loop goes through a list
for number in the_count: #this for loop is iterating the elements in the_count list, in this cas one to five 
    # the term number in line six is used to name each item or iterable (1 2 3 4 5) in the list the_count. it could be named anything 
    print "This is count %d" % number #This like prints "This is the count (the iterable would be printed here)" and this is pulled because % 
        #number at the end of the line is the term we used for the items or iterables in the line above. this is using the string format 

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i #%r is used for a mixture of different types of data this will return the information with quotes or raw data
        #the other types, %s and %d, are for displaying data to users 

#We can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6): #the range function creates a list of numbers, and i represents each element in the list. this list will start at 0 and go to 5
    print "Adding %d to the list." % i
    #append is a function that lists understand
    elements.append(i) #this loop will keep going until it hits the end of the range, and for each iteration, the i is added to the list 

#now we can print them out too
for i in elements:
    print "Element was: %d" % i


    