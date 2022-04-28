import time, sys, os, random

array_no_space_concise_uni = ["qKeltec", "KeltecVz", "KeltecDFS", "$Keltec", "0Keltec0", "1017Keltec", "Keltec3s", "Keltec2P", "qPremo", "PremoVz", "PremoDFS", "$Premo", "0Premo0", "1017Premo", "Premo3s", "Premo2P", "qMantra", "MantraVz", "MantraDFS", "$Mantra", "0Mantra0", "1017Mantra", "Mantra3s", "Mantra2P", "qSkulk", "SkulkVz", "SkulkDFS", "$Skulk", "0Skulk0", "1017Skulk", "Skulk3s", "Skulk2P", "qEclipse", "EclipseVz", "EclipseDFS", "$Eclipse", "0Eclipse0", "1017Eclipse", "Eclipse3s", "Eclipse2P", "qCastro", "CastroVz", "CastroDFS", "$Castro", "0Castro0", "1017Castro", "Castro3s", "Castro2P", "qSubzero", "SubzeroVz", "SubzeroDFS", "$Subzero", "0Subzero0", "1017Subzero", "Subzero3s", "Subzero2P", "qBizzy", "BizzyVz", "BizzyDFS", "$Bizzy", "0Bizzy0", "1017Bizzy", "Bizzy3s", "Bizzy2P", "qXero", "XeroVz", "XeroDFS", "$Xero", "0Xero0", "1017Xero", "Xero3s", "Xero2P", "qDipset", "DipsetVz", "DipsetDFS", "$Dipset", "0Dipset0", "1017Dipset", "Dipset3s", "Dipset2P", "qBeeper", "BeeperVz", "BeeperDFS", "$Beeper", "0Beeper0", "1017Beeper", "Beeper3s", "Beeper2P", "qAves", "AvesVz", "AvesDFS", "$Aves", "0Aves0", "1017Aves", "Aves3s", "Aves2P", "qSantana", "SantanaVz", "SantanaDFS", "$Santana", "0Santana0", "1017Santana", "Santana3s", "Santana2P", "qSlang", "SlangVz", "SlangDFS", "$Slang", "0Slang0", "1017Slang", "Slang3s", "Slang2P", "qDuwap", "DuwapVz", "DuwapDFS", "$Duwap", "0Duwap0", "1017Duwap", "Duwap3s", "Duwap2P", "qSteeze", "SteezeVz", "SteezeDFS", "$Steeze", "0Steeze0", "1017Steeze", "Steeze3s", "Steeze2P", "qCelts", "CeltsVz", "CeltsDFS", "$Celts", "0Celts0", "1017Celts", "Celts3s", "Celts2P", "qBreezy", "BreezyVz", "BreezyDFS", "$Breezy", "0Breezy0", "1017Breezy", "Breezy3s", "Breezy2P", "qAntics", "AnticsVz", "AnticsDFS", "$Antics", "0Antics0", "1017Antics", "Antics3s", "Antics2P", "qOrnery", "OrneryVz", "OrneryDFS", "1Ornery", "0Ornery0", "1017Ornery", "Ornery3s", "Ornery2P", "qNascent", "NascentVz", "NascentDFS", "1Nascent", "0Nascent0", "1017Nascent", "Nascent3s", "Nascent2P", "qShroud", "ShroudVz", "ShroudDFS", "$Shroud", "0Shroud0", "1017Shroud", "Shroud3s", "Shroud2P", "qBertha", "BerthaVz", "BerthaDFS", "$Bertha", "0Bertha0", "1017Bertha", "Bertha3s", "Bertha2P", "qRusty", "RustyVz", "RustyDFS", "$Rusty", "0Rusty0", "1017Rusty", "Rusty3s", "Rusty2P", "qRampage", "RampageVz", "RampageDFS", "$Rampage", "0Rampage0", "1017Rampage", "Rampage3s", "Rampage2P"] #200 items, exhaustive lists are needed since if the array was full of complements and another was full of concise usernames, a random item being chosen for each respective array and added together would mean that there would be an extra space in the generated username
array_no_space_concise_no_uni = ["Keltec", "Premo", "Mantra", "Skulk", "Eclipse", "Castro", "Subzero", "Bizzy", "Xero", "Dipset" "Beeper", "Aves", "Santana", "Slang", "Duwap", "Steeze", "Celts", "Breezy", "Antics", "Ornery", "Nascent", "Shroud", "Bertha", "Rusty", "Rampage"] #25 items
array_no_space_no_concise_uni = ["qRekusuki", "RekusukiVz", "RekusukiDFS", "$Rekusuki", "0Rekusuki0", "1017Rekusuki", "Rekusuki3s", "Rekusuki2P", "qSemantic", "SemanticVz", "SemanticDFS", "$Semantic", "0Semantic0", "1017Semantic", "Semantic3s", "Semantic2P", "qPineault", "PineaultVz", "PineaultDFS", "$Pineault", "0Pineault0", "1017Pineault", "Pineault3s", "Pineault2P", "qHalfnHalf", "HalfnHalfVz", "$HalfnHalf", "0HalfnHalf", "1017HalfnHalf", "HalfnHalf3s", "HalfnHalf2P", "qGetBread", "GetBreadVz", "GetBreadDFS", "$GetBread", "0GetBread0", "1017GetBread", "GetBread3s", "GetBread2P", "qDarkiesha", "DarkieshaVz", "DarkieshaDFS", "$Darkiesha", "0Darkiesha0", "1017Darkiesha", "Darkiesha3s", "Darkiesha2P", "qPackrunner", "PackrunnerVz", "PackrunnerDFS", "$Packrunner", "0Packrunner0", "1017Packrunner", "Packrunner3s", "Packrunner2P", "qArsenics", "ArsenicsVz", "ArsenicsDFS", "$Arsenics", "0Arsenics0", "1017Arsenics", "Arsenics3s", "Arsenics2P", "qPeacekeeper", "PeacekeeperVz", "PeacekeeperDFS", "$Peacekeeper", "0Peacekeeper0", "1017Peacekeeper", "Peacekeeper3s", "Peacekeeper2P", "qSpriteTech", "SpriteTechVz", "SpriteTechDFS", "$SpriteTech", "0SpriteTech0", "1017SpriteTech", "SpriteTech3s", "SpriteTech2P", "qIndominus", "IndominusVz", "IndominusDFS", "$Indominus", "0Indominus0", "1017Indominus", "Indominus3s", "Indominus2P", "qBludgeon", "BludgeonVz", "BludgeonDFS", "$Bludgeon", "0Bludgeon0", "1017Bludgeon", "Bludgeon3s", "Bludgeon2P", "qChromium", "ChromiumVz", "ChromiumDFS", "$Chromium", "0Chromium0", "1017Chromium", "Chromium3s", "Chromium2P", "qLeviathan", "LeviathanVz", "LeviathanDFS", "$Leviathan", "0Leviathan0", "1017Leviathan", "Leviathan3s", "Leviathan2P", "qPenultimate", "PenultimateVz", "PenultimateDFS", "$Penultimate", "0Penultimate0", "1017Penultimate", "Penultimate3s", "Penultimate2P", "qBullwhip", "BullwhipVz", "BUllwhipDFS", "$Bullwhip", "0Bullwhip0", "1017Bullwhip", "Bullwhip3s", "Bullwhip2P", "qJubilees", "JubileesVz", "JubileesDFS", "$Jubilees", "0Jubilees0", "1017Jubilees", "Jubilees3s", "Jubilees2P", "qAutomatic", "AutomaticVz", "AutomaticDFS", "Automatic", "0Automatic", "1017Automatic", "Automatic3s", "Automatic2P", "qAudacity", "AudacityVz", "AudacityDFS", "$Audacity", "0Audacity0", "1017Audacity", "Audacity3s", "Audacity2P", "qCraniacs", "CraniacsVz", "CraniacsDFS", "$Craniacs", "0Craniacs0", "1017Craniacs", "Craniacs3s", "Craniacs2P"] #160 items
array_no_space_no_concise_no_uni = ["Rekusuki", "Semantic", "Pineault", "HalfnHalf", "GetBread", "Darkiesha", "Packrunner", "Arsenics", "Peacekeeper", "SpriteTech", "Indominus", "Bludgeon", "Chromium", "Leviathan", "Penultimate", "Bullwhip", "Jubilees", "Automatic", "Audacity", "Craniacs" ] #20 items
array_space_uni = ["qDouble G", "Double GVz", "Double GDFS", "$Double G", "0Double G0", "1017Double G", "Double G3s", "Double G2P", "qElite Ammo", "Elite AmmoVz", "Elite AmmoDFS", "$Elite Ammo", "0Elite Ammo", "1017EliteAmmo", "EliteAmmo3s", "EliteAmmo2P", "qKill Switch", "Kill SwitchVz", "Kill SwitchDFS", "$Kill Switch", "0Kill Switch", "1017Kill Switch", "Kill Switch3s", "Kill Switch2P", "qDeath Stalker", "Death StalkerVz", "Death StalkerDFS", "$Death Stalker", "0Death Stalker0", "1017Death Stalker", "Death Stalker3s", "Death Stalker2P", "qDigital Enigma", "Digital EnigmaVz", "Digital EnigmaDFS", "$Digital Enigma", "0Digital Enigma0", "1017Digital Enigma", "Digital Enigma3s", "Digital Enigma2P", "qOG Casaonova", "OG CasanovaVz", "OG CasanovaDFS", "$OG Casanova", "1017OG Casanova", "OG Casanova3s", "OG Casanova2P", "qTinfoil Hat", "Tinfoil HatVz", "Tinfoil HatDFS", "$Tinfoil Hat", "0Tinfoil Hat0", "1017Tinfoil Hat", "Tinfoil Hat3s", "Tinfoil Hat2P", "qCough Syrup", "Cough SyrupVz", "Cough SyrupDFS", "$Cough Syrup", "0Cough Syrup0", "1017Cough Syrup", "Cough Syrup3s", "Cough Syrup2P", "qNight Watcher", "Night WatcherVz", "Night WatcherDFS", "$Night Watcher", "0Night Watcher0", "1017Night Watcher", "Night Watcher3s", "Night Watcher2P", "qUndead Alive", "Undead AliveVz", "Undead AliveDFS", "$Undead Alive", "0Undead Alive0", "1017Undead Alive", "Undead Alive3s", "Undead Alive2P", "qWorst Nightmare", "Worst NightmareVz", "Worst NightmareDFS", "$Worst Nightmare", "0Worst Nightmare0", "1017Worst Nightmare", "Worst Nightmare3s", "Worst Nightmare2P", "qShort Fury", "Short FuryVz", "Short FuryDFS", "$Short Fury", "0Short Fury0", "1017Short Fury", "Short Fury3s", "Short Fury2P", "qMolly Wap", "Molly WapVz", "Molly WapDFS", "$Molly Wap", "0Molly Wap0", "1017Molly Wap", "Molly Wap3s", "Molly Wap2P", "qBlank Space", "Blank SpaceVz", "Blank SpaceDFS", "$Blank Space", "0Blank Space0", "1017Blank Space", "Blank Space3s", "Blank Space2P", "qBag Chaser", "Bag ChaserVz", "Bag ChaserDFS", "$Bag Chaser", "0Bag Chaser0", "1017Bag Chaser", "Bag Chaser3S", "Bag Chaser2P", "qThe Reaper", "The ReaperVz", "The ReaperDFS", " $The Reaper", "0The Reaper0", "1017The Reaper", "The Reaper3s", "The Reaper2P", "qFalse Hope", "False HopeVz", "False HopeDFS", "$False Hope", "0False Hope0", "1017False Hope", "False Hope3s", "False Hope2P", "qFlash Bang", "Flash BangVz", "Flash BangDFS", "$Flash Bang", "0Flash Bang0", "1017Flash Bang", "Flash Bang3s", "Flash Bang2P", "qPoint Blank", "Point BlankVz", "Point BlankDFS", "$Point Blank", "0Point Blank0", "1017Point Blank", "Point Blank3s", "Point Blank2P", "qCross Hair", "Cross HairVz", "Cross HairDFS", "$Cross Hair", "0Cross Hair0", "1017Cross Hair", "Cross Hair3s", "Cross Hair2P"] #160 items
array_space_no_uni = ["Double G", "Elite Ammo", "Kill Switch", "Death Stalker", "Digital Enigma", "OG Casanova", "Tinfoil Hat", "Cough Syrup", "Night Watcher", "Undead Alive", "Worst Nightmare", "Short Fury", "Molly Wap", "Blank Space", "Bag Chaser", "The Reaper", "False Hope", "Flash Bang", "Point Blank", "Cross Hair"] #20 items, unable to be split into 2 arrays due to username prefixes not being interchangeable

