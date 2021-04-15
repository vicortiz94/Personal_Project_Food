from decide import decide
from lookList import lookList
from updateInfo import updateInfo

if __name__ == '__main__':
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
      print('see ya!')
      break

    if ino == 'U':
      print('Are you updating the restaurant list (R) or the cooking list (C)?')
      print('To go back, Press M')
      while True:
        roc = input()
        
        if roc == 'M':
          print('')
          break

        if roc == 'R' or roc == 'C':
          print('')
          updateInfo(roc)
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
      print('Do you want to see the restaurant list (R) or the cooking list (C)?')
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