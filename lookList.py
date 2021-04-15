def lookList(x):

  if x == 'R':
    daList = "food_files/restaurant.txt"
    title = 'Restaurant'

  if x == 'C':
    daList = "food_files/cooking.txt"
    title = 'Dish'

  print('Here is the ' + title + ' list!')

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