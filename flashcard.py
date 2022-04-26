# the idea is that you should be able to squentially see card and then after input show it's definition

# I need to read the information from  the file so... yeah

# aconyms and defs that connected with a dictionary
answer_key = {}

with open("Acronyms.txt", 'r') as file:
    # now I have to go line by line reading eveything in file
    for line in file.readlines():
        #split the word and the definition based on a colon, and then set their index's to variables
        line = line.split(':')
        Acro = line[0]
        Def = line[1]

        # put the acro and def in that bad boy
        answer_key[Acro] = Def

for key, val in answer_key.items():
    print("============")
    print(key + ": " + val)
    # a break so that you can actually read it
    info = input("press q to quit, else press ENTER")
    if info == 'q':
        break
    else:
        pass

