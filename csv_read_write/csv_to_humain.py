"""
https://www.reddit.com/r/learnpython/comments/12k204q/opening_writing_saving_a_csv_file_on_mac/

Opening, Writing, Saving a csv file on Mac
Beginner level. I'm trying to open, and save a new csv file on mac, but I keep running into issues (trying to write row by row first. going to aggregate later) Any help on why this is not working would be appreciated. I think it is because I wrote the OS directory incorrectly, but it could be something else.

rows are: date, receipt_id, amount_id

the expected output on the new csv file is "on [date] the spending amount is $[amount]." which repeated row by row



import csv
import os

def modifycsv (folder):
    for file name in os.listdir(folder:
        with open(os.path.join("user/me/scripts","receipts.csv"), 'r') as csvfile:
            reader=csv.reader ( csvfile, delimiter = ' ', quotechar = ',')
            date = 0
            receipt_id = 0
            amount_id = 0
            for row in reader:
                rowsplit = row[0].split(",")
                print("on" , rowSplit[0] , "the spending amount is $", rowSplit[2],".")
                rownum= rownum+1
modifycsv("user/me/scripts/test.csv")
print("done")

"""

import csv
import os


def modify_csv(in_file_name: str, out_file_name: str, folder: str = '.', ):
    in_file_path = os.path.join(folder, in_file_name)
    out_file_path = os.path.join(folder, out_file_name)
    with open(in_file_path, 'r') as csvfile:
        data_iterator = csv.reader(csvfile)
        output_lines = [f"on {row[0]}, the spending amount is ${row[2].strip()}.\n" for row in data_iterator]

    with open(out_file_path, 'w') as output_file:
        output_file.writelines(output_lines)


if __name__ == '__main__':
    modify_csv('in.csv', 'out.txt')
