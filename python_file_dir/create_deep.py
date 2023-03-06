import calendar
import os


def create_folder_tree(parent_dir, *childdirlists):
    """Takes parent folder string and optional lists of foldernames.
    Adds folders to each previous layer of folders."""

    # Create the parent dir if it does not exist.
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)

    # Recursively create child directories.
    if childdirlists:
        for child in childdirlists[0]:
            child_dir = os.path.join(parent_dir,child)
            create_folder_tree(child_dir, *childdirlists[1:])



def main():
    test = ['test2', 'test3', 'test4']
    parent_dir = 'root'
    filetypes = ['text','grids','images']
    years = [str(year) for year in range(2000, 2023)]
    months = [calendar.month_name[month] for month in range(1, 13)]
    days = [str(day) for day in range(31)]

    create_folder_tree(parent_dir, filetypes, years, months, days)


if __name__ == '__main__':
    main()
