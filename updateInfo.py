from lookList import lookList

def updateInfo(x):
  name = ''
  position = ''
  eatOrAdd = ''

  if x == 'R':
    title = 'restaurant'

  if x == 'C':
    title = 'dish'

  print('Did you recently eat something? or are you adding something new to the list?')
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
      print('lets add an option! First, lets take a look at the list!')
      lookList(x)
      print('Whats the name of the ' + title + '?')
      print('Or, press M to go back to menu')
      A = input()
      print('')
			
      if A == 'M':
        return

      name = A
      print('The name is ' + name + '. press Y if that is correct, anything else if it isn\'t')

      nameExit = input()
      if nameExit == 'Y':
        break
      print('')

    while True:
      print('')
      print('Do you want it at the front (F) of the que or the end (E)? ')
      print('(If you messed up the name, start over from the beginning. Press M')
      z = input()
      print('')

      if not (z == 'M' or z == 'F' or z == 'E'):
        print('bruh')
        continue

      if z == 'M':
        return

      if z == 'F':
        position = 'front'

      if z == 'E':
        position = 'end'

      print('We\'ll put it in the ' + position + '. is that alright? Type "Y" if that is correct, anything else if it isn\'t')
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
    daList = "food_files/restaurant.txt"

  if x == 'C':
    daList = "food_files/cooking.txt"

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
    daList = "food_files/restaurant.txt"

  if x == 'C':
    daList = "food_files/cooking.txt"

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
      print('you ate ' + obList[daNumber - 1] + ' recently? if correct, press Y. If not, press anything else')
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