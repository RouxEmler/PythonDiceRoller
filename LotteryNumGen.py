#----Functions------------------
def spacer():
  print("-------------------------------------------")


def rng():
  x = random.randint(1, 70)
  return x


def grng():
  x = random.randint(1, 25)
  return x


#------Importation-------------------
import random
import time
import os
#------Counter Variable----------------
attempt = 0
wnums = []
#-----Introduction----------------------
spacer()
print("---------Welcome to Roux's Lottery!--------")
#------Try Again Loop------------------------
again = True
while again == True:

  #------Variables----------------------
  wnums = []
  guess = []
  x = range(0, 5)
  cont = True
  again = True
  gorp = 0
  cont2 = True
  attempt += 1
  #------Pick Winning Numbers----------------
  for n in x:
    wnums.append(rng())
  
  wnums.append(grng())
  spacer()
    
  print(
      f"Attempt #{attempt}\nThe lottery numbers have been selected, input your guess to see if you've won!"
    )
  spacer()

  #-------Guess or Pick---------------
  while cont == True:
    try:
      ans = input(
        "Would you like to guess the winning numbers, or have them picked for you?\n1. Picked\n2. Guess\n"
      )
      spacer()
      if ans == "2" or ans.lower() == "guess":
        gorp = 1
        cont = False
      elif ans == "1" or ans.lower() == "picked":
        gorp = 2
        cont = False
      elif ans.lower() == "just let me win please":
        gorp = 1
        cont = False
        print(wnums)
      else:
        print("*Please select one of the two options.*")
    except:
      spacer()
      print("*1Invalid response, please try again.*")

#--------Guess------------------
  if gorp == 1:
    for n in x:
      cont = True
      while cont == True:
        try:
          gnum = int(input("Please input a number from 1-70: "))
          spacer()
          if gnum >= 1 and gnum <= 70:
            guess.append(gnum)
            cont = False
          else:
            print("*Invalid number, please try agian.*")
        except:
          spacer()
          print("*2Invalid response, please try again.*")

    cont = True
    while cont == True:
      try:
        ggnum = int(input("Now, please input a number from 1-25: "))
        spacer()
        if ggnum >= 1 and ggnum <= 25:
          guess.append(ggnum)
          cont = False
        else:
          print("*Invalid number, please try agian.*")
      except:
        spacer()
        print("*3Invalid response, please try again.*")

#---------Picked-------------------------------
  elif gorp == 2:
    for n in x:
      guess.append(rng())
    guess.append(grng())
    if attempt == 1000000:
      guess = wnums

#------Output----------------------------------
  if guess == wnums:
    print(f"Congradulations! You won the lottery!\nYour numbers: {guess}\nWinning numbers: {wnums}")
    break
  else:
    print(
      f"Sorry, better luck next time!\nYour numbers: {guess}\nWinning numbers: {wnums}"
    )
  spacer()

  #-----Try again--------------------------------
  while cont2 == True:
    try:
      ans = input("Would you like to try again?\n1. Yes\n2. No\n")
      if ans.lower() == "yes" or ans == "1":
        spacer()
        print("Let's go again!")
        time.sleep(.75)
        print("3..")
        time.sleep(.75)
        print("2..")
        time.sleep(.75)
        print("1..")
        time.sleep(.75)
        print("Go!")
        cont2 = False
        os.system('clear')
      elif ans.lower() == "no" or ans == "2":
        print("Thank you for playing, see you next time!")
        again = False
        cont2 = False
      else:
        spacer()
        print("*Please select one of the two options.*")
    except:
      spacer()
      print("*4Invalid response, please try again.*")
