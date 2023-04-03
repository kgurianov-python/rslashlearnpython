import fnmatch
import os
import pathlib
import shutil


def move_dir(src: str, dst: str, pattern: str = '*'):
    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        print(f)
        shutil.move(os.path.join(src, f), os.path.join(dst, f))



move_dir('source', 'dest', ['*.csv', '*.txt'])