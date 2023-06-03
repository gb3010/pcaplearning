#!/usr/local/bin/python3
filename = 'test.txt'
another_file = 'file_write.txt'
with open(filename, 'r') as f:
    file_content = f.read()

# print(type(file_content)) Returns string as value
print(file_content)

with open(filename, 'r') as f2:
    file_lines = f2.readlines()

# print(type(file_lines)) Returns list as value
print(file_lines)

with open(filename, 'a') as f3:
    f3.write('Appending a new line')

with open(filename, 'r') as fread:
    file_after_append = fread.read()
print(file_after_append) # The new line gets appended without a prepending new line

with open(filename, 'a') as fappendnewline:
    file_after_append_newline = fappendnewline.write('\nThis is another line')

with open(filename, 'r') as fread:
    file_after_append_newline = fread.read()
print(file_after_append_newline) # Now the appended line is printed in a separate line due to prepending new line

with open(another_file, 'w') as fwrite:
    file_write = fwrite.write('This is a new file') # Creates the file another_file and writes the content

with open(another_file, 'r') as fread:
    another_file_write = fread.read()

print(another_file_write)

with open(another_file, 'r+') as fread_and_write: # This mode opens the file in both read and write mode. So, it overrites the existing content when written
    fread_and_write.write('\nAdding another line')

print(another_file)