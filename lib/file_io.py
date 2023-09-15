# The file_name can be a combined file path/name, you will need to add the .txt file extension to the 
# file_name when opening a file for all three of the methods.

# This function should use file_name and file_content to write a .txt file.
def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)

# Write a append_file function that takes in the same parameters and appends to the .txt file.
def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

# Write a read_file function that takes in a file name and returns the content of the .txt file.
def read_file(file_name):
    with open (f'{file_name}.txt') as f:
        return f.read()
