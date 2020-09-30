# infile = open("MyDataFile.txt", "r")
# outfile = open("results.txt", "w")
#
# pass
#
# infile.close()
# outfile.close()

# alternate method for opening files
# this method automatically closes your file for your block is finished

with open("MyDataFile.txt", "r") as infile:

    pass

# open and write to a file
writefile = open("writefile.txt", "w")
writefile.write("This line is written to the file")
writefile.close()

# open and read from file via loop
readfile = open("readfile.txt", "r")

for line in readfile:
    line = readfile.readline()
    print(line[2, 4, ])
# second_line = readfile.readline()
# print(first_line)
# print(second_line)

readfile.close()

# read entire file with file.read() instead of file.readline()
myfile = open("myfile.txt", "r")
myfile.read()
myfile.close()

# reading or writing binary files

# write
mybin = open("mybin", "wb")

# append
mybin = open("mybin", "ab")

# read
mybin = open("mybin", "rb")

# check out the pickle module for binary file manipulation

# tripple quotes will signify a string with implied new-lines:

"""Three quotes in a row are
pretty awesome things
they let you do things like this ..."""

'''You can also do it with single quotes
see? pretty crazy ...
right?'''

# If you want to lay out some multi-line comments
"""Using the tripple quoted string
is totally acceptable,
in the case that you - or I were
totally unawares"""

































