
lastname = "Tao"
firstname = "Junru"
id = 32


#1. this method is relatively slower if there's a massive amount of string ops
text = "My Name is" + firstname + lastname + str(id)

#2. using %s (something like C)
text = "My Name is %s %s %s" % (firstname, lastname, id)
#**Note: Problem is when there are "%s_%s_%s_%s_%s_%s_...%s_%s_" 
# you have no idea what they are

#3. using additional identifiers (dictionary)
text = "My Name is %(fN)s %(lN)s %(id)s" % {
    'fN': firstname, 'lN': lastname, 'id': id}


#4. alternative:
text = "My Name is {} {} {}".format(firstname,lastname,id)

#4. you can choose which goes where:
text = "My Name is {0} {1} {2}".format(firstname,lastname,id)

# as you can do:
text = "My Name is {1} {2} {0}".format(firstname,lastname,id)

# using a dictionary
text = "My Name is {fn} {ln} {id}".format(fn=firstname,ln=lastname,id=id)