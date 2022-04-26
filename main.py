import time
import sys
import os

while True:
  def prompt(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(.03)
      
  prompt("Welcome to the Random Username Generator! Not all usernames are created equal. Please reroll as needed and enjoy! A Y/N system will be put into place. Y for Yes and N for No. Type Y or N to continue and notion that you understand.")
  time.sleep(0.5)
  choice = input("\n" + "Y/N: ")
  try: 
    choice = str(choice)
    if choice.lower() == 'y':
      prompt("Great!" + "\n")
      break
    elif choice.lower() == 'n':
      prompt("Awesome!" + "\n")
      break
  except ValueError:
    print("Please select yes or no")
  except UnboundLocalError:
    print("{choice} is not Y or N")

def no_space_concise_uni():
    prompt("Here is your username, thanks for playing: ")
    # print(no_space_concise_uni[random.randint(0,40)])
    time.sleep(0.5)
    input(prompt("\n" + "Hit enter if you want to reroll your username. Duplicates may occur."))
    os.system('clear')
    no_space_concise_uni()

def no_space_no_concise_uni():
    prompt("Here is your username, thanks for playing: ")
    # print(no_space_no_concise_uni[random.randint(0,40)])
    time.sleep(0.5)
    input(prompt("\n" + "Hit enter if you want to reroll your username. Duplicates may occur."))
    os.system('clear')
    no_space_concise_uni()

def no_space_no_concise1():
    prompt("Here is your username, thanks for playing: ")
    # print(no_space_no_concise[random.randint(0,40)])
    time.sleep(0.5)
    input(prompt("\n" + "Hit enter if you want to reroll your username. Duplicates may occur."))
    os.system('clear')
    no_space_concise_uni()

def space_no_uni():
    prompt("Here is your username, thanks for playing: ")
    # print(space_no_uni[random.randint(0,40)])
    time.sleep(0.5)
    input(prompt("\n" + "Hit enter if you want to reroll your username. Duplicates may occur."))
    os.system('clear')
    no_space_concise_uni()

def space_uni():
    prompt("Here is your username, thanks for playing: ")
    # prompt(space_uni[random.randint(0,40)])
    time.sleep(0.5)
    input(prompt("\n" + "Hit enter if you want to reroll your username. Duplicates may occur."))
    os.system('clear')
    no_space_concise_uni()
  
def no_space_concise():
    prompt("One last question. Do you need to make your username unique? Concise usernames are often taken. Some examples of concise but unique usernames are 'AvesVZ' or 'qAves'")
    time.sleep(0.5)
    choice = input("\n" + "Y/N: ")
    try: 
      choice = str(choice)
      if choice.lower() == 'y':
        no_space_concise_uni()
      elif choice.lower() == 'n':
        no_space_concise_no_uni()
    except ValueError:
      print("Please select yes or no")
    except UnboundLocalError:
      print("{choice} is not Y or N")

def no_space_no_concise():
    prompt("One last question. Do you need to make your username unique? Certain usernames can be taken. Some examples of unique usernames without spaces are 'peacekeeper4L' or 'vPeacekeeper'")
    time.sleep(0.5)
    choice = input("\n" + "Y/N: ")
    try: 
      choice = str(choice)
      if choice.lower() == 'y':
        no_space_no_concise_uni()
      elif choice.lower() == 'n':
        no_space_no_concise1()
    except ValueError:
      print("Please select yes or no")
    except UnboundLocalError:
      print("{choice} is not Y or N")

def space(): 
    prompt("Do you need to make your username unique? Certain usernames can be taken. Examples of unique usernames with spaces are 'Kill Switch24' or 'TYT Kill Switch'")
    time.sleep(0.5)
    choice = input("\n" + "Y/N: ")
    try: 
      choice = str(choice)
      if choice.lower() == 'y':
        space_uni()
      elif choice.lower() == 'n': 
        space_no_uni()
    except ValueError:
      print("Please select yes or no")
    except UnboundLocalError:
      print("{choice} is not Y or N")   
      
def no_space(): 
    prompt("Do you want your username to be concise? Concise usernames are one word and less than 8 letters for the sake of this generator. Some examples would be  'Aves' or 'Santana'")
    time.sleep(0.5)
    choice = input("\n" + "Y/N: ")
    try: 
      choice = str(choice)
      if choice.lower() == 'y':
        no_space_concise()
      elif choice.lower() == 'n': 
        no_space_no_concise()
    except ValueError:
      print("Please select yes or no")
    except UnboundLocalError:
      print("{choice} is not Y or N")   
      
prompt("Would you like your username to have spaces in it?")
time.sleep(0.5)
choice = input("\n" + "Y/N: ")
try:
  choice = str(choice)
  if choice.lower() == 'y':
    space()
  elif choice.lower() == 'n':
    no_space()
except ValueError:
  print("Please select yes or no")
except UnboundLocalError:
  print("{choice} is not Y or N")
      
  
# def no_space_concise_num():
#     print("Here is your username, thanks for playing: ")
#     # print(no_space_concise_num[random.randint(0,40)])
#     time.sleep(0.5)
#     input("Hit enter if you want to reroll your username. Duplicates may occur.")
#     os.system('clear')
#     no_space_concise_num()

# def no_space_no_concise_num():
#     print("Here is your username, thanks for playing: ")
#     # print(no_space_concise_num[random.randint(0,40)])
#     time.sleep(0.5)
#     input("Hit enter if you want to reroll your username. Duplicates may occur.")
#     os.system('clear')
#     no_space_concise_num()
   
# def concise():
#     print("One last question. Do you need to make your username unique? Concise usernames are often taken. Some examples of concise but unique usernames are 'AvesVZ' or 'qAves'")
#     time.sleep(0.5)
#     choice = input("Y/N: ")
#     try: 
#       choice = str(choice)
#       if choice.lower() == 'y':
#         no_space_concise_num()
#       elif choice.lower() == 'n':
#         no_space_concise_no_num()
#     except ValueError:
#       print("Please select yes or no")
#     except UnboundLocalError:
#       print("{choice} is not Y or N")

# def space(): 
#     print("Do you need to make your username unique? Certain usernames are often taken. Examples of unique usernames with spaces are 'Kill Switch24' or 'TYT Kill Switch'")
#     time.sleep(0.5)
#     choice = input("Y/N: ")
#     try: 
#       choice = str(choice)
#       if choice.lower() == 'y':
#         space_num()
#       elif choice.lower() == 'n': 
#         space_no_num()
#     except ValueError:
#       print("Please select yes or no")
#     except UnboundLocalError:
#       print("{choice} is not Y or N")   
      
# def no_space(): 
#     print("Do you want your username to be concise? Concise usernames are one word. Some examples would be  'Aves' or 'Santi'")
#     time.sleep(0.5)
#     choice = input("Y/N: ")
#     try: 
#       choice = str(choice)
#       if choice.lower() == 'y':
#         concise()
#       elif choice.lower() == 'n': 
#         no_concise()
#     except ValueError:
#       print("Please select yes or no")
#     except UnboundLocalError:
#       print("{choice} is not Y or N")   
# print("Would you like your username to have spaces in it?")
# time.sleep(0.5)
# choice = input("Y/N: ")
# try:
#   choice = str(choice)
#   if choice.lower() == 'y':
#     space()
#   elif choice.lower() == 'n':
#     no_space()
# except ValueError:
#   print("Please select yes or no")
# except UnboundLocalError:
#   print("{choice} is not Y or N")
      