import time
import sys
import os

while True:
  def prompt(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(.03)

  prompt("Welcome to the Random Username Generator! Would you like to keep this typewriting display effect? (Type Y for yes, N for no)")
  time.sleep(0.5)
  choice = input("\n" + "Y/N: ")
  try: 
    choice = str(choice)
    if choice == 'y':
      continue
    elif choice == 'n':
      print("You got it!")
      break
  except ValueError:
    print("Please select yes or no")
  except UnboundLocalError:
    print("{choice} is not Y or N")
  # except TypeError:
  #   print("Try again blud")
    
print("Would you like your username to have spaces in it?")
time.sleep(0.5)
choice = input("Y/N: ")
try:
  choice = str(choice)
  if choice == 'y':
    return no_space()
  elif choice == 'n':
    return space()
except ValueError:
  print("Please select yes or no")
except UnboundLocalError:
  print("{choice} is not Y or N")
      
  def no_space(): 
    print("Do you want your username to be concise? Concise usernames are one word. An example of a concise username would be 'Aves' or 'Santana'")
    time.sleep(0.5)
    choice = input("/n" + "Y/N: ")
    try: 
      choice = str(choice)
      if choice == 'y':
        return concise()
      elif choice == 'n': 
        return no_concise()
    except ValueError:
      print("Please select yes or no")
    except UnboundLocalError:
      print("{choice} is not Y or N")

  def concise():
    print("One last question. Do you need to make your username unique? Concise usernames are often taken. An example of a concise but unique username is 'AvesVZ' or 'qAves'")
    time.sleep(0.5)
    choice = input("/n" + "Y/N: ")
    try: 
      choice = str(choice)
      if choice == 'y':
        return no_space_concise_num()
      elif choice == 'n':
        return no_space_concise_no_num()
    except ValueError:
      print("Please select yes or no")
    except UnboundLocalError:
      print("{choice} is not Y or N")

  def no_space_concise_num():
    print("Here is your username, thanks for playing: ")
    # print(no_space_concise_num[random.randint(0,40)])
    time.sleep(0.5)
    input("Type any key if you want to reroll your username. Duplicates may occur.")
    os.system('clear')
    return no_space_concise_num()