while True: 
  def prompt(text):
    for character in text: # This function is taken from https://www.101computing.net/python-typing-text-effect/. All credit for this function is given to their rightful creators.
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(.03)
      
  prompt("Welcome to the Random Username Generator! Make sure that all prompts are loaded before responses are given. Not all usernames are created equal. Please reroll as needed and enjoy! A Y/N system will be put into place. Y for Yes and N for No. Type Y or N to continue and notion that you understand.") # this prompt is necessary to implement break and start process
  time.sleep(0.5)
  choice = input("\n" + "Y/N: ")
  try:
    assert choice.lower() == "y" or choice.lower() == "n" 
    if choice.lower() == 'y':
      prompt("Great!" + "\n")
      break
    elif choice.lower() == 'n':
      prompt("Awesome!" + "\n")
      break
  except AssertionError:
    prompt("Please enter Y/y or N/n" + "\n")
    quit()

def no_space_concise_uni(): #functions need to be defined before being called so they are placed in descending order of how they appear to the user
  prompt("Here is your username, thanks for playing: ")
  prompt(random.choice(array_no_space_concise_uni))
  time.sleep(0.5)
  choice = input("\n" + "Do you want to reroll? Duplicates may occur." + "\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    while choice.lower() == "y":
      os.system('clear')
      no_space_concise_uni()
      choice=""
  except AssertionError:
    prompt("Please enter Y/y or N/n ")  


def no_space_concise_no_uni(): 
  prompt("Here is your username, thanks for playing: ")
  prompt(random.choice(array_no_space_concise_no_uni))
  time.sleep(0.5)
  choice = input("\n" + "Do you want to reroll? Duplicates may occur." + "\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    while choice.lower() == "y":
      os.system('clear')
      no_space_concise_no_uni()
      choice=""
  except AssertionError:
    prompt("Please enter Y/y or N/n ") 

def no_space_no_concise_uni(): 
  prompt("Here is your username, thanks for playing: ")
  prompt(random.choice(array_no_space_no_concise_uni))
  time.sleep(0.5)
  choice = input("\n" + "Do you want to reroll? Duplicates may occur." + "\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    while choice.lower() == "y":
      os.system('clear')
      no_space_no_concise_uni()
      choice=""
  except AssertionError:
    prompt("Please enter Y/y or N/n ") 

def no_space_no_concise_no_uni(): 
  prompt("Here is your username, thanks for playing: ")
  prompt(random.choice(array_no_space_no_concise_no_uni))
  time.sleep(0.5)
  choice = input("\n" + "Do you want to reroll? Duplicates may occur." + "\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    while choice.lower() == "y":
      os.system('clear')
      no_space_no_concise_no_uni()
      choice=""
  except AssertionError:
    prompt("Please enter Y/y or N/n ") 

def space_uni(): 
  prompt("Here is your username, thanks for playing: ")
  prompt(random.choice(array_space_uni))
  time.sleep(0.5)
  choice = input("\n" + "Do you want to reroll? Duplicates may occur." + "\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    while choice.lower() == "y":
      os.system('clear')
      space_uni()
      choice=""
  except AssertionError:
    prompt("Please enter Y/y or N/n ") 

def space_no_uni(): 
  prompt("Here is your username, thanks for playing: ")
  prompt(random.choice(array_space_no_uni))
  time.sleep(0.5)
  choice = input("\n" + "Do you want to reroll? Duplicates may occur." + "\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    while choice.lower() == "y":
      os.system('clear')
      space_no_uni()
      choice=""
  except AssertionError:
    prompt("Please enter Y/y or N/n ") 
    
def no_space_concise():
  prompt("One last question. Do you need to make your username unique? Concise usernames are often taken. Some examples of concise but unique usernames are 'AvesVZ' or 'qAves'")
  time.sleep(0.5)
  choice = input("\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n"
    choice = str(choice)
    if choice.lower() == 'y':
      no_space_concise_uni()
    elif choice.lower() == 'n':
      no_space_concise_no_uni()
  except AssertionError:
    prompt("Please enter Y/y or N/n ")  

def no_space_no_concise():
  prompt("One last question. Do you need to make your username unique? Certain usernames can be taken. Some examples of unique usernames without spaces are 'peacekeeper4L' or 'vPeacekeeper'")
  time.sleep(0.5)
  choice = input("\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    if choice.lower() == 'y':
      no_space_no_concise_uni()
    elif choice.lower() == 'n':
      no_space_no_concise_no_uni()
  except AssertionError:
    prompt("Please enter Y/y or N/n ")  

def space(): 
  prompt("Do you need to make your username unique? Certain usernames can be taken. Examples of unique usernames with spaces are 'Kill Switch24' or 'TYT Kill Switch'")
  time.sleep(0.5)
  choice = input("\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    if choice.lower() == 'y':
      space_uni()
    elif choice.lower() == 'n': 
      space_no_uni()
  except AssertionError:
    prompt("Please enter Y/y or N/n ")  
      
def no_space(): 
  prompt("Do you want your username to be concise? Concise usernames are one word and less than 8 letters for the sake of this generator. Some examples would be 'Aves' or 'Santana'")
  time.sleep(0.5)
  choice = input("\n" + "Y/N: ")
  try: 
    assert choice.lower() == "y" or choice.lower() == "n" 
    if choice.lower() == 'y':
      no_space_concise()
    elif choice.lower() == 'n': 
      no_space_no_concise()
  except AssertionError:
    prompt("Please enter Y/y or N/n ")
  
prompt("Would you like your username to have spaces in it?")
time.sleep(0.5)
choice = input("\n" + "Y/N: ")
try:
  assert choice.lower() == "y" or choice.lower() == "n" 
  if choice.lower() == 'y':
    space()
  elif choice.lower() == 'n':
    no_space()
except AssertionError:
    prompt("Please enter  Y/y or N/n ")
