#file name = MyFunctionExample.py
def Foo():
    myList = [1, 2, 3, 4, 5]
    for num in myList:
        print num, "says hello"

# def defines function, when add it, you need to tab all the lines
# under it to be inside def's scope


#===================================================================
#Now as long as this script is in maya:
#you can type in these in the script editor:
import MyFunctionExample
#maya has to reload that script to execute
reload MyFunctionExample

MyFunctionExample.Foo()
#Then this function will be executed wen the last line is called

#however typing the name is too long, you can give it an alias:
import MyFunctionExample as mfe
reload mfe
mfe.Foo()

