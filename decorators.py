def decorator_function(original_function): 
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


def decorator_function_simple(original_function): 
    def wrapper_function(*args, **kwargs):
        
        print("Simplest decorator")
        original_function(*args, **kwargs)
        print("End of simplest dec")

    return wrapper_function




def my_timer(original_function):

    import time

    def wrapper(*args, **kwargs):

        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(original_function.__name__ , t2))
        return result

    return wrapper


@decorator_function_simple
def display(a, b):
    print('LOST AND FOUND :))')
    print("Sum of the two number is", a + b)


@my_timer
@decorator_function
def display_info(name, age):
    print("{} is {} years old today!".format(name, age))

# decorator_function(display)

## Decorated code
#display()


display(4, 6)





## Non-decorated code

# decorated_display = decorator_function(display)
# decorated_display()



