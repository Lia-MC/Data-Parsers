# load file
# read each line
# for each line, first val is __, second val is __, store them both in an array (2 lists)
# for each list put enter symbols after each of the values and print them separately 
# when user asks for it so that they have time to copy pasta the values into a sheet
# OR for each x, y value in the array, put it into an excel sheet column or plot it (using scipy...?)

import file 
arr1 = []
arr2 = []
counter = -1

filename = ""
while file.nextline != null:
    counter += 1
    temp = file.read(nextline)
    beforespace = True
    word1 = ""
    word2 = ""
    for char in temp:
        if beforespace and char == ' ':
            beforespace = False
        elif not beforespace and char == '/n':
            arr1[counter] = word1
            arr2[counter] = word2
        elif beforespace:
            word1 += char
        else:
            word2 += char