# Test Automation University Notes

# Functions

# def addStuff():
#     # always indent the function body bits 4 spaces
#     a = 10
#     b = 333
#     print(a+b)

# # now call the function to start using it

# addStuff()


# # # Get user input
# # remember that input always returns a string, so you'll need to cast it as int if you want user to enter integers
# # input('give me a number')

# def addition():
#     # use the int to convert the user input to integer
#     c = int(input('give me number a number: '))
#     d = int(input('give me number a 2nd number: '))    
#     print('Your result is : ' + (str(c+d)))

# addition()



# args & kwargs (arguments & keyword arguments)

# def user_info(name, age, city):
#     # create a docstring
#     ''' this function prints print name, age and city'''
#     # now print out this sentence sticking the arguments into the curly braces
#     print("{} is {} years old and from {}".format(name, age, city))

# # you gotta match up the number of variables
# # Python is reading the arguments in order, in this case for the positional arguments
# print ('printing the regular args output')
# user_info("Janet", 58, "Oklahoma City")

# # So let's use kwargs (keyword arguments)
# def user_info2(name="Args1", age=3, city='Scottsdale'):
#     print("{} is {} years old and from {}".format(name, age, city))

# # # so here you can just fill in the needed bits, any not included will just pull the defaults
# user_info2(name = 'Args2', age=33)

# So if you try args w/o populating all the elements you'll get a syntax error'
# and with keyword arguments you don't need to follow the same positions when you call the function

# # https://testautomationu.applitools.com/python-tutorial/chapter3.html
# # What about *args and **kwargs?
# # *args - allows for unlimited variables to be passed into a function w/o defining them ahead of time
# # ex of addition with the ability to pull in any number of args
# def addItUp(*args):
#     print(sum(args))
# addItUp(33, 33, 33, 33, 33)


# # **kwargs - allows for unlimited keywoard arguments to be passed into a function w/o defining them ahead of time
# def application(**kwargs):
#     print(**kwargs)

# application('nancy', 'bo')

# https://testautomationu.applitools.com/python-tutorial/chapter3.html at 7:39
# All 3 argument types can be used in a single function. 
# They must be used in order: 
# formal positional arguments,
#  *args, 
# **kwargs

# ex. 
def application2(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. her. Their email is {}.".format(fname, lname, company, email))

# so you'll need to have the args added to the function call here to avoid errors'
application2('first', 'last', 'mo@mo.com', 'WFH Inc')

# see also my Jupyter Notebook on this: http://localhost:8888/notebooks/Desktop/PythonProjects/FunctionsAndArgsAndKwargs.ipynb


