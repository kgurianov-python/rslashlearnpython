"""
https://www.reddit.com/r/learnpython/comments/12chowd/why_am_i_getting_a_syntaxerror_invalid_syntax/

Why am I getting a "SyntaxError: invalid syntax" when using "@" for decorators?
I'm using SoloLearn to learn how Python. In one exercise, I'm asked:

Which statement can be used to achieve the same behavior as my_func = my_dec(my_func)?

@my_dec

my_func = @my_dec

my_dec(my_func)

The answer is 1, but I don't understand why. Using @my_dec gives me a SyntaxError: invalid syntax, and calling my_dec(my_func) should give me the same result. Is it an error of SoloLearn or am I missing something?

I created this script:

def my_dec(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def my_func():
  print(2)

print(my_dec(my_func))
But I get <function my_dec.<locals>.wrap at 0x7f19c6a151b0> as a return for some reason, instead of:

============
2
============
"""


def my_dec(func):
    def wrap():
        print(f" {func.__name__} ".center(20, '='))
        func()
        print("=" * 20)

    return wrap


@my_dec
def my_func():
    print(2)


def my_other_func():
    print(10)


if __name__ == '__main__':
    my_func()
    my_dec(my_other_func)()
