"""
**Kwargs. I understand the point and most of the syntax, but I'm having trouble handling the kwargs in the function. I have a function that needs to check to see if certain kwargs were entered.

def my_function(arg1, arg2, **kwargs):
    strangy = arg1 + arg2
    if kwargs["kwarg1"] in kwargs:
        strangy += kwargs["kwarg1"]
    if kwargs["kwarg2"] in kwargs:
    strangy += kwargs["kwarg2"]
    return strangy
The kwargs key is being evaluated before the "in kwargs" part so its failing there, which makes sense. But this is what I need (or I think I need). I want to skip adding the arguments that arent entered, but I need to add the ones that are.

I guess I could loop through the kwargs dictionary and just add everything that's in there which would solve the problem, but it seems like that defeats the purpose of kwargs. I might have values entered into the kwargs argument that need to be processed differently.

Any help is appreciated! I might just be approaching the problem incorrectly. I often find this to be the case when I get stuck like this. Round peg, square hole.
"""


def my_function(arg1, arg2, **kwargs):
    strangy = arg1 + arg2
    if "kwarg1" in kwargs:
        strangy += kwargs["kwarg1"]
    if "kwarg2" in kwargs:
        strangy += kwargs["kwarg2"]
    return strangy


if __name__ == '__main__':
    print(my_function(10, 12, kwarg1=1000, kwarg3=10000))