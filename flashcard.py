# the idea is that you should be able to squentially see card and then after input show it's definition

# I need to read the information from  the file so... yeah
with open("Acronyms.txt", 'r') as file:
    # now I have to go line by line reading eveything in file
    for line in file.readlines():
        #split the word and the definition based on a colon, and then set their index's to variables
        line = line.split(':')
        Acro = line[0]
        Def = line[1]
        print(Acro)
        input("press space when ready to see definition")
        print(Def)
        


