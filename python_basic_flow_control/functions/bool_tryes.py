import logging

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('KCL SCrapper')


def my_function():
    return False


def main():
    if not my_function():
        print(f'Function returns {False}')

    print(f'{my_function=} : {bool(my_function)=}')
    empty_list = []
    print(f'{empty_list=}, {bool(empty_list)=}')

    if my_function == False:
        print(f'Function object is {False}')


if __name__ == '__main__':
    main()
