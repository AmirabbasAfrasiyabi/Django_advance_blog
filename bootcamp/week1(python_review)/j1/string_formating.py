# Source: Python Tricks Book
# Recommended Book: CPython Internals


#     Old Style String Formatting


name = 'Bob'
print('Hello, %s' % name)

errno = 50159747054
print('%x' % errno)

print('Hey %s, there is a 0x%x error!' % (name, errno))




a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')

print(f'Hey {name}, there is a {errno:#x} error!')

# # """
# #     Template Strings
# # """

from string import Template
t = Template('Hey, $name!')
print(t.substitute(name=name))

# # Safer than f-strings:

SECRET = 'this-is-a-secret'
class Error:
    def __init__(self):
        pass
err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
print(user_input.format(error=err))

# user_input = '${error.__init__.__globals__[SECRET]}'
# Template(user_input).substitute(error=err)
