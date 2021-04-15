# program to figure out what to eat
import sys


####this updates the list if places##########################################
def upDateInfo(x):
    name = ''
    position = ''
    eatOrAdd = ''

    if x == 'R':
        #    daList = open("restaurant.txt", "w+")
        title = 'Restaurant'

    if x == 'C':
        #    daList = open("cooking.txt", "w+")
        title = 'dish'

    print(
        'Did you recently eat something? or are you adding something new to the list?'
    )
    print('E for eat or A for Add, or M to return to the menu')
    while True:
        eatOrAdd = input()
        print('')
        if (eatOrAdd == 'A' or eatOrAdd == 'E' or eatOrAdd == 'M'):
            break
        print('E for eat, A for Add, or M for menu')

    if eatOrAdd == 'M':
        return

    if eatOrAdd == 'E':
        iAte(x)
        return

    if eatOrAdd == 'A':
        while True:
            print('lets add an option! Whats the name of the ' + title + '?')
            print('Or, press M to go back to menu')
            A = input()
            print('')

            if A == 'M':
                #daList.close()
                return

            name = A
            print('The name is ' + name +
                  '. press Y if that is correct, anything else if it isn\'t')

            nameExit = input()
            if nameExit == 'Y':
                break
            print('')

        while True:
            print('')
            print(
                'Do you want it at the front (F) of the que or the end (E)? ')
            print(
                '(If you messed up the name, start over from the beginning. Press M'
            )
            z = input()
            print('')

            if not (z == 'M' or z == 'F' or z == 'E'):
                print('bruh')
                continue

            if z == 'M':
                #daList.close()
                return

            if z == 'F':
                position = 'front'

            if z == 'E':
                position = 'end'

            print(
                'We\'ll put it in the ' + position +
                '. is that alright? Type "Y" if that is correct, anything else if it isn\'t'
            )
            posExit = input()
            if posExit == 'Y':
                break

        addToList(name, position, x)

        print('Cool, we added ' + name + ' to the ' + position +
              ' of the que.')
        print('')
        return


def addToList(n, p, x):
    obList = []

    if x == 'R':
        daList = "restaurant.txt"

    if x == 'C':
        daList = "cooking.txt"

    #I need to check if there is anything in the file
    with open(daList, 'r') as filehandle:
        filehandle.seek(0)

        while True:
            z = filehandle.readline()
            if z == '':
                break
            obList.append(z)

    if (n + '\n') in obList:
        print('its already here bro')
    else:
        if p == 'front':
            obList.insert(0, n + '\n')
        else:
            obList.append(n + '\n')

    with open(daList, 'w+') as filehandle:
        filehandle.seek(0)

        for entry in obList:
            filehandle.write(entry)
        filehandle.seek(0)
        print(filehandle.read())


def iAte(x):
    obList = []

    if x == 'R':
        daList = "restaurant.txt"

    if x == 'C':
        daList = "cooking.txt"

    with open(daList, 'r') as filehandle:
        filehandle.seek(0)

        while True:
            z = filehandle.readline()
            if z == '':
                break
            obList.append(z.replace('\n', ''))

    print(
        'What did you recently eat? input the correct number, or M to go back to the menu'
    )

    checker = 1
    for element in obList:
        print(str(checker) + '  ' + element)
        checker += 1
    print('')

    while True:
        daNumber = input()
        if daNumber == 'M':
            return
        daNumber = int(daNumber)
        if daNumber > 0 and daNumber < checker:
            print(
                'you ate ' + obList[daNumber - 1] +
                ' recently? if correct, press Y. If not, press anything else')
            lastCheck = input()
            if lastCheck == 'Y':
                print('Okay!')

                obList.append(obList[daNumber - 1])
                del obList[daNumber - 1]

                with open(daList, 'w+') as filehandle:
                    filehandle.seek(0)

                    for entry in obList:
                        filehandle.write(entry + '\n')
                    filehandle.seek(0)
                    print('')
                    print(filehandle.read())

                break
            print('Try again, or press M to go back')
            continue
        print('')
        print('its out of range! Try again, or press M to go back')

    return


########################################################################

#########This is to look at a list #################################


def lookList(x):

    if x == 'R':
        daList = "restaurant.txt"
        title = 'Restaurant'

    if x == 'C':
        daList = "cooking.txt"
        title = 'Dish'

    print('Lets look at the ' + title + ' list!')

    with open(daList, 'r') as filehandle:
        filehandle.seek(0)
        z = filehandle.readline()
        if z == '':
            print('This list is empty!')
            print('')
            return

        filehandle.seek(0)
        print(filehandle.read())
        return


#################################################

#######This brings up suggestions#########################################


def decide(x):
    obList = []

    if x == 'R':
        daList = "restaurant.txt"

    if x == 'C':
        daList = "cooking.txt"

    with open(daList, 'r') as filehandle:
        filehandle.seek(0)
        z = filehandle.readline()
        if z == '':
            print('This list is empty!')
            print('')
            return
        filehandle.seek(0)

        while True:
            z = filehandle.readline()
            if z == '':
                break
            obList.append(z.replace('\n', ''))

    for element in obList:
        print('How does ' + element +
              ' sound? Y for Yes for N for no. M to return')
        while True:
            deciding = input()
            print('')

            if deciding == 'M':
                return

            if deciding == 'Y':
                obList.append(element)
                obList.remove(element)
                with open(daList, 'w+') as filehandle:
                    filehandle.seek(0)

                    for entry in obList:
                        filehandle.write(entry + '\n')
                    filehandle.seek(0)
                    print('Enjoy your meal!')
                return

            if deciding == 'N':
                break

            print('Y for yes, N for no, M to return')

    print('those are all the suggestions I have :/ Try adding some more!')
    return


#########################################################################

#############The main code#############################################

print('Welcome!')
print('This application will make list for you to decide what to eat!')
print('Are we deciding? Or do you want to look at or updating a list?')
print('D for Decide , L to Look, and U for Update')
print('if you want to quit, type Q')

# main loop
while True:
    ino = input()
    print('')

    if ino == 'Q':
        sys.exit()

    if ino == 'U':
        print(
            'Are you updating the restaurant list (R) or the cooking list (C)?'
        )
        print('To go back, Press M')
        while True:
            roc = input()

            if roc == 'M':
                print('')
                break

            if roc == 'R' or roc == 'C':
                print('')
                upDateInfo(roc)
                break

            print('')
            print('Restaurant (R). Cooking (C), or Menu (M)')

    if ino == 'D':
        print('Are we going to a restaurant (R) or cooking something (C)?')
        print('To go back, Press M')
        while True:
            roc = input()

            if roc == 'M':
                print('')
                break

            if roc == 'R' or roc == 'C':
                print('')
                decide(roc)
                break

            print('')
            print('Restaurant (R). Cooking (C), or Menu (M)')

    if ino == 'L':
        print(
            'Do you want to see the restaurant list (R) or the cooking list (C)?'
        )
        print('To go back, Press M')
        while True:

            roc = input()

            if roc == 'M':
                print('')
                break

            if roc == 'R' or roc == 'C':
                print('')
                lookList(roc)
                #upDate()
                break

            print('')
            print('Restaurant (R). Cooking (C), or Menu (M)')
    print('')
    print('Type Q (quit), U (update), L (look) or D (decide),')
