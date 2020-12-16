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



# Conditionals -> https://testautomationu.applitools.com/python-tutorial/chapter4.html
# Comparison operaters refresher: <, >, ==, <=, !=
# Booleans -> True, False

# print('Should be True')
# print(2==2)
# print('Should be True')
# print(3>1)
# print('Should be True')
# print(3!=1)
# print('Should be False') 
# print(3==1)


# if - shows code that should run only if certain conditions are met 
# elif - code that should run when conditions before are not met, but many conditions could possibly be met. Run in the order that it appears
# else - closes out the above, comprises anything that the user might not do  
# Drill thru these

# design w order in mind, once the condition is met, none of the other conditions matter!

# Addition
def add():
    a = float(input('enter a number to add: '))
    b = float(input('enter another number to add: '))
    # print('here is your sum: ' + ((float)(a+b))
    print('Your sum is : ' + (str(a+b)))

# Subtraction
def subtraction():
    a = float(input('enter a number to subtract: '))
    b = float(input('enter another number to subtract: '))
    print('Your difference is : ' + (str(a-b))) 

# Multiplication
def multiply():
    a = float(input('enter a number to multiply: '))
    b = float(input('enter another number to multiply: '))
    print('Your product is : ' + (str(a*b))) 

# Division
def division():
    a = float(input('enter a number to divide: '))
    b = float(input('enter another number to divide: '))
    print('Your division result is : ' + (str(a/b))) 

# Now make a place to call the functions
# so when you run this it's just going to go in order, calling each function
# add()
# subtraction()
# multiply()
# division()


# now let's give the user choice
# create a variable 
operation = input('please enter +, -, *, /: ')

if operation == '+':
    add()
elif operation == '-':
    subtraction()
elif operation =='*':
    multiply()
elif operation == '/':
    division()
else:
    print('you have failed me for the last time!')


# Finished that review
# https://testautomationu.applitools.com/python-tutorial/chapter5.html
# now loops again, going thru it quick

