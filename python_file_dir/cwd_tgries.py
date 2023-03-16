import os

current_path = f"Current working directory is: {os.getcwd()}"
file_path = f"Pyhton File location is: {os.path.abspath(__file__)}"
print(current_path)
print(file_path)
with open('test.txt', 'a') as f:
    f.write(current_path)
    f.write(file_path)
