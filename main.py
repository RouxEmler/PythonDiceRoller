#----Functions-------------------------
def spacer():
  print("-------------------------------")

def dice_count():
  flag = True
  while flag == True:
    try:
      dice_count = int(input("How many dice would you like to roll?\n"))
      flag = False
    except:
      print("Please enter a whole number. E1")
  return(dice_count)
      
def same():
  flag = True
  while flag == True:
    try:
      ans = ""
      ans = str(input("Do all the dice have the same number of sides?\n1. Yes\n2. No\n"))
      if ans == "1" or ans.lower() == "yes":
        same = True
        flag = False
      elif ans == "2" or ans.lower() == "no":
        same = False
        flag = False
      else:
        print("Invalid selection. E2")
    except:
      print("E3")
  return(same)

def pip_count(same, dice_count):
  pip_count = []
  flag = True
  while flag == True:
    try:
      if same == True:
        pip = int(input("How many sides do the dice have: "))
        if pip >= 2:
          for i in range(dice_count):
            pip_count.append(pip)
          return(pip_count)
          flag = False
        elif pip < 2:
          print("Please enter a number greater than 1. E4")
        else:
          print("E5")
          
      elif same == False:
        for i in range(dice_count):
          flag2 = True
          while flag2 == True:
            try:
              pip = int(input(f"How many sides does dice {i+1} have: "))
              if pip >= 2:
                pip_count.append(pip)
                flag2 = False
              elif pip < 2:
                print("Please enter a number greater than 1. E6")
              else:
                print("E7")
            except:
              print("Please enter an whole number. E8")
        return(pip_count)
        flag = False
        
      else:
        print("E9")
        
    except:
      print("E10")
  
def roll(pips):
  roll = []
  for i in pips:
    roll.append(random.randint(1, i))
  return(roll)

def p_roll(roll, pip_count):
  for i in range(len(roll)):
    print(f"D{pip_count[i]} rolled {roll[i]}")

def cont():
  flag = True
  while flag == True:
    try:
      ans = ""
      ans = str(input("Would you like to roll more dice?\n1. Yes\n2. No\n"))
      if ans == "1" or ans.lower() == "yes":
        again = True
        flag = False
      elif ans == "2" or ans.lower() == "no":
        again = False
        flag = False
      else:
        print("Invalid selection. E11")
    except:
      print("E12")
  return(again)
  
#-----Main function-------------------
def main():
  spacer()
  print("------Roux's Dice Roller!------")
  spacer()
  while True:
    d = dice_count()
    spacer()
    s = same()
    spacer()
    p = pip_count(s, d)
    spacer()
    r = roll(p)
    p_roll(r, p)
    spacer()
    c = cont()
    spacer()
    if c == False:
      print("Thanks for using Roux's Dice Roller")
      break
    else:
      print("Let's go again!")

import random
main()
