
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     return second_child

# print(parent(2)())


# Decorators wrap a function, modifying its behavior

# def my_decorator(func):
#     def wrapper():
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee():
#     print("Whee!")
# say_whee()

# Exercise: Write a decorator that
# prints BEFORE before calling the decorated function
# and AFTER afterwards.

# def before_and_after(func):
#     def wrapper(*args, **kwargs):
#         print('BEFORE')
#         result = func(*args, **kwargs)
#         print('AFTER')

#         return result

#     return wrapper


# @before_and_after
# def greet(name):
#     print(f'Hello, {name}!')

#     return 1

# result = greet('hassan')
# print(result) 


# Example: Timing
# import time

# def timeit(func):
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = func(*args, **kwargs)
#         t2 = time.time()
#         print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
#         return result
#     return wrapper

# @timeit
# def compute_fibo(n):
#     """
#        return the nth of fibonachi sequences 
#     """
#     if n in [1,2]:
#         return n-1
#     else:
#         return( compute_fibo(n-1) +compute_fibo(n-2) )
# print(compute_fibo(20))


import json
def cache(filepath):
    def decorator(func):
        cache_dict = {}
        try:
            with open(filepath, 'r') as f:
                cache_dict = json.load(f)
        except:
            pass
        def wrapper(*args, **kwargs):
            key = str(hash((*args, *kwargs.keys(), *kwargs.items())))
            if key not in cache_dict:
                cache_dict[key] = func(*args, **kwargs)
                with open(filepath, 'a') as f:
                    json.dump(cache_dict, f)

            return cache_dict[key]

        return wrapper

    return decorator

@cache('fib_cache.json')
def fib(n):
    """
        Calculates the nth term of fibonacci sequence
    """
    print(f'Calculating fib({n})...')
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(200))
print(fib(180))
print(fib(10))
