# -*- coding: utf-8 -*-
"""
@author: Carmen
"""

# %% Let's start with the most popular first program to write.
# Hit <Shift> + <Enter> to run each cell.

print("Hello World!")

# %% We can manipulate strings.

name = "Carmen"

message1 = "Hello " + name + "!"
print(message1)

# %% I might want to print a hello message to whoever logs in. Whenever we
# find ourselves in a situation of reusing code but maybe only changing
# some values here or there, we should define a function.
# def name_of_function(arguments):
#     (function code)
#     return <a value or object we want to return, or None>

def hello_message():
    print("Hello!")
    
# %% All we did was define the function. Now let's evaluate it.
    
hello_message()

# %% Great! But we want it to be a bit more personal. We could modify the 
# function, but let's create a new one instead, because we could still use 
# the first one to greet guests. 

# Now we need pass an argument to the function with the person's username.

def hello_user(name):
    print("Hello " + name + "!")

username = "CrazyMath"
hello_user(username)
hello_user("DNARules")

# %% What could go wrong?
hellouser(username)

# we mispelt the function name

# %%
hello_user(Mary)

# Mary isn't a variable we've defined, so it should be "Mary" or 'Mary'.
# Important: Words surrounded with quotes are considered STRINGS.

