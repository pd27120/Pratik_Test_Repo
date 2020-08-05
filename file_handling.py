""" Erases file content, write into the file and read it. """


with open('newfile.txt', 'w') as f:
    f.truncate(0)  # erases older content
    f.write("This is a test file\n")

with open('newfile.txt', 'r') as f:
    print(f.read())
