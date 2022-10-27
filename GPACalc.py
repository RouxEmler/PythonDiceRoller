#---Functions--------------------
def spacer():
  print("-----------------------------------")

def pop_students(old_names, old_gpa):
  flag = True
  while flag == True:
    
    flag2 = True
    while flag2 == True:
      
      try:
        spacer()
        stu_count = int(input("How many students would you like to input: "))
        flag2 = False
      except:
        print("Not a valid entry, please try again. Error1")

    new_names = []
    new_gpa = []
    while stu_count > 0:
      
      try:
        spacer()
        student_name = str(input("Please input the student's name: "))
        new_names.append(student_name)
        student_gpa = float(input(f"What is {student_name}'s GPA: "))
        new_gpa.append(student_gpa)
        stu_count -= 1
  
      except:
        print("Not a valid entry, please try again. Error2")

    spacer()
    print("Here are the entered students:")
  
    for i in range(len(new_names)):
      print(f"{new_names[i]}: {new_gpa[i]} GPA")
  
    flag3 = True
    while flag3 == True:
      
      try:
        spacer()
        ans = str.lower(input("Are these correct?\n1. Yes\n2. No\n"))
        if ans == "1" or ans == "yes":
          for i in range(len(new_names)):
            old_names.append(new_names[i])
            old_gpa.append(new_gpa[i])
          flag = False
          flag3 = False
          
        elif ans == "2" or ans == "no":
          print("Let's try again.")
          flag3 = False
          
        else:
          print("Not a valid entry, please try again. Error3")
      except:
        print("Not a valid entry, please try again. Error4")

def print_average_gpa(student_gpas):
  to_gpa = sum(student_gpas)
  
  if len(student_gpas) > 0:
    av_gpa = to_gpa/len(student_gpas) 
    print(f"The average student GPA is {av_gpa:.1f}")
  else:
    print("No current students in the system.")

#---Main----------------------------
def main(student_names, student_gpas):
  #------Header-------------------
  spacer()
  print("-----Student Data Entry System-----")
  #---Call Subfunctions--------------
  cont = True
  while cont == True:
    try:
      spacer()
      ans = str.lower(input("Do you have more GPAs to enter?\n1. Yes\n2. No\n"))
      if ans == "1" or ans == "yes":
        pop_students(student_names, student_gpas)
      elif ans == "2" or ans == "no":
        print_average_gpa(student_gpas)
        cont = False
      else:
        print("Not a valid entry, please try again. Error5")
    except:
      print("Not a valid entry, please try again. Error6")

#------Variables------------------
student_names = []
student_gpas = []

#-----Call Main-----------------
main(student_names, student_gpas)