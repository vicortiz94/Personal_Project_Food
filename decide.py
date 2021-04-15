def decide(x):
  obList = []
  if x == 'R':
    daList = "food_files/restaurant.txt"

  if x == 'C':
    daList = "food_files/cooking.txt"

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
    print('How does ' + element + ' sound? Y for Yes for N for no. M to return')
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