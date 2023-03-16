"""
https://www.reddit.com/r/learnpython/comments/11s8umf/writing_to_file_not_working/
For the last month I've been teaching myself Python, and currently working on a small program which I can expand on as I learn.

The purpose of the program is that the user can add or remove books from a .txt file. For some reason, my addBook() function is not writing to the file and I can't seem to figure out why.

In the same folder as my python file, I have a file 'books.txt'.

Success

But the file is empty.
"""


def addBook():
    """
        This function allows users to add books to the text file 'books.txt'
        """
    try:
        shelf = open("booksa.txt", 'a')

        title = input("Enter the book's name: ")
        author = input("Enter the author's name: ")
        isbn = input("Enter the book's ISBN: ")

        book_data = f"{title}, {author}, {isbn}\n"
        shelf.write(book_data)
        shelf.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    addBook()
