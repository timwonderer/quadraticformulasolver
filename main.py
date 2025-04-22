from quadratic_function_solver import quadratic_formula_by_parts

def input_check(num):
    try:
        num = int(num)
    except ValueError:
        print ("Invalid entry. Please try again.")
        return (False, None)
    else:
        return (True, num)



def main():
    print("Quadratic Formula Solver")
    print("Please enter the coefficient of your quadratic function when prompted. If the coefficient doesn't exist, write 0.")
    print ("----------------------------------------")
    
    count = 0
    coefficients = {"a":0, "b":0, "c":0}
    repeat = True
    while repeat == True:
      for coefficient in coefficients:
          valid_input = False
          while valid_input == False:
              user_input = input ("Please enter the coefficient '"+str(coefficient)+"' as an integer value: ")
              print ()
              if coefficient == "a" and user_input == "0":
                print ("-------------CAUTION!------------")
                print ("If coefficient 'a' is zero, this function is actually a linear function and cannot be solved with the quadratic formula.")
                print ("---------------------------------")
                try_again = input("Do you wish to try again? Enter Y for yes:")
                print ("=================================")
                try_again.lower()
                if try_again == "y":
                  continue
                else:
                  print ("Program ends.")
                  quit()
              valid_input, num = input_check(user_input)
              if valid_input == True:
                  coefficients[coefficient]=num
      answers = quadratic_formula_by_parts (coefficients)
      print ("Solution for the entered equation:")
      for answer in answers:
        print ("x =", answer)
      print ()
      reset = input("Enter 'Y' to start this tool again. Any other keys to exit.").upper()
      repeat = True if reset == 'Y' else print ("Program ends.")
      print ()
    exit ()


if __name__ == "__main__":
  main()
