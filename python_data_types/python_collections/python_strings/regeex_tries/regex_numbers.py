import logging
import re

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('logger')


def main():
    input_string = "There are only 78498 numbers under 1,000,000"

    finds: list[str] = re.findall("[0-9]+", input_string)
    print(f"{finds}")

    finds: list[str] = re.findall("[\\d,]+", input_string)
    print(f"{finds}")

    p = r'\b\d{1,2}\.\d{1,2}\.\d{2}(?:\d{2})?\b|\b(?<!\d[.,])(\d{1,3}(?=([.,])?)(?:\2\d{3})*|\d+)(?:(?(2)(?!\2))[.,](\d+))?\b(?![,.]\d)'
    finds: list[str] = re.compile(p).findall(input_string)
    print(f"{finds}")



if __name__ == '__main__':
    main()
