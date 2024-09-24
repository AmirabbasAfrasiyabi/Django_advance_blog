# Python functions are first-class objects
# Python objects can be callable

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# def compute_fibo(n):
#     """
#        return the nth of fibonachi sequences 
#     """
#     if n in [1,2]:
#         return n-1
#     else:

#         return( compute_fibo(n-1) +compute_fibo(n-2) )

# print(compute_fibo(10))
# print(compute_fibo.__name__)
# print(compute_fibo.__doc__)


# dynamically programing functions

# def compute_fibo(n):
#     """
#         return the nth of fibonachi sequences 
#     """
#     fib = [0] * (n+1)
#     fib[1] = 0
#     fib[2] = 1
#     for i in range(3, n+1):
#         fib[i] = fib[i-1] + fib[i-2]

#     return fib[n]

# print(type("compute_fibo"))
# print(compute_fibo(1000))
# print(compute_fibo.__name__)
# print(compute_fibo.__doc__)


# Functions can be stored in data structures

# def caesar_encrypt(s, n=7):

#     """
#     This function encrypts a string by shifting each character by n places in the alphabet.
#     """
#     s = list(s)
#     n %= 26
#     for i in range(len(s)):
#         s[i] = chr(((ord(s[i]) - 97 + n) % 26) + 97)
#     s = ''.join(s)

#     return s

# def caesar_decrypt(s, n=7):

#     """
#     This function decrypts a string by shifting each character by 26 - n places in the alphabet.
#     """
#     return caesar_encrypt(s, 26 - (n % 26))

# # def reversed_string(s):
# #     return s[::1]

# # def make_uppercases(s):
# #     return s.upper()

# s = "hello"
# print(type(s))
# print(s.upper())
# print(s.lower())
# print(s.capitalize())

# funcs = [
#     caesar_encrypt,
#     # reversed_string,
#     # make_uppercases,
#     lambda s: s[::-1],
#     str.upper,
# ]

# s = 'helloworld'
# for func in funcs:
#     s = func(s)
# print(s)
# print(type(s))

#this function uses packing to sum

# def mySum(*args):
#     print(args)
#     return sum(args)

# args = [1, 2, 3, 4]
# print(mySum(*args))

# def fun(*args, **kwargs): # packing
#     print(args)
#     print(kwargs)

# fun(*[1, 2, 3], a=1, b={'b': 6}, c='s') # unpacking

# def my_print(*args, end='\n', sep=' '):
#     print(*args, **kwargs)

# my_print(1, 2, end='')
# my_print(1, 2)

# def f(a=2, b=3):
#     print(a, b)
# f(None, 4)

# a = 2
# b = 3
# l = [2, 3]
# a, b = 2, 3
# print(a, b)

# Functions can be passed to other functions

# def my_map(func, items):
#     results = []
#     for item in items:
#         results.append(func(item))

#     return results

# # 1 2 3
# l = my_map(
#         int,
#         input().split())
# print(l)

# Functions can be nested

def f(text):
    def g():
        return text[::-1]

    return g().upper()

print(f('hello'))