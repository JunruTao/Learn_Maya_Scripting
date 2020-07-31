#basic print function
print "hello world"

#uisng "type()" function to get the type of variables
print type("hello world") #will return type as <string>
print type(22) #will return type as <int>
print type(29.34) #float
print type(True) #boolean
print type(False)#boolean
print type(None) #<type NoneType> -> similar to NULL or Nah or nullptr

#variables:
foo = "Hello"
print foo

#lists (items in a list in python can be anything)
myList = ["Hello", 10, 23.4, False]
print myList

myList = ["Hello", 10, 23.4, False, foo] #you can put variables into the list
print myList

#push back in python: append; C++: push_back(), C# Add(), python: .append()
myList.append("Goodbye")
print myList

#getting the list items: C++ = C# = python : list[n]
print myList[1] #get the second item in the list


##--------------------------------------------------------------------------------------------------------
#Tuple
#    1. Fixed size (probably static, defined at compile time)
#    2. Executed faster than lists
#more complex list type: TUPLE **New <- closed with()
myTuple = ("Hello", "Hello", 10, 23.4, False, foo, foo)
#test the type
print myTuple, type(myTuple)
###Note: Tuples CANNOT be either appended, or had its items reassigned: i.g. (NO)tuple[1] = ...(NO)

#SET:
#   1. unodered
#   2. uniqueness of items
mySet = set(myTuple)
print mySet
#result: ("Hello",  23.4, 10, False, foo) <- unodered, unique, no duplicates

#Dictionary
#      1. std::unordered_map c++, dictionary is unodered
#      2. Key -> value
#      3. like set, uniqueness
#      4. like lists, you can reassign values
myDict = {"Last Name":"Tao", "First Name":"Junru", "Age":"25"}
print myDict
print myDict["Last Name"] #use the key to get values

myDict["Age"] = 26
print myDict


