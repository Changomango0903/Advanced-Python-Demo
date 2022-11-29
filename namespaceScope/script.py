#Below shows all the built-in functions of python. This is the largest Namespace within python. This includes all built in functions we use every day.
print("Python built-in functions: ")
print(dir(__builtins__))

#Global variables are variables created within the code. Global namespace only contains items that are non-nested.
print(' -- globals() Namespace with empty script -- \n')
print(globals())

global_variable = 'global'
def print_global():
    global_variable = 'nested global'
    nested_variable = 'nested value'
print(' \n -- globals() Namespace non-empty script -- \n')
#notice how globals() namespace changes depending on the section of script.py it resides?
#This means that globals() shows the namespace at time of execution
print(globals())


